import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def selected_range(hsv,a,b):
        lower_green = np.array(a)
        upper_green = np.array(b)
        mask = cv2.inRange(hsv, lower_green, upper_green)
        kernel = np.ones((5, 5))
        grad = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cnts = cv2.findContours(grad.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return cnts

while 1:
    ret, frame = cap.read()


    hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cnts1=selected_range(hsv1,[29,86,6],[100,255,255])
   
    cnts2=selected_range(hsv1,[0,100,100],[5,255,255])

     
     
      
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

    cv2.imshow('frame', frame)
    
    
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()


        
