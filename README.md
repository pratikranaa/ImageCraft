# ImageCraft

This is a web application that allows users to upload images and perform various operations on them, such as object detection, image classification, image captioning, and annotated images. The application is built using Flask for the backend, React for the frontend, and Vite as the build tool. It also utilizes TailwindCSS for styling and is containerized using Docker for easy deployment.

![Demo](https://raw.githubusercontent.com/pratikranaa/ImageCraft/master/demo%20(3).gif)

## Table of Contents

1. [Introduction](#1-introduction)
2. [Features](#2-features)
3. [Setup and Installation](#3-setup-and-installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [Running the Application](#4-running-the-application)
5. [Folder Structure](#5-folder-structure)
6. [Configuration](#6-configuration)
7. [Usage](#7-usage)
8. [Contributing](#8-contributing)
9. [Conclusion](#9-conclusion)
10. [Creator](#10-creator)
11. [Demo Video](#11-demo-video)


## 1. Introduction

React + Flask Based AI Image processing app. The application utilises various image processing techniques such as object detection, image classification, and image captioning. We have used Mobilenetv3 for image classification because it is efficient and lightweight and good for scalability and low latency. It consists of a React frontend that interacts with a Flask backend to handle image processing tasks. The frontend communicates with the backend via HTTP requests.

## 2. Features

- **Object Detection**: The application can detect objects present in an uploaded image and provide bounding boxes around them.
- **Image Classification**: The application can classify the uploaded image into different categories.
- **Image Captioning**: The application can generate a textual description (caption) for the uploaded image.
- **Docker Containerization**: The application is containerized using Docker, making it easy to deploy and run in different environments.

## 3. Setup and Installation

### Prerequisites

#### Before using the application, ensure you have the following installed:

- Node.js
- npm (Node Package Manager)
- Python 3.x
- Docker (optional, for containerization)

### Installation Steps

#### 1. Clone the repository:

   ```bash
   git clone https://github.com/pratikranaa/ImageCraft.git
   ```
#### 2. Navigate to the project frontend directory:

   ```bash
   cd ai-frontend
   ```

#### 3. Install frontend dependencies:

   ```bash
   npm install
   ```

#### 4. Install backend dependencies (recommended to set up a virtual environment first):

   ```bash
   cd ..
   python -m venv env
   source env/bin/activate  # For Unix/Mac
   env\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

## 4. Running the Application

### Development Mode

To run the application in development mode, you need to start both the frontend and backend servers.

#### 1. Start the frontend development server:

   ```bash
   cd ai-frontend #if not in frontend directory
   npm run dev
   ```
   
   The frontend development server will start running on the default port (5173).

   Open a web browser and navigate to http://localhost:5173/ to view the application.

#### 2. Start the Flask backend server:

   ```bash
   python3 main.py # go in directory containing main.py 
   ```
   
   The application will start running on the default port (5000).

### Production Build 

To build the application for production, follow these steps:

#### 1. Build the frontend:

   ```bash
   cd ai-frontend
   npm run build
   ```

#### 2. Copy the frontend build to flask directory

   ```bash
   cd ..           #go back to main directory
   cp -r ai-frontend/dist .
   ```
#### 3. Run the Backend

   ```bash
   python3 main.py
   ```
   The application will start running on the default port and open the link displayed in browser.

### Production Build with Docker

To run the application in production mode using Docker, follow these steps:

1. Build the Docker image:

```bash
docker-compose build
```

2. Run the Docker containers:

```bash
docker-compose up
```
The application will be available at `http://localhost:5000` or the link displayed after deployment.

## 5. Folder Structure

```
Imagecraft/
├── ai-frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   ├── index.jsx
│   │   ├── ...
│   ├── package.json
│   ├── vite.config.js
│   ├── ...
├── app/
│   ├── __init__.py
│   ├── captioning.py
│   ├── classification.py
│   ├── detection.py
│   ├── file_delete.py
│   ├── ...
├── main.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
├── dist        # after npm run build and copying frontend build files
│   ├── index.html
│   ├── main.js
│   ├── ...
├── ...
```

- `ai-frontend/`: Contains the React application source code.
- `app/`: Contains the Flask application source code.
- `main.py`: The main Flask application file.
- `docker-compose.yml`: Docker Compose configuration file.
- `Dockerfile`: Dockerfile for building the Docker image.
- `requirements.txt`: Python dependencies.
- `.env`: Environment variables (if any).
- `dist`: Contains the built frontend files. need to copy from ai-frontend after npm run build

## 6. Configuration

- **Backend Configuration:** No additional configuration is required for the backend. However, you can modify the Flask application logic in `main.py` as needed.

- **Frontend Configuration:** Update the `proxy` field in `AI-frontend/package.json` if the backend server is running on a different port.

## 7. Usage

### 1. Upload Images for Processing:

   On the web interface, you can upload image for processing. The uploaded images will
   undergo object detection, image classification, and image captioning.

### 2. Processing Images:

   Once images are uploaded, the application will process them using the following steps:

- Object Detection: Detects objects present in the image.
- Image Classification: Classifies the image into predefined categories.
- Image Captioning: Generates a descriptive caption for the image.
- The processed images with annotations will be displayed on the web interface.

### 3. View Results:

   After processing, the application will return the results to the output table, including detected
   objects, image categories, and generated captions.

   #### API Usage
      
   Alternatively, you can interact with the application programmatically using the provided API endpoints.


#### Endpoint:

```
   POST /api/process_images
```

#### Request Body:

   Send a POST request to /process_images endpoint with a JSON object containing base64-encoded
   images.

#### Example:

```
   {
   "Images": [
   "base64_encoded_image_1",
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
   "captioning": "image_caption",
   "image": "base64_encoded_image_1"
   },
   {
   "detection": {
   "objects": ["object_1", "object_2", ...]
   },
   "classification": "image_category",
   "captioning": "image_caption",
   "image": "base64_encoded_image_2"
   },
   ...
   ]
```

## 8. Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/fooBar`).
3. Make changes and commit them (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new pull request.


## 9. Conclusion

   Whether through the web interface or API endpoints, you can easily process images and obtain object
   detection, image classification, and image captioning results.

## 10. Creator

This project was created by:
   - [Pratik Rana](https://github.com/pratikranaa)

## 11. Demo Video

You can see a demo of the application in the following video:

[Imagecraft Demo Video](https://github.com/pratikranaa/ImageCraft/blob/master/demo.mp4)

