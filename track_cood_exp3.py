import cv2
import numpy as np
import pyautogui as p

cap=cv2.VideoCapture(0)
r,img=cap.read()
cap.release()
cv2.destroyAllWindows()

ROI=[]
for x in range(1,631,10):
    for y in range(1,471,10):
        ROI.append(img[x:x+10,y:y+10])



cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([29, 86, 6])
    upper_green = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    kernel = np.ones((5, 5))
    grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
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

    for x in range(1,621,20):
        for y in range(1,461,20):
             if b in range(x,x+20) and c in range(y,y+20):
                b=x+10
                c=y+10
                
    cv2.circle(frame,(b,c),5,(255,0,0),1)        
        
            
    
    cv2.imshow('frame', frame)
   
    
   
    

    if cv2.waitKey(1)==27:
        break





cv2.destroyAllWindows()
