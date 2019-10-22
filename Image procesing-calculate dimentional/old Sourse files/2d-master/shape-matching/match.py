# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True,
# 	help = "Path to the image")
# ap.add_argument("-t", "--template", required = True,
# 	help = "Path to the template image")
# args = vars(ap.parse_args())


# load the image and template images

#image = cv2.imread(args["image"])
#template = cv2.imread(args["template"])

image = cv2.imread("1.jpg")
template = cv2.imread("t.jpg")


(templateHeight, templateWidth) = template.shape[:2]

# find the template in the image
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)

# grab the bounding box of template and extract it from the image
topLeft = maxLoc
botRight = (topLeft[0] + templateWidth, topLeft[1] + templateHeight)
roi = image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]

# construct a darkened transparent 'layer' to darken everything
# in the image except for template
mask = np.zeros(image.shape, dtype = "uint8")
image = cv2.addWeighted(image, 0.25, mask, 0.75, 0)

# put the original template back in the image so that he is
# 'brighter' than the rest of the image
image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi

# display the images
cv2.imshow("Image", imutils.resize(image, height = 650))
cv2.imshow("Template", template)
cv2.waitKey(0)