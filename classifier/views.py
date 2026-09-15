from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import tensorflow as tf
import numpy as np

from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the model once when Django starts
model = tf.keras.models.load_model("ml_models/best_peat_augmented_model.keras")

# Class labels (same order as train_generator.class_indices)
class_names = [
    "Black Soil",
    "Cinder Soil",
    "Laterite Soil",
    "Peat Soil",
    "Yellow Soil"
]


def home(request):
    context = {}

    if request.method == "POST" and request.FILES.get("image"):

        image = request.FILES["image"]

        fs = FileSystemStorage()

        filename = fs.save(image.name, image)

        image_url = fs.url(filename)

        image_path = fs.path(filename)

        # Load image
        img = load_img(image_path, target_size=(224, 224))

        # Convert image to NumPy array
        img_array = img_to_array(img)

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        # Normalize
        img_array = img_array / 255.0

        # Predict
        prediction = model.predict(img_array)

        class_index = np.argmax(prediction)

        confidence = float(np.max(prediction) * 100)

        result = class_names[class_index]

        context = {
            "image": image_url,
            "result": result,
            "confidence": round(confidence, 2),
        }

    return render(request, "home.html", context)