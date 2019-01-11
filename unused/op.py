# _*_ coding: utf-8 _*_

import cv2
import matplotlib.pyplot as plt
from DB import *
from fingercode import *


# this part id for test the DB function weather is ok

a = []
b = []
for i in range(8):
    for j in range(80):
        b.append(45.0)
    a.append(b)

c = []
d = []
for i in range(8):
    for j in range(80):
        c.append(30.0)
    d.append(c)

jk = cal_euler_distance(a, d)

print "--------"
print jk
print "--------"
# convert to string
temp = []
for i in a:
    temp.append(str(i))
image_name = '2/101_2.tif'
temp.insert(0, image_name)
# insert the id and the image name
temp.insert(0, 2)
#print temp[1]
initlize_db('1.db')
#save_fingercode('1.db', temp)
result = get_fingercode('1.db')
#print result
print len(result)

target = []

for i in range(2, len(result)):
    temp = list(eval(result[i]))
    print type(temp)
    target.append(temp)
    print len(temp)

print len(target)

all_result = get_all('1.db')

ko = get_image_name(all_result)
print len(ko)
print ko[7]

lp = cv2.imread(ko[7])
plt.figure()
plt.subplot(111)
plt.imshow(lp)
plt.show()
"""
print len(all_result)
ll = []
for index in all_result:
     ll.append(convert_list(index))

# all the results cal_eluer distabce
for i in range(len(ll)-1):
    for j in range(i, len(ll)-1):
        print cal_euler_distance(ll[i], ll[j])
"""