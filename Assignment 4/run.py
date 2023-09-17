#! /usr/bin/env python3

import os
import requests
import re
import json

text_file_location = "./supplier-data/descriptions/"
url = "http://34.145.82.174/fruits/"

def toJson(fileName):
  with open(text_file_location + fileName, "r") as f:
    iLines = f.readlines()
    name = (re.match("([a-z]*)", iLines[0], flags = re.IGNORECASE))[1]
    num = int(re.match("(\d+) ", iLines[1])[1])
    description = iLines[2]
  output = { "name" : name,
             "weight" : num,
             "description" : description,
             "image_name" : fileName[0:-3] + "jpeg"
  }
  ouput = json.dumps(output, indent = 4)
  return output


if __name__ == "__main__":
  file_list = os.listdir(text_file_location)
  jsonList = []
  for file in file_list:
    if file.endswith(r".txt"):
      jsonList.append(toJson(file))
  for json in jsonList:
    r = requests.post(url, data = json)