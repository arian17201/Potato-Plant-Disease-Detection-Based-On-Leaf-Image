import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from PIL import Image

app = Flask(__name__)

# Load the trained model
MODEL_PATH = 'model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

# Class names corresponding to your trained model
CLASS_NAMES = ['Potato_early_blight', 'Potato_healthy', 'Potato_late_blight']
IMAGE_SIZE = (255, 255)

def preprocess_image(image: Image.Image) -> np.ndarray:
    """Resize image to 255x255 and normalize pixel values (1./255)"""
    image = image.convert('RGB')
    image = image.resize(IMAGE_SIZE)
    img_array = np.array(image, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        image = Image.open(file.stream)
        processed_img = preprocess_image(image)
        
        # Perform model prediction
        predictions = model.predict(processed_img)[0]
        
        # Identify predicted class and confidence
        predicted_idx = int(np.argmax(predictions))
        predicted_class = CLASS_NAMES[predicted_idx]
        confidence = float(predictions[predicted_idx]) * 100
        
        # Detailed probability mapping for all classes
        class_probabilities = {
            CLASS_NAMES[i].replace('_', ' '): float(predictions[i]) * 100 
            for i in range(len(CLASS_NAMES))
        }

        return jsonify({
            'success': True,
            'prediction': predicted_class.replace('_', ' '),
            'confidence': round(confidence, 2),
            'probabilities': class_probabilities,
            'model_accuracy': 97.67  # Overall validation accuracy from your training
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)