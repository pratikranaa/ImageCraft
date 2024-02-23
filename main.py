import os
import base64
from io import BytesIO
from PIL import Image
import numpy as np
from app import captioning, detection, classification
from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
    
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def decode_base64_image(image_data):
    image_data = image_data.split(',')[1]
    img_bytes = BytesIO(base64.b64decode(image_data))
    img = Image.open(img_bytes)
    temp_image_path = os.path.join(UPLOAD_FOLDER, 'temp_image.jpg')
    img.save(temp_image_path)
    return temp_image_path

@app.route("/")
def index():
    return send_file('web/index.html')


@app.route('/process_images', methods=['POST'])
def process_images():
    data = request.json.get('Images')
    results = []
    for image_data in data:
        image_path = decode_base64_image(image_data)
        detection_results = detection.perform_detection(image_path)
        classification_result = classification.perform_classification(image_path)
        captioning_results = captioning.generate_image_caption(image_path)

        image_result = {
            'detection': detection_results,
            'classification': classification_result,
            'captioning': captioning_results
        }
        results.append(image_result)
        # os.remove(image_path)
    return jsonify(results)


if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 8000)))
