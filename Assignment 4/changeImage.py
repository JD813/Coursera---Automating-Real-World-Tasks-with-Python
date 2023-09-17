#!/usr/bin/env python3

from PIL import Image as Image
import os

images_location = "./supplier-data/images/"
save_location = "./supplier-data/images/"

def process_image(fileName):
  print (images_location + f"{fileName}")
  to_proc = Image.open(images_location + f"{fileName}")
  to_proc = to_proc.convert("RGB")
  to_proc = to_proc.resize((600,400))
  print (save_location + fileName[0:-4] + "jpeg")
  to_proc.save(save_location + fileName[0:-4] + "jpeg")

if __name__ == "__main__":
  file_list = os.listdir(images_location)
  for file in file_list:
    if file.endswith(r".tiff"):
      process_image(file)
