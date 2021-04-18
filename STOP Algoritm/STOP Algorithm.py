from cv2 import cv2
import strel #file in order to build the structuring elements
import numpy as np
import morpho #file containing the functions of morphological transformations

im_orig=cv2.imread('stop.jpg',0)#loading original image but gray tint
im_gray_area=cv2.resize(im_orig,(640,480))#modification of the size of the image

cv2.imshow('im gray',im_gray_area)#image display
cv2.imwrite('1_Stop_Gray.jpg',im_gray_area)#save image

im_color_orig=cv2.imread('stop.jpg')#loading original image
im_color=cv2.resize(im_color_orig,(640,480))#modification of the size of the image
cv2.imshow('im color',im_color)#image display
cv2.imwrite('2_Stop_color.jpg',im_color)#save image

#the idea is to filter the pixels and their data a new value if they are included in ranges of values.
for i in range(0,im_gray_area.shape[0]):#selection of image pixel columns
    for j in range(0,im_gray_area.shape[1]):#selection of image pixel lines
        if (im_gray_area[i,j]>240):
            im_gray_area[i,j]=0
        if (im_gray_area[i,j]>0) & (im_gray_area[i,j]<130):
            im_gray_area[i,j]=0

ret_gray,t_gray=cv2.threshold(im_gray_area,127,255,cv2.THRESH_BINARY)#choice of threshold for the gray area
cv2.imshow('t_gray',t_gray)#image display
cv2.imwrite('3_Stop_thresh_gray_aera.jpg',t_gray)#save image
#contour selection
contours_1,hierarchy_1=cv2.findContours(t_gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("shapes found : ",len(contours_1))#display the number of contours
#it is necessary to filter the contours via a parameter, 
# in this case, we use the concept of area of ​​a geometric figure
for cnt in contours_1:
    area=cv2.contourArea(cnt)
    if (area>10000):
        epsilon=0.01*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(im_color,[approx],0,(0,0,255),3)

cv2.imshow('im_Final_Aggragation',im_color)#display the final result
cv2.imwrite('4_Stop_Result_Final.jpg',im_color)#save image
cv2.waitKey(0)