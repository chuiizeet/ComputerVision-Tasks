import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),10)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)

img = cv2.imread('dog_backpack.jpg')

while True:
    cv2.imshow('my_drawing',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()