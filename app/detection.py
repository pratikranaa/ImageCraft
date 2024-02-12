import torch


def perform_detection(image_url):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    results = model(image_url)
    detection_results = results.pandas().xyxy[0].to_dict('records')
    return detection_results
