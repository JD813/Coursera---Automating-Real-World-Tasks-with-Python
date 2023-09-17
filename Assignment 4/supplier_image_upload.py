#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

images_location = "./supplier-data/images/"

file_list = os.listdir(images_location)
print (file_list)
for file in file_list:
  if file.endswith(".jpeg"):
    with open(images_location + file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})