#importing the required libraries

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

#global list variables that need to be used 
list=[0,6400,25600,57600,102400,160000,230400,313600,409600,518400,640000]
cnts=[]
a=[]
t=['a','g','c']

#function that gives the countours of the colour we want to detect

def selected_range(hsv,a,b):
        lower_green = np.array(a)
        upper_green = np.array(b)
        mask = cv2.inRange(hsv, lower_green, upper_green)
        kernel = np.ones((5, 5))
        grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return cnts
        
def playmusic(a):

         pygame.mixer.init()
         ch1=pygame.mixer.Channel(0)
         ch2=pygame.mixer.Channel(1)
         ch3=pygame.mixer.Channel(2)
         a=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\combinations\{}".format(a[0]))
         b=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\combinations\{}".format(a[1]))
         c=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\combinations\{}".format(a[2]))
         ch1.play(a)
         ch2.play(b)
         ch3.play(c)
         
#returns  the coordinates of the approximate centroid of the object
def distance(cnts):
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
    r=(b-240)*(b-240) + (c-320)*(c-320)
    return(r)

#determines which song has to be played based on the coordinates inputted
def song(r,x):
    if r!=0:
        for i in range(0,10):
            if r in range(list[i],(list[i+1])+1):
                a='{}'.format(x)+'{}.wav'.format(i+1)
        return a
    else:
         return('emp.wav')


#the main function where we decide whic colours we want to detect
while 1:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    cnts.append(selected_range(hsv,[29,86,6],[100,255,255]))
   
    cnts.append(selected_range(hsv,[0,100,100],[5,255,255]))

    cnts.append(selected_range(hsv,[110,50,50],[130,255,255]))

    
     
    r=[0,0,0]
      
    for i in range(0,3):
        if cnts[i] != []:
            r[i]=distance(cnts[i])
    

    
    for i in range(0,3):
        a.append(song(r[i],t[i]))
    
           
    playmusic(a)       
    cv2.imshow('frame', frame)
    
    
    if cv2.waitKey(1)==27:  #press escape to exit
        break



cv2.destroyAllWindows()


    
