from cv2 import cv2
import strel
import myutil
import numpy as np

def myerode(im,el):
    return cv2.erode(im, el)

def mydilate(im,el):
    return cv2.dilate(im,el)

def mygrad(im,el):
    return cv2.dilate(im,el) - cv2.erode(im, el)

def myopen(im,el):
    return mydilate(myerode(im,el),el)

def myclos(im,el):
    return myerode(mydilate(im,el),el) 

def tresh(im,tresh):
    res = np.zeros(im.shape,im.dtype)
    res[im>=tresh] = 255
    return res

def myconddilat(im,M,el):
    return np.minimum(im,mydilate(M,el))

def myconderod(im,M,el):
    return np.maximum(im,myerode(M,el))

def myreconinf(im,M,el):
    r_copie = M
    r = myconddilat(im,M,el)
    while not np.array_equal(r_copie,r):
        r_copie = r
        r = myconddilat(im,r,el)
    return r

def myreconsup(im,M,el):
    r_copie = M
    r = myconderod(im,M,el)
    while not np.array_equal(r_copie,r):
        r_copie = r
        r = myconderod(im,r,el)
    return r

def myopenrecon(im,el_o,el_r):
    return myreconinf(im,myopen(im,el_o),el_r)

def myclosrecon(im,el_c,el_r):
    return myreconsup(im,myclos(im,el_c),el_r)

def mymaxima(im,h,el):
    im_h = np.maximum(im,h) - h
    return myreconinf(im,im_h,el)