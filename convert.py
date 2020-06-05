# Goal is to convert jpg images from a given folder to png and save them in a spearate folder
# accept 2 images folder and new folder name at console

import sys
import os
from PIL import Image, ImageFilter

input_folder = sys.argv[1]
output_folder = sys.argv[2]

print(input_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for item in os.listdir(input_folder):
    img = Image.open(os.path.join(input_folder, item))
    file, ext = os.path.splitext(item)
    img.save(f'{output_folder}/{file}.png', 'png')

    img.thumbnail((100, 100))
    img.save(f'{output_folder}/{file}_thumbnail.png', 'png')
