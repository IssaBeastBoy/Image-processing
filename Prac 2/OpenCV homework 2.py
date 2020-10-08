import cv2
import numpy as np

#Task 1: Placing my face on a status 

color = cv2.imread('Me.jpg')
color = cv2.resize(color,None, fx=0.1, fy=0.1)
background = cv2.imread('philo.jpg')
background = cv2.resize(background, (313, 221))
grayscale = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(grayscale, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

thinking = cv2.bitwise_and(background, background, mask=mask)
me_Me = cv2.bitwise_and(color, color, mask=mask_inv )

output = cv2.add(thinking,me_Me)

cv2.imshow('Me', color)
cv2.imshow('Philo', background)
cv2.imshow('Output', output)


cv2.waitKey(0)
cv2.destroyAllWindows()

#Task 2: Adding edge detection and some filtering

draw = cv2.imread('Draw.jpg')
draw = cv2.resize(draw,None, fx=0.1, fy=0.1)
gray = cv2.cvtColor(draw, cv2.COLOR_BGR2GRAY)
De_noise = cv2.fastNlMeansDenoising(gray, None, 5, 7, 21)
edge = cv2.Canny(De_noise, 70, 100)

cv2.imshow('original', draw)
cv2.imshow('Denoised', De_noise)
cv2.imshow('edge', edge)


cv2.waitKey(0)
cv2.destroyAllWindows()

#Teask 3: Dynamic edge detaction modification

def editImage(position):
    pos = position

cv2.namedWindow('post')
##cv2.namedWindow('edited')
cv2.createTrackbar('Min', 'post', 0, 255, editImage)
cv2.createTrackbar('Max', 'post', 0, 255, editImage)

while True:
    draw = cv2.imread('Draw.jpg')
    draw = cv2.resize(draw,None, fx=0.1, fy=0.1)
    gray = cv2.cvtColor(draw, cv2.COLOR_BGR2GRAY)
    gray  = cv2.medianBlur(gray,9)    
    cv2.imshow('post', edge)    
    posMin = cv2.getTrackbarPos('Min', 'post')
    posMax = cv2.getTrackbarPos('Max', 'post')
    edge = cv2.Canny(De_noise, posMin, posMax)
    escape = cv2.waitKey(1) & 0xFF
    
    if escape == 27:
        break
    

##    cv2.imshow('post', edited)
    
cv2.destroyAllWindows()
