# importing the required libraries. The functions
#of the libraries are as follows

import cv2                          #the key python library used for image processing
import numpy as np                  #a numerical library with some useful functions. We have used a lot of array functions of this ibrary                         
import pygame

temp1 = 1000000
temp2 = 1000000
temp3 = 1000000

b1, b2, b3 = True,True,True           #boolean variables three for each of the blocks


songlen = 500                           # a random value. decides the duration given to a song if the region is not changed

count1, count2, count3 = 0, 0, 0      #counting variables three for each of the blocks

cap = cv2.VideoCapture(1)           #VideoCapture initiates the webcam

cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)                   #these two commands are used for displaying the videos
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN,             #captured by the webcam onto the full screen of the laptop
                      cv2.WINDOW_FULLSCREEN)





b = True
count = 0

# function that gives the co
# ntours of the colour we want to detect
def selected_range(hsv, a, b):
    lower_green = np.array(a)                           #stores the lower limit of the hsv value we want to detect
    upper_green = np.array(b)                           #stores the upper range of the hsv value that we want to detect
    mask = cv2.inRange(hsv, lower_green, upper_green)   #filters out the parts of the frame in the range specified by lower_green and upper_green

    
    kernel = np.ones((5, 5))                                                                           #these three commands together return the contours
    grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)                                              # of the parts of the image
    cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]               # filtered out

    return cnts

#decides which music to be played for the green block
def playmusic1(a1):
    pygame.mixer.init()
    ch1 = pygame.mixer.Channel(0)                                           #selects channel 0 for playing the song received
    a = pygame.mixer.Sound(r"C:\Users\SOUMYA\Desktop\{}".format(a1))        #variable a stores the sound to be played
    ch1.play(a)                                                             #plays the song in the alloted channel

#decides which music to be played for the red block
def playmusic2(a2):

    pygame.mixer.init()
    ch2 = pygame.mixer.Channel(1)                                           #selects channel 1 for playing the song received
    b = pygame.mixer.Sound(r"C:\Users\SOUMYA\Desktop\{}".format(a2))        #variable b stores the sound to be played
    ch2.play(b)                                                             #plays the song in the alloted channel

#decides which music to be played for the blue block
def playmusic3(a3):

    pygame.mixer.init()
    ch3 = pygame.mixer.Channel(2)                                           #selects channel 2 for playing the song received
    c = pygame.mixer.Sound(r"C:\Users\SOUMYA\Desktop\{}".format(a3))        #variable v stores the sound to be played
    ch3.play(c)                                                             #plays the song in the alloted channel


# returns  the coordinates of the approximate centroid of the object
def distance(cnts):
    cmax = max(cnts, key=cv2.contourArea)                  #selects the contour with the maximum area or the greatest coloured part out of a number of parts of the same colour
    x, y, w, h = cv2.boundingRect(cmax)                    
    if w * h > 1000:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)     #draws an enclosing rectangle for the contour of the block detected
        a = len(cmax)
        sum1 = [[0, 0]]
        for i in range(a):
            sum1 += cmax[i]
        avg = sum1 / a                                       
        b = int(avg[0][0])                                   #b stores the x coordinate of the centre of the contour located
        c = int((avg[0][1]))                                 #c stores the y coordinate of the centre of the contour located
        cv2.circle(frame, (b, c), 3, (0, 0, 255), 2)         #draws a circle depicting the centre of the block detected  
        r = (b - 240) * (b - 240) + (c - 320) * (c - 320)    #r stores the distance between the centre of the screen and the centre of contour detected
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


#decides which region the block being inspected is in        
def check(r1,temp1):

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
# the main function where we decide which0 colours we want to detect
while 1:
    ret, frame = cap.read()                                        #takes and stores the current photo of the video in the variable frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                   #converts the frame from RGB format into the hsv format

    cnts1 = selected_range(hsv, [29, 86, 6], [100, 255, 255])      #for getting the contours or the edges of the green block

    cnts2 = selected_range(hsv, [110, 50, 50], [130, 255, 255])    #for getting the contours or the edges of the red block

    cnts3 = selected_range(hsv, [0, 100, 100], [5, 255, 255])      #for getting the contours or the edges of the blue block

    r1 = 0                              #store the distance between the centre of the         
    r2 = 0                              #screen and the centre of the green, red and 
    r3 = 0                              #blue blocks respectively
    
    if cnts1 != []:                          #ensures that an empty contour for the green block is not sent as that would throw an error
        r1 = distance(cnts1)
    if cnts2 != []:                          #ensures that an empty contour for the red block is not sent as that would throw an error
        r2 = distance(cnts2)
    if cnts3 != []:                          #ensures that an empty contour for the blue block is not sent as that would throw an error
        r3 = distance(cnts3)
    
    
    if r1==0:                                     #these commands send an empty track
        playmusic1('empty.wav',0)                 #to be played if either of the green,
        temp1=1000000                             #red or blue
    if r2==0:                                     #blocks is not present
        playmusic2('empty.wav',1)                 #thus ensuring that no
        temp2=1000000                             #music is played if the 
    if r3==0:                                     #blocks are not on
        playmusic3('empty.wav',2)                 #the
        temp3=1000000                             #table

        
    if check(r1,temp1) or check(r2,temp2) or check(r3,temp3):

        a1 = song(r1, 'd')         #decides which song has to be played for the green block depending on its distance from the screen center
        a2 = song(r2, 'p')         #decides which song has to be played for the red block depending on its distance from the screen center 
        a3 = song(r3, 't')         #decides which song has to be played for the blue block depending on its distance from the screen center
        
        if check(r1,temp1):         
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
    cv2.imshow('frame', frame)     #responsible for displaying the frames with the bounding rectangles on the blocks

    if cv2.waitKey(1) == 27:       # press escape to exit
        break

cv2.destroyAllWindows()            #this command is self explanatory. destroys all the windows playing any video    
cap.release()                      #this command releases the webcam shutting it down
