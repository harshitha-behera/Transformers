from transformers import ViTFeatureExtractor, ViTForImageClassification
import torch
from PIL import Image
import requests
import streamlit as st

# Specify the model name
model_name = 'google/vit-large-patch16-384' #"google/vit-base-patch16-224"

# Load the feature extractor and model
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

print("ViT model and feature extractor loaded successfully!")

# Sample image URL (you can change to any image URL)
image_url = "https://images.pexels.com/photos/163398/football-american-football-canadian-university-canadian-football-163398.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
response = requests.get(image_url, stream=True)
img = Image.open(response.raw).convert("RGB")
img

# Preprocess and predict
inputs = feature_extractor(images=img, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()

# The model config contains label information
labels = model.config.id2label
predicted_label = labels[predicted_class_idx]

st.write(f"Image description: {predicted_label}")

st.title("Vision Transformer (ViT) Image Classification")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess the image
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
    
    labels = model.config.id2label
    predicted_label = labels[predicted_class_idx]
    st.write(f"Prediction: {predicted_label}")