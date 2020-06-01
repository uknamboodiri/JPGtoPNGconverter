"""Program to convert all JPG files from a given folder & save them to a output folder as PNG

Usage:
JPGtoPNGconverter <input_folder> <output_folder>

Example:
      python JPGtoPNGconverter.py ./images ./png_images
"""
import sys
import os
from PIL import Image

# take input and out folder location as input
input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for item in os.listdir(input_folder):
    img = Image.open(f"{input_folder}/{item}")
    file_name = os.path.splitext(item)[0]

    img_thumbnail = Image.open(f"{input_folder}/{item}")
    img_thumbnail.thumbnail((100, 100))

    img.save(f"{output_folder}/{file_name}.png", "png")
    img_thumbnail.save(f"{output_folder}/{file_name}_thumbail.png", "png")
