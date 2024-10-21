# COTTON CARE AI – Deep Learning Project

## Project Overview
Cotton Care AI is a web-based application designed to aid in the early detection and classification of cotton plant diseases. Leveraging deep learning and transfer learning with the InceptionV3 model, the application can categorize images of cotton plants into four distinct classes:
1. Diseased Cotton Leaf
2. Diseased Cotton Plant
3. Fresh Cotton Leaf
4. Fresh Cotton Plant

By using this tool, farmers and agricultural professionals can monitor the health of cotton crops in real-time, facilitating early disease detection and contributing to improved crop yield, sustainability, and reduced loss in agriculture.

## Key Features
- **Image Classification**: Upload an image of a cotton plant or leaf, and the model will classify it into one of four categories.
- **Flask-Based Web Application**: The project uses a Flask framework to provide an easy-to-use web interface.
- **Transfer Learning**: The InceptionV3 pre-trained model is used to achieve high accuracy in classifying cotton plant images.
- **User-Friendly Interface**: A simple interface where users can upload images and receive results quickly.
- **Agricultural Focus**: Built specifically for cotton farming, helping to prevent disease outbreaks and reduce financial losses.

## Use Case
The primary use case for Cotton Care AI is to assist farmers, agronomists, and agricultural workers in identifying diseases in cotton plants early. Traditional methods of disease identification can be slow and require expert knowledge. With Cotton Care AI, anyone can use a smartphone or camera to capture an image of a cotton plant or leaf, upload it to the application, and receive immediate feedback on the health status of the plant.

### Benefits:
- **Increased Crop Yield**: Early detection and treatment of diseased plants can improve overall crop health and yield.
- **Sustainability**: Helps minimize the need for blanket pesticide use, targeting only infected plants.
- **Ease of Use**: Designed for non-experts, no technical or agricultural expertise is required to use the tool.
- **Scalability**: Can be extended to detect diseases in other crops as well.

## How It Works
1. **Data Collection**: The model is trained on a dataset of cotton plant and leaf images that are labeled into the four categories mentioned above.
2. **Transfer Learning**: The InceptionV3 model, which has been pre-trained on the ImageNet dataset, is fine-tuned to classify the images in the cotton plant dataset.
3. **Model Integration**: The trained model is integrated into a Flask application, providing a web-based interface for users to interact with.
4. **Image Upload**: Users upload images of cotton leaves or plants, and the application processes these images and returns a classification result.
5. **Result Display**: The application displays the classification result on the webpage, allowing users to determine whether the plant is diseased or healthy.

## Technical Details
- **Framework**: Flask (Python)
- **Model**: InceptionV3 (Transfer Learning)
- **Languages**: Python, HTML, CSS, JavaScript
- **Frontend**: HTML/CSS, JavaScript for the user interface
- **Backend**: Flask for handling requests and image classification
- **Model Training**: Trained on a dataset of cotton plant images, categorized into four distinct classes
- **Deployment**: Can be hosted on local servers or cloud platforms

## Sample Testing Images

Here are a few examples of images used for testing the Cotton Care AI application:

### 1. Diseased Cotton Leaf
![Diseased Cotton Leaf](static/images/diseased_cotton_leaf.jpg)

### 2. Fresh Cotton Leaf
![Fresh Cotton Leaf](static/images/fresh_cotton_leaf.jpg)
