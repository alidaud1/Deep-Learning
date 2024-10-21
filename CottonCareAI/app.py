from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64

# Initialize Flask app
app = Flask(__name__)

# Load model architecture from JSON
with open("CottonDiseaseDetection.json", "r") as json_file:
    loaded_model_json = json_file.read()

# Create model from loaded JSON
loaded_model = tf.keras.models.model_from_json(loaded_model_json)

# Load model weights
loaded_model.load_weights("CottonDiseaseDetection.h5")

# Define classes
classes = ['Diseased Cotton Leaf', 'Diseased Cotton Plant', 'Fresh Cotton Leaf', 'Fresh Cotton Plant']

# Function to preprocess the image
def preprocess_image(image):
    img = Image.open(io.BytesIO(image))
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0  # Normalize pixel values
    return img_array.reshape(-1, 224, 224, 3)

# Define route for the index page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded image file
        file = request.files["file"]
        
        # Check if the file is present and is an image
        if file and file.filename.endswith(('.png', '.jpg', '.jpeg')):
            # Read the image file
            image = file.read()
            
            # Preprocess the image
            processed_image = preprocess_image(image)
            
            # Make prediction
            prediction = loaded_model.predict(processed_image)
            
            # Get class label
            class_label = classes[np.argmax(prediction)]
            
            # Convert the image to base64 encoding
            encoded_image = base64.b64encode(image).decode('utf-8')
            
            return render_template("index.html", prediction=class_label, uploaded_image=encoded_image)
        else:
            return "Please upload a valid image file."
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
