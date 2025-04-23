import os
import tensorflow as tf
# Force TensorFlow to use CPU only
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
tf.config.set_visible_devices([], 'GPU')

import cv2
import numpy as np
import json
from tensorflow.keras.models import model_from_json
from tensorflow.keras.applications.efficientnet import preprocess_input

# Global variable to cache the model after first load
_model = None

def get_model():
    """
    Load and cache the model from components - only loads once
    """
    global _model
    if _model is not None:
        return _model
    
    model_dir = "/home/jet/Downloads/mars/best_efficientnetb0_garbage.keras"
    config_path = os.path.join(model_dir, "config.json")
    weights_path = os.path.join(model_dir, "model.weights.h5")
    
    # Check that files exist
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Model config not found at {config_path}")
    if not os.path.exists(weights_path):
        raise FileNotFoundError(f"Model weights not found at {weights_path}")
    
    # Load model architecture from config.json
    print(f"Loading model architecture from {config_path}")
    with open(config_path, 'r') as f:
        model_config = json.load(f)
    
    # Create model from JSON config
    _model = model_from_json(json.dumps(model_config))
    
    # Load weights
    print(f"Loading weights from {weights_path}")
    _model.load_weights(weights_path)
    print("Model loaded successfully!")
    
    return _model

def classify_image(image_path):
    """
    Classify an image and return the class name
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Classification result ('metal', 'paper', or 'plastic')
    """
    # Class names for the model
    class_names = ["metal", "paper", "plastic"]
    
    # Load model (uses cached model if already loaded)
    model = get_model()
    
    # Load and preprocess image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image from {image_path}")
    
    # Resize to 224x224 for MobileNetV2
    image = cv2.resize(image, (224, 224))
    
    # Preprocess image
    image_array = np.expand_dims(image, axis=0)
    image_array = preprocess_input(image_array)
    
    # Make prediction
    pred_probs = model.predict(image_array)
    pred_index = np.argmax(pred_probs, axis=1)[0]
    pred_class = class_names[pred_index]
    confidence = pred_probs[0][pred_index]
    
    print(f"Classification: {pred_class} with {confidence:.2f} confidence")
    return pred_class

# For testing the function directly
if __name__ == "__main__":
    image_path = "/home/jet/Downloads/mars/captured_image.jpg"
    result = classify_image(image_path)
    print(f"Result: {result}")