import os
import base64
from io import BytesIO
from PIL import Image
import numpy as np
from app import captioning, detection, classification, file_delete
from flask import Flask, send_file, request, jsonify, send_from_directory
from flask_cors import CORS
import shutil
import glob



app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("dist/" + path):
        return send_from_directory('dist', path)
    else:
        return send_from_directory('dist', 'index.html')


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
    
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def decode_base64_image(image_data):
    image_data = image_data.split(',')[1]
    img_bytes = BytesIO(base64.b64decode(image_data))
    img1 = Image.open(img_bytes)
    img = img1.convert('RGB')
    temp_image_path = os.path.join(UPLOAD_FOLDER, 'temp_image.jpg')
    img.save(temp_image_path)
    return temp_image_path

# @app.route("/")
# def index():
#     return send_file('web/index.html')


# @app.route('/api/process_images', methods=['POST', 'GET'])
# def process_images():
#     data = request.json.get('Images')
#     results = []
#     for image_data in data:
#         image_path = decode_base64_image(image_data)
#         detection_results = detection.perform_detection(image_path)
#         classification_result = classification.perform_classification(image_path)
#         captioning_results = captioning.generate_image_caption(image_path)

#         image_result = {
#             'detection': detection_results,
#             'classification': classification_result,
#             'captioning': captioning_results
#         }
#         results.append(image_result)
#     return jsonify(results)

@app.route('/api/process_images', methods=['POST', 'GET'])
def process_images():
    if request.content_type == 'application/json':
        data = request.json.get('Images')
        results = []
        for image_data in data:
            image_path = decode_base64_image(image_data)
            detection_results = detection.perform_detection(image_path)
            classification_result = classification.perform_classification(image_path)
            captioning_results = captioning.generate_image_caption(image_path)
            
            # Find the latest processed image
            latest_file = file_delete.get_latest_file('runs/detect/exp*/temp_image.jpg')

            # Convert processed image to base64 and include it in the response
            with open(latest_file, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode('utf-8')

            image_result = {
                'detection': detection_results,
                'classification': classification_result,
                'captioning': captioning_results,
                'image': 'data:image/jpeg;base64,' + encoded_string

            }
            
            # Delete the runs folder
            file_delete.delete_directory('runs')
            
            results.append(image_result)
        return jsonify(results)
    
    elif request.content_type.startswith('multipart/form-data'):
        if 'image' not in request.files:
            return jsonify(error='No image part in the request'), 400

        file = request.files['image']

        if file.filename == '':
            return jsonify(error='No selected file'), 400

        if file and allowed_file(file.filename):
            image = Image.open(file)
            image = image.convert('RGB')  # Convert image to 'RGB' mode
            image_path = os.path.join(UPLOAD_FOLDER, 'temp_image.jpg')
            image.save(image_path)

            detection_results = detection.perform_detection(image_path)
            classification_result = classification.perform_classification(image_path)
            captioning_results = captioning.generate_image_caption(image_path)
            
            # Find the latest processed image
            latest_file = file_delete.get_latest_file('runs/detect/exp*/temp_image.jpg')


            # Convert processed image to base64 and include it in the response
            with open(latest_file, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode('utf-8')

            image_result = {
                'detection': detection_results,
                'classification': classification_result,
                'captioning': captioning_results,
                'image': 'data:image/jpeg;base64,' + encoded_string
            }
            
            # Delete the runs folder
            file_delete.delete_directory('runs')

            return jsonify(image_result)
    else:
        return jsonify(error='Invalid content type'), 400
    



