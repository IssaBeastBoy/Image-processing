import cv2
import numpy as np

#Task 1: Using erosion and dilation
 
##color = cv2.imread('Me.png')
originalImg = color.copy()
erode = color.copy()

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(erode, kernel, iterations=1)
dilate = cv2.dilate(color, kernel, iterations=1)



cv2.imshow('Original', originalImg)
cv2.imshow('Dilated Image', dilate)
cv2.imshow('Eroded Image', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Task 2: The solar system
solarS = cv2.imread('space.jpg')
originalImg = solarS.copy()
gray = cv2.cvtColor(solarS, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5), np.uint8)
copy = cv2.erode(gray, kernel, iterations=1)

planets = cv2.HoughCircles(copy, cv2.HOUGH_GRADIENT, 20, 10,minRadius=5, maxRadius=22)

amount = 0
for planet in planets[0,:]:
    cv2.circle(solarS, (planet[0],planet[1]),planet[2], (0,255,0),2)
    amount = amount + 1

print(amount)

cv2.imshow('Original', originalImg)
cv2.imshow('All the planets + MoonSun', solarS)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Task 3 = Finding charmander
beachDay = cv2.imread('pokemon.png')
grey = cv2.cvtColor(beachDay, cv2.COLOR_BGR2GRAY)
charmander = cv2.imread('charmanderEyes.png')
template =  cv2.cvtColor(charmander, cv2.COLOR_BGR2GRAY)

position = cv2.matchTemplate(grey, template, cv2.TM_CCOEFF_NORMED)
minVal, maxVal, minCoord, maxCoord = cv2.minMaxLoc(position)

H,W=template.shape
cv2.rectangle(beachDay, maxCoord,(maxCoord[0]+W,maxCoord[1]+H+300), (255,0,0), 2)
cv2.putText(beachDay, f'Charmander Eyes: {int(maxVal*100)}%', (maxCoord[0],maxCoord[1]-5), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,0,0))

cv2.imshow('charmanderEyes', beachDay)
cv2.waitKey(0)
cv2.destroyAllWindows()
