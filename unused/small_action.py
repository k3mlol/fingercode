# _*_ coding: utf-8 _*_
# descrption: some small functions
import os
import cv2
from finger import *

# get all images path from a folder
def get_all_image(folder):
    files = os.listdir(folder)
    files_path = []
    for i in files:
        temp = folder + '/' + i
        files_path.append(temp)
    return files_path

success = 0
failed = 0
images_path = get_all_image('2')
for image in images_path:
    img = cv2.imread(image)
    print image
    core_x, core_y = Get_central_point(img)
    rows, cols = img.shape[:2]

    if core_x != 0:
        if (core_x + 75 > cols) | (core_y + 75 > rows):
            print "failed"
            failed += 1
        else:
            print "success"
            print image
            success += 1
    else:
        print "failed"
        failed += 1
print "success:", success
print "failed:", failed
