#A simple program to reshape images for neural style transfer and other tasks
from PIL import Image
import os

def reshape_images(directory = "images"):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            path = os.path.join(directory, filename)
            images = Image.open(path)
            images = images.resize((512, 512))
            images.save(path)