# _* coding: utf-8 _*_
# description : run the database to get the result

import cv2
import matplotlib.pyplot as plt
from DB import *
from fingercode import *
db_name = "final.db"
result = get_all(db_name)
images = get_image_name(result)

counts = []
for i in result:
    counts.append(convert_list(i))
# all the results cal_eluer distabce
correct_images = []
all_temp = []
for i in range(len(counts)):
    images_temp = []
    for j in range(len(counts)):
        if images[i] != images[j]:
            if images[j] not in all_temp:
                temp = cal_euler_distance(counts[i], counts[j])
                #print temp
                if (temp < 3000):
                    print temp
                    all_temp.append(images[j])
                    print images[i], images[j]
                    images_temp.append(images[j])
                    #counts.remove(counts[j])

                    img1 = cv2.imread(images[i])
                    img2 = cv2.imread(images[j])
                    plt.figure()
                    plt.subplot(1, 2, 1)
                    plt.imshow(img1)
                    plt.subplot(1, 2, 2)
                    plt.imshow(img2)
                    plt.show()

    correct_images.append(images_temp)

print len(correct_images)

"""
jk = []
for i in correct_images:
    if len(i) > 1:
        jk.append(i)



rows = len(jk)

for i in jk:
    plt.figure()
    index = 1
    for j in i:
        plt.subplot(rows, 4, index)
        img = cv2.imread(j)
        plt.imshow(img)
        index += 1
    plt.show()
"""