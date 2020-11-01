import cv2
import numpy as np

original = cv2.imread('Sexy.jpg')
row= int(original.shape[0] *0.25)
cols = int(original.shape[1] * 0.15)
new_Size = (row, cols)
reSize = cv2.resize(original, new_Size, interpolation= cv2.INTER_AREA)
gray = cv2.cvtColor(reSize, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)


row, cols = threshold.shape
pixel_row = 0
new_RowOne = []
new_RowTwo = []
number = 1
white = [255, 255, 255]
black = [1, 1, 1]
while pixel_row < row:
    new_Col1_One = []
    new_Col1_Two = []
    new_Col2_One = []
    new_Col2_Two = []
    pixel_col = 0
    while pixel_col < cols:
        if threshold[pixel_row, pixel_col] == 255:
            if number == 1:
                number = 0
                new_Col1_One.append(1)
                new_Col1_Two.append(255)
                new_Col2_One.append(255)
                new_Col2_Two.append(1)
            else:
                number = 1
                new_Col1_One.append(255)
                new_Col1_Two.append(1)
                new_Col2_One.append(1)
                new_Col2_Two.append(255)

        if threshold[pixel_row, pixel_col] == 1 or threshold[pixel_row, pixel_col] == 0:
            if number == 1:
                number = 0
                new_Col1_One.append(255)
                new_Col1_Two.append(1)
                new_Col2_One.append(1)
                new_Col2_Two.append(255)
            else:
                number = 1
                new_Col1_One.append(1)
                new_Col1_Two.append(255)
                new_Col2_One.append(255)
                new_Col2_Two.append(1)

        pixel_col = pixel_col + 1
    new_RowOne.append(new_Col1_One)
    new_RowTwo.append(new_Col2_One)
    new_RowOne.append(new_Col1_Two)
    new_RowTwo.append(new_Col2_Two)
    pixel_row = pixel_row + 1

print(threshold)
print()
print(new_RowTwo)
print()

while True:
    cv2.imshow('Original', reSize)
    cv2.imshow('Image one', new_RowOne)
    cv2.imshow('Image two', new_RowTwo)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
        

cv2.destroyAllWindows()