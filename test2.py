import cv2
import numpy as np
img=cv2.imread(r'C:\Users\utkarsh kumar\Pictures\red.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.rectangle(hsv, (500,360), (950,400), (0, 0, 255), 3)

cv2.imshow('frame',hsv)

for i in range(500,950):
    for j in range(360,400):
        h,s,v=hsv[i,j]
        print(h,' ',s,' ',v)

