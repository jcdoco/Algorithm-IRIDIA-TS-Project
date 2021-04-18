import numpy as np
import cv2


def myseuil(im, s):
    im_s = np.zeros(im.shape, im.dtype)
    #im_s = np.zeros(im)
    im_s[im >= s]=255
    return im_s





def myseuil_interactif(im):
    global seuil

    def myseuil_interactif_callback(val):
        global seuil
        seuil=val
        cv2.imshow('Seuil Interactif', myseuil(im, seuil))

    cv2.namedWindow('Seuil Interactif')
    cv2.createTrackbar('Seuil', 'Seuil Interactif', 100, 256, myseuil_interactif_callback)
    myseuil_interactif_callback(100)

    cv2.waitKey(0)
    cv2.destroyWindow('Seuil Interactif')
    return seuil