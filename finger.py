# _*_ coding:utf-8 _*_

# author: Eason
# description: the fingercode base on the Gabor filter

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from Sector import *
from Gabor import *
from fingercode import *
from DB import *


# get all images path from a folder
def get_all_image(folder):
    files = os.listdir(folder)
    files_path = []
    for i in files:
        temp = folder + '/' + i
        files_path.append(temp)
    return files_path


# get the reference frame
def Get_central_point(img):
    img1 = img.copy()
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.blur(img, (5, 5))
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

    sobelx1 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    #abssobelx = cv2.convertScaleAbs(sobelx)
    #abssobelx1 = cv2.convertScaleAbs(sobelx1)

    A = sobelx.copy()
    B = sobelx1 + A
    gh = cv2.Sobel(B, cv2.CV_16S, 1, 1, ksize=3)
    gh_blur = cv2.GaussianBlur(gh, (15, 15), 0)
    gh_blur = cv2.convertScaleAbs(gh_blur,gh_blur)
    gh_media = cv2.medianBlur(gh_blur, 5)
    gh_media = cv2.medianBlur(gh_media, 5)
    gh_media = cv2.medianBlur(gh_media, 3)
    rows, cols = img.shape[:2]
    """
    for i in range(rows):
        for j in range(cols):
            print gh_media[i][j]
    """
    gh_media = cv2.convertScaleAbs(gh_media)
    gh_media = cv2.cvtColor(gh_media, cv2.COLOR_BGR2GRAY)
    ret1, binary1 = cv2.threshold(gh_media, 35, 255, cv2.THRESH_BINARY)
    #binary1 = cv2.adaptiveThreshold(gh_media, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    #print binary1[152][130]
    #image, contours, hierarchy = cv2.findContours(gh_media, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #img1 = cv2.drawContours(img, contours, 3, (0, 255, 0), 1)
    kernel = np.ones((5, 5), np.uint8)
    gh_blur = cv2.erode(binary1, kernel, iterations=1)
    rows, cols = gh_blur.shape[:2]
    max = 0.0
    row = 0
    col = 0
    for i in range(rows):
        for j in range(cols):
            if binary1[i][j] > 0:
                max = gh_blur[i][j]
                row = i
                col = j
                 #print row, col

    #print gh_media[373][387]
    #gh_blur = cv2.convertScaleAbs(gh_blur,gh_blur)
    #print rows, cols
    #print "------"
    #print row, col
    #print "------"
    rows, cols = img.shape[:2]
    if row != 0:
        if (col + 75 < cols) & (row + 75 < rows):
            print "success"
        else:
            row = 0
            col = 0
            print "failed"
    else:
        print "failed"

    plt.figure()
    plt.subplot(1, 3, 1)
    plt.imshow(binary1, cmap='gray')
    plt.subplot(1, 3, 2)
    plt.imshow(img, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.imshow(gh_media, cmap='gray')
    plt.show()

    return col, row

# copy the reference frame
def Get_core_img(img, core_x, core_y):
    radius = 75
    # crop the image 80*80
    #core_img = np.zeros((radius, radius, 3), np.uint8)
    core_img = img[core_y-radius:core_y+radius, core_x-radius:core_x+radius]

    return core_img


if __name__ == '__main__':
    folder = '2'
    db_name = '1.db'
    # initlize the database
    initlize_db(db_name)
    # get the images path
    images_path = get_all_image(folder)
    # start processing
    id = 0
    for image in images_path:

        print image
        img = cv2.imread(image)
        rows, cols = img.shape[:2]
        # get the reference point
        core_x, core_y = Get_central_point(img)

        print core_x, core_y
        if core_x != 0:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            core_img = Get_core_img(img, core_x, core_y)

            plt.figure()
            plt.subplot(1, 2, 1)
            plt.imshow(img, cmap='gray')
            plt.subplot(1, 2, 2)
            plt.imshow(core_img, cmap='gray')
            plt.show()

            # divide the img sector
            sectors = Divide_sector(core_img)

            core_img = Normalize_img(core_img, sectors)

            #cv2.imwrite('kkk.tif', core_img)
            # show normalize image

            plt.figure()
            plt.subplot(1, 1, 1)
            plt.imshow(core_img, cmap='gray')
            plt.show()

            result = getGabor(core_img)
            # show Gabor filters process images

            plt.figure()
            for i in range(len(result)):
                plt.subplot(1, 8, i+1)
                plt.imshow(result[i], cmap='gray')
            plt.show()

            gh = []
            ADD = []
            for i in result:

                imgtemp, fingercodetemp = fingercode(i)
                gh.append(imgtemp)
                ADD.append(fingercodetemp)
            # convert tht array to string
            temp = []
            for i in ADD:
                temp.append(str(i))

            # insert the image name
            temp.insert(0, image)
            temp.insert(0, id)
            save_fingercode(db_name, temp)
            id += 1

            plt.figure()
            for i in range(len(gh)):
                plt.subplot(1, 8, i+1)
                plt.imshow(gh[i], cmap='gray')
            plt.show()
