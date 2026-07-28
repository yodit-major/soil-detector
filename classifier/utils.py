import cv2
import numpy as np


def analyze_soil(image_path):

    img = cv2.imread(image_path)

    img = cv2.resize(img, (300, 300))

    avg = img.mean(axis=0).mean(axis=0)

    b, g, r = avg

    if r > 120 and g > 100:
        result = "🌾 DRY Soil"
    else:
        result = "🌿 HEALTHY or WET Soil"

    return {
        "result": result,
        "red": int(r),
        "green": int(g),
        "blue": int(b)
    }