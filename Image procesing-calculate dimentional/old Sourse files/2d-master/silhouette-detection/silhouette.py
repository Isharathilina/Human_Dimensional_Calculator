import numpy as np
import cv2
    
def main():
    bg = cv2.imread('../images/background.jpg', 1)
    side = cv2.imread('../images/side1.jpg', 1)

    edged_bg = find_edges(bg)
    edged_side = find_edges(side)

    # Get the different between background image an front view image
    diff = cv2.subtract(edged_side, edged_bg)

    # Floodfill the image by border
    floodfilled = floodfill(diff) 

    #img = cv2.imread('j.png',0)
    #kernel = np.ones((5,5),np.uint8)
    #erosion = cv2.erode(img,kernel,iterations = 1)

    # View the result
    while(1):
        cv2.imshow('image', floodfilled)
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
            break

def find_edges(img):
    # Change all images to HSV to remove the shadow
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # Remove shadow from front image by setting v channel to fixed value
    hsv_img[:,:,2] = 200

    # Change all images back to bgr image
    img = cv2.cvtColor(hsv_img,cv2.COLOR_HSV2BGR)

    # Convert different image to gray
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # normalize 
    cv2.normalize(img, img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Binary different image
    # Increase second params to reduce big salt and peppersize noise
    median = cv2.medianBlur(img, 5)

    # Remove small object
    blur = cv2.GaussianBlur(median,(5,5),0) 

    # Apply the canny filter to the different
    edged_img = cv2.Canny(blur,0,40)

    # Dilate to close the gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
    dilation = cv2.dilate(edged_img,kernel,iterations = 1)

    return dilation

def floodfill(img):
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    seed_pt = None

    cv2.floodFill(img, mask, seed_pt, (0, 0, 0), (0,)*3, (255,)*3, 4 + (255 << 8) + cv2.FLOODFILL_MASK_ONLY)
    img = img[1:h,1:w]

    return img

if __name__ == "__main__":
    main()
