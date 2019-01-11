#from scipy.ndimage import gaussian_filter1d
import numpy as np
import matplotlib.pyplot as plt
import cv2



def Get_Five_Max(contours):
    max = 0
    index = 0
    for i in range(len(contours)):
        if len(contours[i]) > 30:
            (x, y), (MA, ma), angle = cv2.fitEllipse(contours[i])
            if angle > max:
                max = angle
                bb = contours[i]
                index = i
    return bb, index



img = cv2.imread('2/101_2.tif')
img = cv2.GaussianBlur(img, (3, 3), 0)
#canny = cv2.Canny(img, 50, 150)
#ret, binary = cv2.threshold(canny, 127, 255, cv2.THRESH_BINARY)
#image, contours, hi = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

sobelx1 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

abssobelx = cv2.convertScaleAbs(sobelx)
abssobelx1 = cv2.convertScaleAbs(sobelx1)

#dst = cv2.addWeighted(abssobelx, 0.5, abssobelx1, 0.5, 0)
#canny_dst = cv2.Canny(dst, 50, 150)
#ret1, binary1 = cv2.threshold(canny_dst, 127, 255, cv2.THRESH_BINARY)
#image1, contours1, hi1 = cv2.findContours(binary1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours1, -1, (0, 0, 255), 1)
A = sobelx.copy()
B = sobelx1 + A
gh = cv2.Sobel(B, cv2.CV_16S, 1, 1, ksize=3)
gh_blur = cv2.GaussianBlur(gh, (15, 15), 0)
gh_blur = cv2.convertScaleAbs(gh_blur,gh_blur)
gh_media = cv2.medianBlur(gh_blur, 5)
gh_media = cv2.medianBlur(gh_media, 15)
gh_media = cv2.medianBlur(gh_media, 7)

ret1, binary1 = cv2.threshold(gh_media, 50, 255, cv2.THRESH_BINARY)
#print gh_media[150][209]
#gh = cv2.Sobel(gh_blur, cv2.CV_16S, 1, 1, ksize=3)
#abs_gh_blur = np.absolute(gh_blur)
rows, cols = gh_blur.shape[:2]

#op = cv2.convertScaleAbs(gh_blur)
max = 0.0
for i in range(rows):
    for j in range(cols):
        if binary1[i][j][0] > 0:
            max = gh_blur[i][j][0]
            #print gh_media[i][j]
            row = i
            col = j

#print gh_media[373][387]
#gh_blur = cv2.convertScaleAbs(gh_blur,gh_blur)
#print rows, cols
print "------"
print row, col
print "------"

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(binary1, cmap='gray')
plt.subplot(1, 3, 2)
plt.imshow(img)
plt.subplot(1, 3, 3)
plt.imshow(gh_media, cmap='gray')
plt.show()
