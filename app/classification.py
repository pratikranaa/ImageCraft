import torch
from torchvision.models import mobilenet_v3_large
import torchvision.transforms as transforms
from PIL import Image

model = mobilenet_v3_large(weights='IMAGENET1K_V2', pretrained=True)
model.eval()

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),  
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)  
    return input_batch

def perform_classification(image_path):
    input_batch = preprocess_image(image_path)
    with torch.no_grad():
        output = model(input_batch)
    _, predicted_idx = torch.max(output, 1)
    predicted_label = predicted_idx.item()
    return predicted_label
