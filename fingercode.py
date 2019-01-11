# _* coding: utf-8 _*_

import math
from Sector import *


def cal_standar(points, mean):
    total = 0
    for i in range(len(points)):
        point = points[i]
        total += math.pow(point.Gray - mean, 2)
    if len(points) != 0:
        return total / len(points)
    else:
        return 0

# calculate the fingercode
def fingercode(img):

    # divide the sectors
    sectors = Divide_sector(img)
    result = []
    Mean = []
    for i in range(len(sectors)):
        Mean.append(cal_mean(sectors[i]))

    Variance = []
    for i in range(len(sectors)):
        Variance.append(cal_standar(sectors[i], Mean[i]))

    for i in range(len(sectors)):
        temp = round(math.sqrt(Variance[i]), 0)
        #print temp
        result.append(int(temp))
    #return result
    print "------"
    print result
    print "------"
    # show the fingercode
    for i in range(len(sectors)):
        sector = sectors[i]
        for point in sector:
            img[point.X, point.Y] = result[i]
    return img, result
    #return result


# get the result from database and convert to list
# return list type
def convert_list(result):
    target = []
    for i in range(2, len(result)):
        temp = list(eval(result[i]))
        #print type(temp)
    target.append(temp)
    return target


# calculate the fingercode Euler ventor
def cal_euler_distance(result1, result2):
    distance = 0
    for i in range(len(result1)):
        temp1 = result1[i]
        temp2 = result2[i]
        for j in range(len(temp1)):
            distance += math.pow(temp1[j] - temp2[j], 2)

    return distance


# get the images name from the database
def get_image_name(result):

    image_name = []
    for i in result:
        image_name.append(i[1])
    return image_name
