#importing the required libraries

import cv2               
import numpy as np       
import pyglet
import time
import pygame
import pyautogui
import os


pygame.mixer.init(frequency=42050)
ch1=pygame.mixer.Channel(0)
ch2=pygame.mixer.Channel(1)
ch3=pygame.mixer.Channel(2)
a=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav")
b=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav")
c=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav")
ch1.play(a)
ch2.play(b)
ch3.play(c)


cap = cv2.VideoCapture(0)

cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)     

list=[0,1213200,2426400,3639600,4852800]

#function that gives the countours of the colour we want to detect

def selected_range(hsv,a,b):
        lower_green = np.array(a)
        upper_green = np.array(b)
        mask = cv2.inRange(hsv, lower_green, upper_green)
        kernel = np.ones((5, 5))
        grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return cnts
        

        
#returns  the coordinates of the approximate centroid of the object
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
            return(r)
    else:
            return(0)

#determines which song has to be played based on the coordinates inputted
def song(r,x):
    if r!=0:
        for i in range(0,4):
            if r in range(list[i],(list[i+1])+1):
                a='{}'.format(x)+'{}.wav'.format(i+1)
        return a
    else:
         return('emp.wav')


#the main function where we decide which colours we want to detect
while 1:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    cnts1=selected_range(hsv,[29,86,6],[100,255,255])
   
    cnts2=selected_range(hsv,[29,86,6],[100,255,255])

    cnts3=selected_range(hsv,[0,100,100],[5,255,255])

    
     
    r1=0
    r2=0
    r3=0
      
    if cnts1 != [] :            
            r1=distance(cnts1)
    if cnts2 != []:            
            r2=distance(cnts2)
    if cnts3 != [] :
            r3=distance(cnts3)
    

    
    
    
           
    change_music(r1)

    
    cv2.imshow('frame', frame)
    
    
    if cv2.waitKey(1)==27:  #press escape to exit
        break



cv2.destroyAllWindows()
cap.release()


    
