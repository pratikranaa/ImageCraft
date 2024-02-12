from transformers import pipeline

def generate_image_caption(image_url):
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    caption_results = image_to_text(image_url)
    return caption_results[0]['generated_text']