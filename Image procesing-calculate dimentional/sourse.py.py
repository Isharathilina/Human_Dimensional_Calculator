# USAGE
# python extreme_points.py

# import the necessary packages
import imutils
import cv2

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread("ee.jpg")
#image = cv2.IMREAD_GRAYSCALE("qq.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
c = max(cnts, key=cv2.contourArea)

# determine the most extreme points along the contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])




# draw the outline of the object, then draw each of the
# extreme points, where the left-most is red, right-most
# is green, top-most is blue, and bottom-most is teal
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
#cv2.circle(image, extLeft, 6, (0, 0, 255), -1)
#cv2.circle(image, extRight, 6, (0, 255, 0), -1)
cv2.circle(image, extTop, 6, (255, 0, 0), -1)
cv2.circle(image, extBot, 6, (255, 255, 0), -1)






#----------------------------------------------


length=len(c)  
to = int(length/2)
div = int(length/10)

print("points are ")

i = 0
r = 0
count = 0

while (i<to):
	
	i = i + div
	mtl = c[i]
	ext1 = max(mtl)

	cv2.circle(image, (ext1[0],ext1[1]), 6, (255, 0, 200), -1)



	r = length - i
	mt2 = c[r]
	ext2 = max(mt2)

	cv2.circle(image, (ext2[0],ext2[1]), 6, (255, 0, 200), -1)


	print(ext1)
	print(ext2)
	count = count+1

	if count==2:        # getting chest points
		cp1 = ext1[0]
		cp2 = ext2[0]
		print("(chest poitnt mesh)")







heigh = 150     # actual height cm
point1 = min(extTop)
point2 = max(extBot)
catcode = 0

print("Y points :- ",point1,"and",point2)
defar = point2 - point1
print("defance :- ",defar)

scale = heigh/defar            # heigh def factor for pixcel
print("scale :- ",scale)



print("chest X poitnt",cp1,"and",cp2)


cdist = cp2 - cp1
print( "image chest length ",cdist,"pixcel")
chest = int(cdist*scale)     
print("calculated half chest length:- ",chest,"cm")

#------------------------start categorizing---------------------

if heigh>150:
	# A

	if chest>57:

		print("Aa ")
		catcode = 1
	elif chest<37:
	
		print("Ac")
		catcode = 3
	else:
		print("Ab")
		catcode = 2




elif heigh<130:
	# C

	if chest>57:
	
		print("Ca ")
		catcode = 7

	elif chest<37:
	
		print("Cc")
		catcode = 9
	else:
		print("Cb")
		catcode = 8



else:
	# B

	if chest>57:
	
		print("Ba ")
		catcode = 4

	elif chest<37:
	
		print("Bc")
		catcode = 6

	else:
		print("Bb")
		catcode = 5




print("category code :- ",catcode)


# show the output image
cv2.imshow("Image", image)


cv2.waitKey(0)