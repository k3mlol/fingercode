# _*_ coding: utf-8 _*_

import cv2
img = cv2.imread('1/101_8.tif', 0)


class Ponit:
    def __init__(self, x, y, gray):
        self.X = x
        self.Y = y
        self.Gray = gray


a = []
for i in range(8):
    a.append(Ponit(100, 100, 30))

print type(a[0])
print a[0].Gray
print len(a)