import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.src.applications.resnet import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
# from keras_vggface.utils import preprocess_input
import cv2
import os
import requests
from io import BytesIO
from PIL import Image

# Get the directory containing Haar cascade files
cascade_dir = cv2.data.haarcascades

# Path to the Haar cascade file for frontal face detection
cascade_file = os.path.join(cascade_dir, 'haarcascade_frontalface_default.xml')

# Check if the cascade file exists
if os.path.isfile(cascade_file):
    print("Haar cascade file found:", cascade_file)
else:
    print("Haar cascade file not found. Downloading...")
    cv2_base_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/"
    cascade_url = cv2_base_url + 'haarcascade_frontalface_default.xml'
    os.system(f"wget {cascade_url} -P {cascade_dir}")
    print("Haar cascade file downloaded successfully.")

# Now, you can use cascade_file as the filter_path in your code.
filter_path = cascade_file


def load_and_preprocess_image(img_array, target_size):
    """Preprocesses a single image for model prediction."""
    img = cv2.resize(img_array, target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess image
    return img_array


def detect_and_crop_faces(img_array, filter_path):
    """Detects faces in the image and returns the cropped faces."""
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier(filter_path)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cropped_faces = [(img_array[y:y + h, x:x + w], (x, y, w, h)) for (x, y, w, h) in faces]
    return cropped_faces, img_array


def predict_and_display(model, class_names, img_url, target_size, filter_path):
    """Predicts the label of faces detected in the given image URL and displays the image with predicted labels."""
    # Download the image from the URL
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content)).convert('RGB')
    img_array = np.array(img)

    # Detect and crop faces
    cropped_faces, original_img = detect_and_crop_faces(img_array, filter_path)

    if not cropped_faces:
        print("No faces detected.")
        return

    plt.figure(figsize=(10, 10))

    for face, (x, y, w, h) in cropped_faces:
        # Preprocess the cropped face
        img_array = load_and_preprocess_image(face, target_size)

        # Make prediction
        predictions = model.predict(img_array)
        pred_idx = np.argmax(predictions[0])
        predicted_label = class_names[pred_idx]

        # Draw bounding box and label on the original image
        cv2.rectangle(original_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(original_img, predicted_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Display the image with bounding boxes and labels
    plt.imshow(original_img)
    plt.axis("off")
    plt.show()


# Load your model without compiling
reloaded_model = load_model("my_29_30_model_97.h5", compile=False)

# Compile the model with a new optimizer
reloaded_model.compile(optimizer=tf.keras.optimizers.Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Define the class names for your dataset
class_names = ['Akshay Kumar', 'Alexandra Daddario', 'Alia Bhatt', 'Amitabh Bachchan',
               'Andy Samberg', 'Anushka Sharma', 'Billie Eilish', 'Brad Pitt', 'Camila Cabello',
               'Charlize Theron', 'Claire Holt', 'Courtney Cox', 'Dwayne Johnson', 'Elizabeth Olsen',
               'Ellen Degeneres', 'Henry Cavill', 'Hrithik Roshan', 'Hugh Jackman', 'Jessica Alba',
               'Lisa Kudrow', 'Margot Robbie', 'Natalie Portman', 'Priyanka Chopra', 'Robert Downey Jr',
               'Roger Federer', 'Tom Cruise', 'Vijay Deverakonda', 'Virat Kohli', 'Zac Efron']

# List of image URLs
img_urls = ["https://upload.wikimedia.org/wikipedia/commons/e/ef/Virat_Kohli_during_the_India_vs_Aus_4th_Test_match_at_Narendra_Modi_Stadium_on_09_March_2023.jpg",
            "https://in.bmscdn.com/iedb/artist/images/website/poster/large/akshay-kumar-94-1681713982.jpg",
            "https://m.media-amazon.com/images/M/MV5BMTUxNzY3NzYwOV5BMl5BanBnXkFtZTgwNzQ3Mzc4MTI@._V1_.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Brad_Pitt_2019_by_Glenn_Francis.jpg/1200px-Brad_Pitt_2019_by_Glenn_Francis.jpg",
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf43hIcOv1v_GWMgz8dBqg_g5SUK52yAx58g&s',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_eg1B7FFdpLMGzNHXf_-QrkeomOjvflQWHQ&s',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQohXZspQ43hcdkLKTM5X1WF8EOyY9GJA2mCQ&s',
            'https://img.jagranjosh.com/imported/images/E/GK/Amitabh-Bachchan-list-of-awards.webp',
            'https://media.newyorker.com/photos/5909527c1c7a8e33fb38a864/master/pass/Man_of_Steel-580.jpeg',
            'https://www.giantfreakinrobot.com/wp-content/uploads/2021/03/robert-downey-iron-man-900x506.jpg',
            'https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/Elizabeth_Olsen_as_Wanda_Maximoff.jpg/220px-Elizabeth_Olsen_as_Wanda_Maximoff.jpg',
            'https://www.gqmiddleeast.com/2021/06/Tom-Cruise.jpg',
            'https://telugubullet.com/wp-content/uploads/2023/12/SS-022-jpg.webp',
            'https://static1.srcdn.com/wordpress/wp-content/uploads/2021/02/Wanda-maximoff-avengers-infinity-war-Tony-Stark-MCU.jpg',
            'https://img.theweek.in/content/dam/week/gallery/shots/2021/january-24-2021/people/72-anushka-virat.jpg',
            ]

for img_url in img_urls:
    # Predict and display the label of the image
    predict_and_display(reloaded_model, class_names, img_url, target_size=(224, 224), filter_path=filter_path)
