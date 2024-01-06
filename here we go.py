import cv2
import numpy as np
import pyglet
import time
import pygame
import pyautogui
import os



cap = cv2.VideoCapture(0)

cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)     

def selected_range(hsv,a,b):
        lower_green = np.array(a)
        upper_green = np.array(b)
        mask = cv2.inRange(hsv, lower_green, upper_green)
        kernel = np.ones((5, 5))
        grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return cnts
        
def playmusic1(a1,a2):

         pygame.mixer.init()
         ch1=pygame.mixer.Channel(0)
         ch2=pygame.mixer.Channel(1)
         a=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\combinations\{}".format(a1))
         b=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\combinations\{}".format(a2))
         ch1.play(a)
         ch2.play(b)



while 1:
    ret, frame = cap.read()

    hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    cnts1=selected_range(hsv1,[29,86,6],[100,255,255])
   
    cnts2=selected_range(hsv1,[0,100,100],[5,255,255])

     
    r1=0
    r2=0
      
    if cnts1 != []:            
            cmax = max(cnts1, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(cmax)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            a = len(cmax)
            sum1 = [[0, 0]]
            for i in range(a):
                sum1 += cmax[i]

            avg = sum1 / a
            b1 = int(avg[0][0])
            c1 = int((avg[0][1]))
            cv2.circle(frame, (b1, c1), 3, (0, 0, 255), 2)
           
            r1=(b1-240)*(b1-240) + (c1-320)*(c1-320)

    if cnts2 != []:            
            cmax = max(cnts2, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(cmax)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            a = len(cmax)
            sum1 = [[0, 0]]
            for i in range(a):
                sum1 += cmax[i]

            avg = sum1 / a
            b2 = int(avg[0][0])
            c2 = int((avg[0][1]))
            cv2.circle(frame, (b2, c2), 3, (0, 0, 255), 2)
           
            r2=(b2-240)*(b2-240) + (c2-320)*(c2-320)



    if r1==0:
        a1='emp.wav'
    if 0 < r1 < 6400:

        a1='a1.wav'
               
    if 6400 < r1 < 25600:
               
        a1='a2.wav' 

    if 25600 < r1 < 57600:

        a1='a3.wav'

    if 57600 < r1 < 102400:

        a1='a4.wav'
                
    if 102400 < r1 < 160000:

        a1='a5.wav'

    if  160000 < r1 < 230400:

        a1='a6.wav'
                
    if  230400 < r1 < 313600:

        a1='a7.wav'
                
    if  313600 < r1 < 409600:

        a1='a8.wav'

    if  409600 < r1 < 518400:

        a1='a9.wav'

                
    if 518400 < r1 < 640000:

        a1='a10.wav'   
           


    if r2==0:
        a2='emp.wav'
    if 0 < r2 < 6400 :

        a2='g1.wav'
               
    if 6400 < r2 < 25600:
               
        a2='g2.wav' 

    if 25600 < r2 < 57600:

        a2='g3.wav'

    if 57600 < r2 < 102400:

        a2='g4.wav'
                
    if 102400 < r2 < 160000:

        a2='g5.wav'

    if  160000 < r2 < 230400:

        a2='g6.wav'
                
    if  230400 < r2 < 313600:

        a2='g7.wav'
                
    if  313600 < r2 < 409600:

        a2='g8.wav'

    if  409600 < r2 < 518400:

        a2='g9.wav'

                
    if 518400 < r2 < 640000:

        a2='g10.wav'   
           
    playmusic1(a1,a2)       
    cv2.imshow('frame', frame)
    
    
    if cv2.waitKey(1)==27:
        break



cv2.destroyAllWindows()


    
