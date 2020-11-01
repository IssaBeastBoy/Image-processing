import cv2

origin = cv2.VideoCapture(0)
frame = cv2.VideoCapture(0)
average = cv2.VideoCapture(0)

starter_Frame = 0
starter_average = 0

while(True):

    ret1, origin_frame = origin.read()
    ret2, frameD_frame = frame.read()
    ret3, average_frame = average.read()

    movement = frameD_frame - starter_frame
    starter_frame = movement
    
    if starter_average = 0:
        average = 0.05 * average_frame + (1 - 0.05) * average_frame
    else:
        average = 0.05 * average_frame + (1 - 0.05) * average
    starter_average = 1

    cv2.imshow('Original frames', origin_frame)
    cv2.imshow('Frame differencing', movement)
    cv2.imshow('Running average', average)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

background.release() 
frame.release() 
average.release() 
cv2.destroyAllWindows() 