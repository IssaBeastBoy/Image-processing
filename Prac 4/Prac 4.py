import cv2
import argparse
import numpy as np


#Task 1: Applying features on video stream
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,680))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray  = cv2.Canny(gray, 100, 100)
    out.write(frame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
out.release()
cv2.destroyAllWindows()

#Task 2: Drawing shapes on an image
FindItems = cv2.imread('Find.jpg')
copy = FindItems.copy()
FoundItem = cv2.imread('Found.png')
cv2.namedWindow('Find')
store_Postions = []

def click_draw(event, x, y, flags, param):
    
    global store_Postions
    
    if event == cv2.EVENT_LBUTTONDOWN:
        store_Postions = [(x, y)]

    elif event ==  cv2.EVENT_LBUTTONUP:
        store_Postions.append((x,y))
        cv2.rectangle(FindItems, store_Postions[0], store_Postions[1], (0,0,255), 2)
        cv2.imshow('Find', FindItems)
        store_Postions = []
    
cv2.setMouseCallback('Find', click_draw)


while True:
    
    cv2.imshow('Find', FindItems)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cv2.imshow('items', FoundItem)
        break

cv2.waitKey(8000)
cv2.destroyAllWindows()
