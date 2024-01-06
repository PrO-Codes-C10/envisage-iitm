import cv2
import numpy as np

def selected_range(hsv,a,b):
        lower_green = np.array(a)
        upper_green = np.array(b)
        mask = cv2.inRange(hsv, lower_green, upper_green)
        kernel = np.ones((5, 5))
        grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        if cnts!=[]:
            
            cmax = max(cnts, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(cmax)
            return (w*h)
        else :
            return(0)

img=cv2.imread(r'C:\Users\utkarsh kumar\Pictures\red.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

'''for i in range(0,256):
    for j in range(0,256):
        for k in range(0,256):
            r=selected_range(hsv,[i,j,k],[i,j,k])
            if r>1000:
                
                print(i,' ',j,' ',k)'''
