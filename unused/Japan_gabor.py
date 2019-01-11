# encoding: utf-8
# gabor.py
# 2012-3-8
# 2013-8-30 getGaborKernel
# Eiichiro Momma
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


src_f = 0
kernel_size = 33
pos_sigma = 4
pos_lm = 10
pos_th = 0
pos_gam = 100
pos_psi = 90

def Process():
    sig = pos_sigma
    lm = pos_lm
    th = pos_th*np.pi/180.
    gm = pos_gam/100.
    ps = (pos_psi-180)*np.pi/180
    print 'kern_size=' + str(kernel_size) + ', sig=' + str(sig) + ', th=' + str(pos_th) + ', lm=' + str(lm) +', gm=' + str(gm) + ', ps=' + str(ps)
    kernel = cv.getGaborKernel((kernel_size,kernel_size),sig,th,lm,gm,ps)
    kernelimg = kernel/2.+0.5
    global src_f
    dest = cv.filter2D(src_f, -1, kernel)
    rows, cols = dest.shape[:2]
    for i in range(rows):
        for j in range(cols):
            if dest[i][j] > 255:
                print dest[i][j]
    cv.imshow('Process window', dest)
    cv.imshow('Kernel', cv.resize(kernelimg, (kernel_size*20,kernel_size*20)))
    cv.imshow('Mag', np.power(dest,2))

def cb_sigma(pos):
    global pos_sigma
    if pos > 0:
         pos_sigma = pos
    else:
        pos_sigma = 1
    Process()

def cb_lm(pos):
    global pos_lm
    pos_lm = pos
    Process()

def cb_th(pos):
    global pos_th
    pos_th = pos
    Process()

def cb_psi(pos):
    global pos_psi
    pos_psi = pos
    Process()

def cb_gam(pos):
    global pos_gam
    pos_gam = pos
    Process()

if __name__ == '__main__':
    image = cv.imread("kkk.tif")
    #cv.imshow('Src', image)

    src = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #global src_f
    src_f = np.array(src, dtype=np.float32)
    src_f /= 255.
    if not kernel_size%2:
        kernel_size += 1


    cv.namedWindow('Process window',1)
    cv.createTrackbar('Sigma','Process window',pos_sigma,kernel_size/2,cb_sigma)
    cv.createTrackbar('Lambda', 'Process window', pos_lm, kernel_size-2, cb_lm)
    cv.createTrackbar('Theta', 'Process window', pos_th, 360, cb_th)
    cv.createTrackbar('gamma', 'Process window', pos_gam, 300, cb_gam)
    cv.createTrackbar('Psi', 'Process window', pos_psi, 360, cb_psi)
    Process()
    cv.waitKey(0)
    cv.destroyAllWindows()
