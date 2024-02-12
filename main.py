import os
import torch
from app import captioning
from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def save_uploaded_image(file):
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    return filepath

@app.route("/")
def index():
    return send_file('web/index.html')

@app.route('/process_images', methods=['POST'])
def process_images():
    data = request.files.getlist('images')
    image_paths = []
    for file in data:
        filepath = save_uploaded_image(file)
        image_paths.append(filepath)

    results = []
    for image_path in image_paths:
        # detection_results = detection.perform_detection(image_path)
        # classification_results = classification.perform_classification(image_path)
        captioning_results = captioning.generate_image_caption(image_path)

        image_result = {
            'image': image_path,
            # 'detection': detection_results,
            # 'classification': classification_results,
            'captioning': captioning_results
        }
        results.append(image_result)

        # Delete the uploaded image after processing
        # os.remove(image_path)

    return jsonify(results)


if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 8000)))
