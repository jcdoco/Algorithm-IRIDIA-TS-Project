#based on John Chaussard's algorithm

from cv2 import cv2
import strel #file in order to build the structuring elements
import numpy as np
import morpho #file containing the functions of morphological transformations

def search_altitude_min(l):
    i = 0
    while(len(l[i])==0):
        i = i+1
    return i

im_tro_gd_color = cv2.imread('image_8.jpg')
im_trop_grand = cv2.imread('image_8.jpg',0)
im = cv2.resize(im_trop_grand,(900,675))
cv2.imshow('im gray',im)# display
cv2.imwrite('1_watershed.jpg',im)#save image
imcolor = cv2.resize(im_tro_gd_color,(900,675))
cv2.imshow('im color',imcolor)# display
cv2.imwrite('2_watershed.jpg',imcolor)#save image

#mask 1 & 2
obj = cv2.imread('mask1.jpg',0)
cv2.imshow('mask1',obj)# display
cv2.imwrite('3_watershed.jpg',obj)#save image
comp = cv2.imread('mask2.jpg',0)
cv2.imshow('mask2',comp)# display
cv2.imwrite('4_watershed.jpg',comp)#save image

r = np.zeros(im.shape,im.dtype)
r = r + np.uint8(obj/255*10) + np.uint8(comp/255*20)
cv2.imshow('r',r)# display
cv2.imwrite('5_watershed.jpg',r)#save image

#structural element
g8 = strel.build('carre',1 )
grad = morpho.mygrad(im,g8)
cv2.imshow('grad',r)# display
cv2.imwrite('6_watershed.jpg',grad)#save image

#list with 256 lists inside
l = [[] for i in range(0,256)]


#add at list
#li.append

#soustraction of a element of the list
#li.pop(0) #indice of the element to soustract

#count of the number of elements in all lists of l
nb_el_liste = 0

#iterate through r to find the pixels that have a non-zero value at the start
for x in range(0,r.shape[0]):
    for y in range(0,r.shape[1]):
        if r[x,y]>0:
            alt = grad[x,y]
            l[alt].append((x,y))
            nb_el_liste+=1

#returns the coordinates of the pixels of the structuring element
g8_liste = strel.build_as_list('carre', 1, None)
print(g8_liste)

#g8 minus the origin (0,0)
g8etoile_liste = [v for v in g8_liste if v !=(0,0)]
print(g8etoile_liste)

k = 0

#as long as there are elements in one of the lists l
while(nb_el_liste > 0):
    #we look for the pixels of the lowest altitude in grad
    alt = search_altitude_min(l)
    #we remove a pixel among all those of lower altitude
    (x,y) = l[alt].pop(0)
    nb_el_liste-=1
    k+=1
    #for each neighbor (px, py) of (x, y)
    for (vx,vy) in g8etoile_liste:
        px = x + vx
        py = y + vy

        if (px >= 0 and py >=0 and px < r.shape[0] and py<r.shape[1] and r[px,py]==0):
            #(px, py) must belong to the same object as (x, y)
            r[px,py] = r[x,y]
            #the altitude of p (px, py) is equal to its value of the gradient image
            l[grad[px,py]].append((px,py))
            nb_el_liste+=1
          
    if (k%10000) == 0:       
        cv2.imshow("res",r)
        cv2.waitKey(500)
    
#cv2.imshow("grad",imcolor)
cv2.imshow("res prim",r)
cv2.imwrite('7_watershed.jpg',r)#save image
imcolor2 = cv2.resize(im_tro_gd_color,(900,675))
gradr = morpho.mygrad(r,g8)
gradr_5 = gradr*5
cv2.imshow('grad5',gradr_5)# display
cv2.imwrite('8_watershed.jpg',r)#save image

#display of the image with the detected aera
imcolor2[gradr_5>20] = [0,0,255]
cv2.imshow("res final",imcolor2)
cv2.imwrite('9_watershed.jpg',imcolor2)#save image

cv2.waitKey(0)



cv2.waitKey(0)