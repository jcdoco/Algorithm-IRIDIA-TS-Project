from cv2 import cv2
import strel #file in order to build the structuring elements
import numpy as np
import morpho #file containing the functions of morphological transformations



im_original = cv2.imread('image_2.jpg',0)#loading original image but gray tint
im_black_aera=cv2.resize(im_original,(640,480))#modification of the size of the image
im_gray_area=cv2.resize(im_original,(640,480))#modification of the size of the image
cv2.imshow('im gray',im_black_aera)#gray tint image display
cv2.imwrite('1_Aggregation_Gray.jpg',im_black_aera)#save image

im_color_original=cv2.imread('image_2.jpg')#loading original image
im_color=cv2.resize(im_color_original,(640,480))#modification of the size of the image
cv2.imshow('im color',im_color)#color image display
cv2.imwrite('2_Aggregation_color.jpg',im_color)#save image

#the idea is to filter the pixels and their data a new value if they are included in ranges of values.
for i in range(0,im_black_aera.shape[0]):#selection of image pixel columns
    for j in range(0,im_black_aera.shape[1]):#selection of image pixel lines
        #concerns pixels in the gray area
        if (im_gray_area[i,j]>240):
            im_gray_area[i,j]=0

        if (im_gray_area[i,j]>0) & (im_gray_area[i,j]<130):
            im_gray_area[i,j]=0
        #concerns pixels in the black area
        #black area 20 et 40
        if (im_black_aera[i,j]<20):
            im_black_aera[i,j]=255
        if (im_black_aera[i,j]>40):
            im_black_aera[i,j]=255
        """
        #concerns pixels in the white area
        if im[i,j]<220:
            im[i,j]=0
        """

#change of lower of thresh
ret_black,t_black=cv2.threshold(im_black_aera,127,255,cv2.THRESH_BINARY)#choice of threshold for the black zone
ret_gray,t_gray=cv2.threshold(im_gray_area,127,255,cv2.THRESH_BINARY)#choice of threshold for the gray area

cv2.imshow('t_black',t_black)#image display, black area, after the threshold
cv2.imwrite('3_Aggreagation_thresh_black_aera.jpg',t_black)

cv2.imshow('t_gray',t_gray)#display of the image, gray area, after the threshold
cv2.imwrite('4_Aggregation_thresh_gray_aera.jpg',t_gray)

#contour selection
contours,hierarchy=cv2.findContours(t_black,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#selection of contours for the black area
contours_1,hierarchy_1=cv2.findContours(t_gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#selection of contours for the gray area
print("shapes found : ",len(contours))

#it is necessary to filter the contours via a parameter, 
# in this case, we use the concept of area of ​​a geometric figure
for cnt in  contours:#concerns the black area
    area=cv2.contourArea(cnt)
    if (area>10000):
        epsilon=0.01*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(im_color,[approx],0,(0,255,0),3)#select the color green

for cnt in  contours_1:#concerns the gray area
    area=cv2.contourArea(cnt)
    if (area>10000):
        epsilon=0.01*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(im_color,[approx],0,(0,0,255),3)#we select the color red

'''
#we use this syntax when we want to select all outlines
for cnt in contours:
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(im_color, [approx],0, (0,255,0), 3)

'''
cv2.imshow('im_Final_Aggragation',im_color)#display of the final result
cv2.imwrite('5_Aggregation_Result_Final.jpg',im_color)#save final result
cv2.waitKey(0)