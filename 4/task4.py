"""
Create a program that reads in a live stream from a camera on your computer. Then whenever you click the left mouse button down, create a blue circle aroynd wgere you've clicked.
"""

import cv2

def draw_circle(event,x,y,flags,params):
    
    global center, clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        #Reset
        if clicked == True:
            clicked = False
            center = (0,0)
            
        if clicked == False:
            center = (x,y)
            clicked = True


center = (0,0)
clicked = False

cap = cv2.VideoCapture(0)
cv2.namedWindow('Draw_circle')
cv2.setMouseCallback('Draw_circle', draw_circle)

while True:

    ret, frame = cap.read()

    if clicked:
        cv2.circle(frame,
                   center=center,
                   radius=50,
                   color=(255,0,0),
                   thickness=3)


    cv2.imshow('Draw_circle', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
