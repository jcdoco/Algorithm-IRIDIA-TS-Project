from cv2 import cv2
import strel#file in order to build the structuring elements
import numpy as np
import morpho#file containing the functions of morphological transformations

im_orig=cv2.imread('image_1.jpg',0)#loading original image but gray tint
im_black_aera=cv2.resize(im_orig,(640,480))#modification of the size of the image for black aera
im_gray_area=cv2.resize(im_orig,(640,480))#modification of the size of the image for gray aera
im_white_area=cv2.resize(im_orig,(640,480))#modification of the size of the image for withe aera
cv2.imshow('im gray',im_black_aera)#image display
#cv2.imwrite('1_foraging_Gray.jpg',im_black_aera)#save image

im_color_orig=cv2.imread('image_1.jpg')#loading original color image
im_color=cv2.resize(im_color_orig,(640,480))#modification of the size of the image
cv2.imshow('im color',im_color)#image display
#cv2.imwrite('2_foraging_color.jpg',im_color)#save image

#the idea is to filter the pixels and their data a new value if they are included in ranges of values.
for i in range(0,im_black_aera.shape[0]):#selection of image pixel columns
    for j in range(0,im_black_aera.shape[1]):#selection of image pixel lines
        #concerns pixels in the gray area
        if  (im_gray_area[i,j]>240):
            im_gray_area[i,j]=0

        if  (im_gray_area[i,j]>0) & (im_gray_area[i,j]<130):
            im_gray_area[i,j]=0
        #concerns pixels in the black area
        #black area 20 et 40
        if (im_black_aera[i,j]<20):
            im_black_aera[i,j]=255
        if (im_black_aera[i,j]>40):
            im_black_aera[i,j]=255
        #concerns pixels in the white aera
        if im_white_area[i,j]<220:
            im_white_area[i,j]=0

##change of lower of thresh
ret_black,t_black=cv2.threshold(im_black_aera,127,255,cv2.THRESH_BINARY)#choice of threshold for the black zone
ret_gray,t_gray=cv2.threshold(im_gray_area,127,255,cv2.THRESH_BINARY)#choice of threshold for the gray zone
ret_white,t_white=cv2.threshold(im_white_area,127,255,cv2.THRESH_BINARY)#choice of threshold for the white zone
cv2.imshow('t_black',t_black)#image display
#cv2.imwrite('3_foraging_thresh_black_aera.jpg',t_black)#save image
cv2.imshow('t_gray',t_gray)#image display
#cv2.imwrite('4_foraging_thresh_gray_aera.jpg',t_gray)#save image
cv2.imshow('t_write',t_white)#image display
#cv2.imwrite('5_foraging_thresh_write_aera.jpg',t_white)#save image

#construction of a structuring element intended for the gray area
el=strel.build('carre',1,0)
op=morpho.myopen(t_gray,el)

#contour selection
contours,hierarchy=cv2.findContours(t_black,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#selection of contours for the black area
contours_1,hierarchy_1=cv2.findContours(op,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#selection of contours for the gray area
contours_2,hierarchy_2=cv2.findContours(t_white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#selection of contours for the white area
print("shapes found : ",len(contours))#print the numbers of outlines

#it is necessary to filter the contours via a parameter, 
# in this case, we use the concept of area of ​​a geometric figure
for cnt in contours:#concerns the black area
    area=cv2.contourArea(cnt)
    if (area>10000):
        epsilon=0.01*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(im_color,[approx],0,(0,255,0),3)

for cnt in contours_1:#concerns the gray area
    area=cv2.contourArea(cnt)
    if (area>10000):
        epsilon=0.01*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(im_color,[approx],0,(0,0,255),3)
for cnt in contours_2:#concerns the white area
    area=cv2.contourArea(cnt)
    if (area>10000):
        epsilon=0.01*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(im_color,[approx],0,(255,0,0),3)

cv2.imshow('im_Final_foraging',im_color)#display of the final result
#cv2.imwrite('6_foraging_Result_Final.jpg',im_color)#save final resul
cv2.waitKey(0)