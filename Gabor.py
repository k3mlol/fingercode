# _*_ encoding: utf-8 _*_
# description: the Gabor filters function

# this is for build the Gabor filter
import cv2
import numpy as np

# the paper setup the param is sigma_x = 4.0, sigma_y = 4.0 f = 0.1
# sigma_x = sigma
# so from the Gabor source code sigma_y = sigma_x / gamma
# the gamma should be 1.0
# lamba = 0.1
def build_filters():
    filters = []
    sigma = 4
    gamma = 1.0
    ksize = 33
    lamba = 10
    ps = (90-180)*np.pi/180.0
    for theta in np.arange(0, np.pi, np.pi / 8):
        kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamba, gamma, ps)
        #kern = kern/2 + 0.5
        filters.append(kernel)
    return filters


# processing the img
def process(img, kernel):
    #img = np.array(img, dtype=np.float32)
    #img /= 255.
    dest = cv2.filter2D(img, -1, kernel)
    return dest


# get the image's result after the Gabor filtering
def getGabor(img):
    filters = build_filters()
    res = []
    for i in filters:
        res1 = process(img, i)
        res.append(res1)
    """
    plt.figure(2)
    for temp in xrange(len(res)):
        plt.subplot(4, 6, temp+1)
        plt.imshow(res[temp], cmap='gray')

    plt.show()
    """
    return res

