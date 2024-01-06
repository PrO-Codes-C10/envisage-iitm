import cv2               
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
s1=r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav"

a1=a2=a3=a4=0
b1=b2=b3=b4=True
songlen=100
import pygame
def playmusic(s):
        pygame.mixer.init()
        ch1=pygame.mixer.Channel(0)
        a=pygame.mixer.Sound(s)
        ch1.play(a)


def selected_range(hsv,a,b):
        lower_green = np.array(a)
        upper_green = np.array(b)
        mask = cv2.inRange(hsv, lower_green, upper_green)
        kernel = np.ones((5, 5))
        grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return cnts

def distance(cnts):
    cmax = max(cnts, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(cmax)
    if w*h>1000:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            a = len(cmax)
            sum1 = [[0, 0]]
            for i in range(a):
                sum1 += cmax[i]
            avg = sum1 / a
            b = int(avg[0][0])
            c = int((avg[0][1]))
            cv2.circle(frame, (b, c), 3, (0, 0, 255), 2)
            r=(b-960)*(b-960) + (c-540)*(c-540)
            r=r**0.5
            return(r)
    else:
            return(0)



while 1:
    
    ret, frame = cap.read()
    cv2.circle(frame, (320,240), 100, (0, 0, 255), 2)
    cv2.circle(frame, (320,240), 200, (0, 0, 255), 2)
    cv2.circle(frame, (320,240), 300, (0, 0, 255), 2)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cnts1=selected_range(hsv,[29,86,6],[100,255,255])#determine the colour here

    
    if cnts1 != [] :            
            r=distance(cnts1)
            
    
    if r<100:
        
        if b1:           
                playmusic(s1)
        b1=False
        a1+=1
        if a1>songlen:
                b1=True
                a1=0
   
        
    if 100<=r<200:
        if b2:           
                playmusic(s1)
        b2=False
        a2+=1
        if a2>songlen:
                b2=True
                a2=0
   
       
    if 200<=r<300:
        if b3:           
                playmusic(s1)
        b3=False
        a3+=1
        if a3>songlen:
                b3=True
                a3=0

    
   

    cv2.imshow('frame', frame)
    
    
    if cv2.waitKey(1)==27:  #press escape to exit
        break



cv2.destroyAllWindows()
cap.release()

