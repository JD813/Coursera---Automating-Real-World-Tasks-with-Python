from PIL import Image as im
import os

oDirectory = "/opt/icons/"

def processImage(image, outDirectory):
    with im.open("./images/" + image) as img:
        img = img.convert("RGB")
        img = img.rotate(-90)
        img = img.resize((128,128))
        output = img
        output.save(os.path.join(outDirectory,image),"JPEG")

if __name__ == "__main__":
    fileList = os.listdir("./images/")
    if not (os.path.isdir(oDirectory)):
        os.makedirs(oDirectory)
    for file in fileList:
        if not(file.startswith(".")):
            processImage(file, oDirectory)