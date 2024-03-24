# ImageCraft

React + Flask Based AI Image processing app. The application utilises various image processing techniques such as object detection, image

classification, and image captioning. We have used Mobilenetv3 for image classification because it is

efficient and lightweight and good for scalability and low latency

## I. Setup:

### 1. Before using the Flask application, ensure you have the following installed:

● Python (3.x recommended)
● Flask
● PIL (Python Imaging Library)
● NumPy

### 2. Clone the repository containing the Flask application:

```
git clone https://github.com/pratikranaa/AI-pipeline-image
```

### 3. Navigate to the project directory:

```
cd AI-pipeline-image
```

### 4. Install the required dependencies:

```
pip install -r requirements.txt
```

## II. Usage

### 1. Run the Flask Application:

   To start the Flask application, execute the following command in your terminal:

```
   python main.py
```

   The application will start running on the default port (8000).

### 2. Access the Web Interface:

   Open a web browser and navigate to http://127.0.0.1:8000/ to access the web interface.

### 3. Upload Images for Processing:

   On the web interface, you can upload one or multiple images for processing. The uploaded images will
   undergo object detection, image classification, and image captioning.

### 4. Processing Images:

   Once images are uploaded, the application will process them using the following steps:

- Object Detection: Detects objects present in the image.
- Image Classification: Classifies the image into predefined categories.
- Image Captioning: Generates a descriptive caption for the image.

### 5. View Results:

   After processing, the application will return the results to the console in JSON format, including detected
   objects, image categories, and generated captions. The image will also be saved in a directory runs/detect/

## III. API Usage

   Alternatively, you can interact with the application programmatically using the provided API endpoints.

### Endpoint:

```
   POST /process_images
```

### Request Body:

   Send a POST request to /process_images endpoint with a JSON object containing base64-encoded
   images.

### Example:

```
   {
   "Images": [
   "base64_encoded_image_1",
   "base64_encoded_image_2",
   ...
   ]
   }
```

### Response:

   The endpoint will return a JSON object containing the processed results for each image.
   Example Response:

```
   [
   {
   "detection": {
   "objects": ["object_1", "object_2", ...]
   },
   "classification": "image_category",
   "captioning": "image_caption"
   },
   {
   "detection": {
   "objects": ["object_1", "object_2", ...]
   },
   "classification": "image_category",
   "captioning": "image_caption"
   },
   ...
   ]
```

## IV. Conclusion

   Whether through the web interface or API endpoints, you can easily process images and obtain object
   detection, image classification, and image captioning results.
