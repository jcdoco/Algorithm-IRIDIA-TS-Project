from cv2 import cv2
import strel#file in order to build the structuring elements
import numpy as np
import morpho#file containing the functions of morphological transformations


img = cv2.imread('image_2.jpg')#loading original image
im = cv2.imread('image_2.jpg',0)#loading original image but gray tint

#creation of a table that will create an empty image 
#it has the same shape as the original image
tab = np.ones(im.shape,np.uint8)*255
cv2.imshow('tab', tab)
cv2.imwrite('1_Detct_black_aera.jpg',tab)

#loading duplicate gray tint image
im_2 = cv2.imread('image_2.jpg',0)

"""
#rectangle black
#el = strel.build('carre',2,0)
#triangle black
"""

#creation of a structuraling element
el = strel.build('diamant',2,0)

#use of the morphological gradient technique
grad = morpho.mygrad(im,el)
cv2.imshow('grad', grad)
cv2.imwrite('2_Detct_black_aera.jpg',grad)


grad3 = morpho.mygrad(im,el)
grad4=grad3*10
cv2.imshow('grad4', grad4)
cv2.imwrite('3_Detct_black_aera.jpg',grad4)

##the idea is to filter the pixels and their data a new value if they are included in ranges of values.
for i in range(0,im_2.shape[0]):
    for j in range(0,im_2.shape[1]):
        if (grad[i,j]>=0) & (grad[i,j]<10):
            tab[i,j]=im_2[i,j]

cv2.imshow('tab prim', tab)
cv2.imwrite('4_Detct_black_aera.jpg',tab)

#use of the morphological gradient technique
grad2 = morpho.mygrad(tab,el)
cv2.imshow('grad2', grad2)
cv2.imwrite('5_Detct_black_aera.jpg',grad2)

#creation of a table that will create an empty image 
#it has the same shape as the original image
tab_1 = np.zeros(im.shape,np.uint8)
cv2.imshow('tab 1', tab_1)
cv2.imwrite('6_Detct_black_aera.jpg',tab_1)


#second filtering pixels according to their value
for i in range(0,im_2.shape[0]):
    for j in range(0,im_2.shape[1]):
        if (grad2[i,j]>=220) & (grad2[i,j]<=245):
            tab_1[i,j]=grad2[i,j]

cv2.imshow('tab 1 prime', tab_1)
cv2.imwrite('7_Detct_black_aera.jpg',tab_1)
#contour detection and contour drawing
contours, hierarchy = cv2.findContours(tab_1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

"""
for cnt in contours:    
    area = cv2.contourArea(cnt)
    if (area > 50000) & (area < 52000):
        print(area)
        epsilon = 0.01*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(img, [approx],0, (0,255,0),3)
"""
#it is necessary to filter the contours via a parameter, 
# in this case, we use the concept of area of ​​a geometric figure
for cnt in contours:
    area = cv2.contourArea(cnt)
    if (area > 95000) & (area < 100600):
        print(area)
        epsilon = 0.01*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(img, [approx],0, (0,255,0),3)
"""
for cnt in contours:
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(img, [approx],0, (0,255,0), 3)
"""



cv2.imshow('img', img)#display final result
cv2.imwrite('8_Detct_black_aera.jpg',img)
#cv2.imwrite("triangl_sh.jpg",img)#save image




cv2.waitKey(0)