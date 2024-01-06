import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while 1:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_green=np.array([29,86,6])
    upper_green=np.array([100,255,255)]

    mask=cv2.inRange(hsv,lower_green,upper_green)

    kernel=np.ones((5,5))

    grad=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    cnts=cv2.findContours(grad.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cmax=max(cnts,key=cv2.contourArea)

    x.y,w,h=cv2.boundingRect(cmax)

    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    a=len(cmax)

    sum1=[[0,0]]

    for i in range(a):
        sum1 +=cmax[i]
    avg=sum1/a
    b=int(avg[0][0])
    c=int(avg[0][1])

    cv2.circle(frame,(b,c),3,(0,0,255),2)

    cv2.imshow('frame'.frame)

    print('x:',b,'y:',c)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
