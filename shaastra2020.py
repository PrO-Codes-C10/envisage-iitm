# importing the required libraries

import cv2
import numpy as np
import pyglet
import time
import pygame
import pyautogui
import os
temp1 = 1000000
temp2 = 1000000
temp3 = 1000000
b1, b2, b3 = True,True,True
songlen = 500
count1, count2, count3 = 0, 0, 0
cap = cv2.VideoCapture(0)

cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)

list = [0, 6400, 25600, 57600, 102400, 160000, 230400, 313600, 409600, 518400, 640000]


# function that gives the co
# ntours of the colour we want to detect
b = True
count = 0

def selected_range(hsv, a, b):
    lower_green = np.array(a)
    upper_green = np.array(b)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    kernel = np.ones((5, 5))
    grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    return cnts


def playmusic1(a1,x):
    #print(a1)
    pygame.mixer.init()
    ch1 = pygame.mixer.Channel(x)
    #s = r"C:\Users\SOUMYA\Desktop\emp.wav"
    #a = pygame.mixer.Sound(s)
    a = pygame.mixer.Sound(r"C:\Users\SOUMYA\Desktop\{}".format(a1))
    ch1.play(a)

def playmusic2(a2):

    pygame.mixer.init()
    ch2 = pygame.mixer.Channel(1)
    b = pygame.mixer.Sound(r"C:\Users\SOUMYA\Desktop\{}".format(a2))
    ch2.play(b)

def playmusic3(a3):

    pygame.mixer.init()
    ch3 = pygame.mixer.Channel(2)
    c = pygame.mixer.Sound(r"C:\Users\SOUMYA\Desktop\{}".format(a3))
    ch3.play(c)



# returns  the coordinates of the approximate centroid of the object
def distance(cnts):
    cmax = max(cnts, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(cmax)
    if w * h > 1000:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        a = len(cmax)
        sum1 = [[0, 0]]
        for i in range(a):
            sum1 += cmax[i]
        avg = sum1 / a
        b = int(avg[0][0])
        c = int((avg[0][1]))
        cv2.circle(frame, (b, c), 3, (0, 0, 255), 2)
        r = (b - 240) * (b - 240) + (c - 320) * (c - 320)
        return (r)
    else:
        return (0)


# determines which song has to be played based on the coordinates inputted
def song(r, x):
    if r==0:
        return "empty.wav"
    if r<15000:
        i=1
    if 15000<r<30000:
        i=2
    if r>30000:
        i=3
    return "{}{}.wav".format(x,i)

def bul(b,count,songlen,a):

    if b:
        playmusic1(a)
    b = False
    count = count + 1
    if count > songlen:
        b = True
        count = 0
def check(r1,temp1):
    #print(f'{r1} {temp1} asdhfg')
    if r1 <15000:
        if temp1<15000:
            return False
        else:
            return True
    elif 15000<r1<30000:
        if 15000<temp1<30000:
            return False
        else:
            return True
    elif 30000<r1:
        if 200000>temp1>30000:
            return False
        else:
            return True
# the main function where we decide which colours we want to detect
while 1:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cnts1 = selected_range(hsv, [29, 86, 6], [100, 255, 255])

    cnts2 = selected_range(hsv, [110, 50, 50], [130, 255, 255])

    cnts3 = selected_range(hsv, [0, 100, 100], [5, 255, 255])
    r1 = 0
    r2 = 0
    r3 = 0
    if cnts1 != []:
        r1 = distance(cnts1)
    if cnts2 != []:
        r2 = distance(cnts2)
    if cnts3 != []:
        r3 = distance(cnts3)
    print(f"{temp1} {temp2} {temp3} {r1} {r2} {r3}")
    #print(f'{r1} {r2} {r3}')
    if r1==0:
        playmusic1('empty.wav',0)
        temp1=1000000
    if r2==0:
        playmusic1('empty.wav',1)
        temp2=1000000
    if r3==0:
        playmusic1('empty.wav',2)
        temp3=1000000
    if check(r1,temp1) or check(r2,temp2) or check(r3,temp3):

        a1 = song(r1, 'd')
        a2 = song(r2, 'p')
        a3 = song(r3, 't')
        #print(f"{b1} {b2} {b3}")
        if check(r1,temp1):
            #print("asdrfghjytrewasdgfhgfdrseasfdgh")
            b1 = True
            count1=0
        if check(r2,temp2):
            b2 = True
            count2=0
        if check(r3,temp3):
            b3 = True
            count3=0
        if b1:
            playmusic1(a1,0)
        b1 = False
        count1 = count1 + 1
        if count1 > songlen:
            b1 = True
            count1 = 0
        if b2:
            playmusic1(a2,1)
        b2 = False
        count2 = count2 + 1
        if count2 > songlen:
            b2 = True
            count2 = 0
        if b3:
            playmusic1(a3,2)
        b3 = False
        count3 = count3 + 1
        if count3 > songlen:
            b3 = True
            count3 = 0
        temp1=r1
        temp2=r2
        temp3=r3
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:  # press escape to exit
        break

cv2.destroyAllWindows()
cap.release()
