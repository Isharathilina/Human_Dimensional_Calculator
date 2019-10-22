# USAGE
# python silhouette2.py -i ../images/image.jpg

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

# load the puzzle and waldo images
image = cv2.imread(args["image"])

# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image
r = 600.0 / image.shape[1]
dim = (600, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# Load the image, convert it to grayscale, and blur it slightly
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.bilateralFilter(image, 9, 41, 41)
# blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

canny = cv2.Canny(image, 40, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)