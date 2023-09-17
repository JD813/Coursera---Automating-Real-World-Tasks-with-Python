#!/usr/bin/env python3
import os
import requests

fileList = os.listdir("/data/feedback/")
for file in fileList:
    with open (os.path.join("/data/feedback", file), "r") as f:
        iLines = f.readlines()
    temp = {}
    temp ["title"]      = iLines[0]
    temp ["name"]       = iLines[1]
    temp ["date"]       = iLines[2]
    temp ["feedback"]   = iLines[3]

    response = requests.post("http://34.132.248.226/feedback/", data = temp)
