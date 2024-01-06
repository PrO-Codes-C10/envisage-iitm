import cv2
import numpy as np
import time
import pygame
import os

def playmusic(part1):
         pygame.mixer.init()
         ch1=pygame.mixer.Channel(0)
         ch2=pygame.mixer.Channel(1)
         ch3=pygame.mixer.Channel(2)
         a=pygame.mixer.Sound(part1)
         #b=pygame.mixer.Sound(part2)
         #c=pygame.mixer.Sound(part3)
         ch1.play(a)
         #ch2.play(b)
         #ch3.play(c)

songlen = 300
b1, b2, b3 = True,True,True
count1, count2, count3 = 0, 0, 0
    

def distance(frame,a,b):
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,np.array(a),np.array(b))
    kernel = np.ones((5, 5))
    grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if cnts!=[]:
        cmax = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(cmax)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        a = len(cmax)
        sum1 = [[0, 0]]
        for i in range(a):
            sum1 += cmax[i]

        avg = sum1 / a
        b = int(avg[0][0])
        c = int((avg[0][1]))
        cv2.circle(frame, (b, c), 3, (0, 0, 255), 2)
        dd=(b-320)*(b-320)+(c-240)*(c-240)
        d=dd**0.5
    else:
        d=1000000
    return d

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)

previous_region=np.array([1,1,1])
current_region=np.array([])
while 1:
    ret, frame = cap.read()
    
    r1=distance(frame,[29,86,6],[100,255,255])
    r2=distance(frame,[110,50,50],[130,255,255])
    r3=distance(frame,[0,100,100],[5,255,255])

    
    cv2.circle(frame,(320,240),100,(255,0,0),2)
    
    cv2.circle(frame,(320,240),200,(255,0,0),2)
   
    if r1<100:
        current_region[0]=1
        a=r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav"
    elif r1<200:
        current_region[0]=2
        a=r"C:\Users\utkarsh kumar\Desktop\envisage\2.wav"
    elif r1<1000000:
        current_region[0]=3
        a=r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav"
    else:
        current_region[0]=0
        a=r"C:\Users\utkarsh kumar\Desktop\envisage\combinations\emp.wav"

    if current_region[0]!=previous_region[0]:
        playmusic(a)
    previous_region[0]=current_region[0]




    if r2<100:
        current_region[1]=1
        b=r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav"
    elif r2<200:
        current_region[1]=2
        b=r"C:\Users\utkarsh kumar\Desktop\envisage\2.wav"
    elif r2<1000000:
        current_region[1]=3
        b=r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav"
    else:
        current_region[1]=0
        b=r"C:\Users\utkarsh kumar\Desktop\envisage\combinations\emp.wav"

    if current_region[1]!=previous_region[1]:
        playmusic(b)
    previous_region[1]=current_region[1]





    if r3<100:
        current_region[2]=1
        c=r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav"
    elif r3<200:
        current_region[2]=2
        c=r"C:\Users\utkarsh kumar\Desktop\envisage\2.wav"
    elif r3<1000000:
        current_region[2]=3
        c=r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav"
    else:
        current_region[2]=0
        c=r"C:\Users\utkarsh kumar\Desktop\envisage\combinations\emp.wav"

    if current_region[2]!=previous_region[2]:
        playmusic(c)
    previous_region[2]=current_region[2]



       
    cv2.imshow('frame', frame)       
    if cv2.waitKey(1)==27:
        break

pygame.mixer.pause()
cap.release()
cv2.destroyAllWindows()
