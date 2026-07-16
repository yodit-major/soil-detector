from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import cv2
import numpy as np
import os


def home(request):
    context = {}

    if request.method == "POST" and request.FILES.get("image"):

        image = request.FILES["image"]

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)

        image_url = fs.url(filename)

        # Get image path
        image_path = fs.path(filename)

        # Read image
        img = cv2.imread(image_path)

        # Resize image
        img = cv2.resize(img, (300, 300))

        # Calculate average color
        avg = img.mean(axis=0).mean(axis=0)

        b, g, r = avg

        # Your current rule
        if r > 120 and g > 100:
            result = "🌾 DRY Soil"
        else:
            result = "🌿 HEALTHY or WET Soil"

        context["image_url"] = image_url
        context["result"] = result

    return render(request, "home.html", context)
