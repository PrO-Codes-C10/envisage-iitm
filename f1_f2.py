from threading import Thread



import cv2
import numpy as np
import pyglet
import time
import pygame
import pyautogui
import os


def c1():
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)     

    def selected_range(a,b):
            lower_green = np.array(a)
            upper_green = np.array(b)
            mask = cv2.inRange(hsv, lower_green, upper_green)
            kernel = np.ones((5, 5))
            grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            return cnts
            
    def playmusic(a):
        
             pygame.mixer.init()

             pygame.mixer.music.load(r"C:\users\utkarsh kumar\desktop\envisage\{}".format(a))

             pygame.mixer.music.play()

    while 1:
        ret, frame = cap.read()


        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cnts=selected_range([29,86,6],[100,255,255])
        
        

            
            
        if cnts != []:            
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
                if r < 300:


                   playmusic('d1.mp3')

                   
                if r < 22000:
                   
                   playmusic('d2.mp3') 

                if 22000 < r < 44000:

                    playmusic('d3.mp3')

                if 44000 < r < 66000:

                    playmusic('d4.mp3')
                    
                if 66000 < r < 88000:

                    playmusic('d5.mp3')

                if  88000 < r < 110000:

                    playmusic('d6.mp3')
                    
                if r > 110000:

                    playmusic('d7.mp3')
                    
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1)==27:
            break



    cv2.destroyAllWindows()


        




def c2():
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("fram", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("fram", cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)     

    def selected_range(a,b):
            lower_green = np.array(a)
            upper_green = np.array(b)
            mask = cv2.inRange(hsv, lower_green, upper_green)
            kernel = np.ones((5, 5))
            grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            return cnts
            
    def playmusic(a):
        
             pygame.mixer.init()

             pygame.mixer.music.load(r"C:\users\utkarsh kumar\desktop\envisage\{}".format(a))

             pygame.mixer.music.play()

    while 1:
        ret, fram = cap.read()


        hsv = cv2.cvtColor(fram, cv2.COLOR_BGR2HSV)

        cnts=selected_range([0,100,100],[5,255,255])
        
        

            
            
        if cnts != []:            
                cmax = max(cnts, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(cmax)
                cv2.rectangle(fram, (x, y), (x + w, y + h), (0, 0, 255), 3)
                a = len(cmax)
                sum1 = [[0, 0]]
                for i in range(a):
                    sum1 += cmax[i]

                avg = sum1 / a
                b = int(avg[0][0])
                c = int((avg[0][1]))
                cv2.circle(fram, (b, c), 3, (0, 0, 255), 2)
               
                r=(b-240)*(b-240) + (c-320)*(c-320)
                if r < 300:


                   playmusic('a1.mpeg')

                   
                if r < 22000:
                   
                   playmusic('a2.mpeg') 

                if 22000 < r < 44000:

                    playmusic('a3.mpeg')

                if 44000 < r < 66000:

                    playmusic('a4.mpeg')
                    
                if 66000 < r < 88000:

                    playmusic('a5.mpeg')

                if  88000 < r < 110000:

                    playmusic('a6.mpeg')
                    
                if r > 110000:

                    playmusic('a7.mpeg')
                    
        cv2.imshow('fram', fram)
        
        if cv2.waitKey(1)==27:
            break



    cv2.destroyAllWindows()


    

    
Thread(target=c1).start()   
Thread(target=c2).start() 
