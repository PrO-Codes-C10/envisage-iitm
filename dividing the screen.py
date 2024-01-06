import cv2
import pyautogui as p
import numpy as np

#pixel size of the webcam window is: height 480   width 640

print(p.size())

cap=cv2.VideoCapture(0)
r,img=cap.read()
(height,width,depth)=img.shape
cap.release()
cv2.destroyAllWindows()
    
h=height
w=width

#x : 1 - 640   y : 1 - 480



arr=[roi1,roi2,roi3,roi4]
print(arr)
c=0
ROI=[]
for x in range(1,621,20):
    for y in range(1,461,20):
        ROI.append(img[x:x+20,y:y+20])
print(ROI)
