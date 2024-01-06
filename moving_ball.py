import cv2

cap=cv2.VideoCapture(0)

cx=10.0
cy=10.0

while True:
    ret,frame=cap.read()
    h,w,d=frame.shape
    print('rows ',h,'columns ',w)
    cv2.circle(frame,(int(cx),int(cy)),3,(255,0,255),-1)
    cx=cx+2
    cy=cy+1
    cv2.imshow('game',frame)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
