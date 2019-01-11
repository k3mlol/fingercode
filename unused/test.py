# _*_ encoding: utf-8 _*_

import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
from Gabor import *
from fingercode import *

"""
if (4 > 2)&(7 > 4):
    print "ok"
else:
    print "NO"

a = -1.0
b = 1
print math.degrees(math.atan(-1.0 / 1.0)) + 180.0
print math.degrees(math.atan(1.0/1.0))
print math.degrees(math.atan(1.0/-1.0)) + 360.0
print math.degrees(math.atan(-1.0/-1.0)) + 180.0

img = cv2.imread('1/101_7.tif', 0)

print type(img[10][10])

a = numpy.uint8([1])
print type(a)
print math.sqrt(4)

img = cv2.imread('1/101_7.tif', 0)
result = getGabor(img)
plt.figure()

for i in range(len(result)):
    plt.subplot(1, 8, i+1)
    plt.imshow(result[i], cmap='gray')
plt.show()


img = cv2.imread('1/101_7.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img, None)
kk, des = sift.compute(gray, kp)
img = cv2.drawKeypoints(gray, kp, img)

plt.figure()
plt.subplot(1, 1, 1)
plt.imshow(img)
plt.show()
"""


img = cv2.imread('2/101_5.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


image, contours, hi = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
"""
plt.figure()
plt.subplot(1, 1, 1)
plt.imshow(img, 'gray')
plt.show()
"""
y = contours[0]
MAX = 0.0
for contour in contours:
    if len(contour) > 20:
        for i in range(len(contour)-2):
            q = contour[i-2][0]
            #print q
            p = contour[i][0]
            r = contour[i+2][0]
            cross = (q[1] - p[1]) * (r[1] - p[1]) + (q[0] - p[0]) * (r[0] - p[0])
            if cross > MAX:
                MAX = cross
                point = p


print MAX
print point
plt.figure()
plt.subplot(1, 1, 1)
plt.imshow(img, 'gray')
plt.show()
"""
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=13)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=13)
sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=13)
"""


