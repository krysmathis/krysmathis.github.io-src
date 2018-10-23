Title: Reading text from an image file
Date: 2018-10-20
Slug: python-ocr-simple

# Python Optical Character Recognition

One step toward realizing a complete project related to object detection in a retail setting is learning to distinguish text from an image. This type of has a variety of applications:

1. Reading shelf labels - quickly gather competitor prices with a flash
1. Reading nutritional information
1. Gathering size information vs shelf label unit of measure

This is but a small step toward any one of those applications. But an important first step in those directions.


## Sources
1. https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/

# Installing the Required Libraries
Installing tesseract    
```
brew install tesseract
```

In this project, I'm using tesseract inside a virtual environment
```
pip3 install pillow
pip3 install pytesseract
```

> adding some block quotes

## The code to read from the command line

```
from PIL import Image
import pytesseract
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
                help="path to input image to be ocr'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
args = vars(ap.parse_args())

image  = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif args['preprocess'] == 'blur':
    gray = cv2.medianBlur(gray, 3)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
# clean-up the temporary file
os.remove(filename)
print(text)

# cv2.imshow("Image", image)
cv2.imshow("Output", gray)
print('hit q to exit', but from the image itself)
cv2.waitKey(1048689) # q
```