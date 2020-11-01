import cv2
import numpy as np
import imutils

video = cv2.VideoCapture('video.MOV')

ret, face = video.read()
face = imutils.rotate(face, 180)
roi = face[300:600, 700:1030]
roi_nose = face[445:480, 800:900]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [256], [11, 256])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

hsv_roiNose = cv2.cvtColor(roi_nose, cv2.COLOR_BGR2HSV)
roi_histNose = cv2.calcHist([hsv_roiNose], [0], None, [256], [11, 256])
roi_histNose = cv2.normalize(roi_histNose, roi_hist, 0, 255, cv2.NORM_MINMAX)

term = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

Haar_cascadeEyes = cv2.CascadeClassifier('haarcascade_eye.xml')
Haar_cascadeFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Haar_cascadeLEyes = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')


while True:
    ret, frame = video.read()

    if ret == False:
        video = cv2.VideoCapture('video.MOV')
        ret, frame = video.read()
    
    frame = imutils.rotate(frame, 180)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.calcBackProject([hsv], [0], roi_hist, [5, 230], 1)
    ret, track_Face = cv2.CamShift(mask, (920, 200, 745, 400), term)
    points = cv2.boxPoints(ret)
    points = np.int0(points)
    cv2.polylines(frame, [points], True, (0,255,0), 2)

    face = Haar_cascadeFace.detectMultiScale(hsv, 1.3, 5)
    for (x,y,w,h) in face:
        roi_HSV = hsv[y:y+h, x:x+w]
        roi = frame[y:y+h, x:x+w]
        eyes = Haar_cascadeEyes.detectMultiScale(roi_HSV, 1.3, 5)
        for (Eyes_x, Eyes_y, Eyes_w, Eyes_h) in eyes:
            cv2.rectangle(roi, (Eyes_x, Eyes_y), (Eyes_x + Eyes_w, Eyes_y + Eyes_h), (0, 255, 0), 2)
            
            mouthHSV_roi = cv2.calcHist([hsv], [0], None, [256], [11, 256])

            skin = cv2.calcBackProject([hsv], [0], roi_histNose, [5, 230], 1)
            ret, track_Mouth = cv2.CamShift(skin, (445, 800, 35, 100), term)
            points = cv2.boxPoints(ret)
            points = np.int0(points)
            cv2.polylines(skin, [points], True, (0,255,0), 2)

    cv2.imshow('Skin', skin)
    cv2.imshow('Thulani features', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
video.release()
cv2.destroyAllWindows()