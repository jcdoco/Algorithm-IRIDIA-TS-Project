from cv2 import cv2
import numpy as np
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
x,y = -1,-1


def mouse_drawing(event,x,y,flags,params):
    #global ix,iy,drawing,img
    global drawing,img
    if event == cv2.EVENT_LBUTTONDOWN:
        print('left click')
        drawing = True
        print(x,y)
    elif event == cv2.EVENT_MOUSEMOVE:
        print('mouse mouve')
        if drawing == True:
            if mode == True:
                cv2.circle(img,(x,y),2,(255,255,255),1)
                print('i m drawing')
            else:
                cv2.circle(img,(x,y),2,(255,255,255),1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

            


def nothin(x):
    print(x)

img = cv2.imread('image_2.jpg')
img1 = cv2.resize(img,(960,720))
print(img1.shape)
#img = cv2.imread('yoda.png',0)
#print(img.shape)
img = np.zeros((720,960,3), np.uint8)

output = cv2.addWeighted(img1, 0.1, img, 0.1, 0)
 


cv2.namedWindow('window')
cv2.setMouseCallback('window',mouse_drawing)

cv2.createTrackbar('alpha','window',0,10,nothin)

while(True):
    cv2.imshow('window', output)
    cv2.imshow('img', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
        
    
    alpha = cv2.getTrackbarPos('alpha', 'window') * 0.1
    beta = 1 - alpha
    output = cv2.addWeighted(img1, alpha, img, beta, 0)
    cv2.imwrite('mask1.jpg',img)


cv2.destroyAllWindows()
cv2.waitKey(0)