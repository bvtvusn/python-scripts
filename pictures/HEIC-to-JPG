import os
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

folder_path = r"C:\Users\source" # Change this path to the folder with your heic files
output_folder = r"C:\Users\destination"

for filename in os.listdir(folder_path):
    if filename.lower().endswith((".heic", ".heif")):
        file_path = os.path.join(folder_path, filename)
        im = Image.open(file_path)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        im.convert('RGB').save(output_path, quality=90)
