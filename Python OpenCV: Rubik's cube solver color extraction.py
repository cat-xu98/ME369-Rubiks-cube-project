import cv2
import numpy as np
from imutils import contours

image = cv2.imread('test cube.jpg')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = np.zeros(image.shape, dtype=np.uint8)

colors = {
    'gray': ([76, 0, 41], [179, 255, 70]),        # Gray
    'blue': ([69, 120, 100], [179, 255, 255]),    # Blue
    'yellow': ([21, 110, 117], [45, 255, 255]),   # Yellow
    'orange': ([0, 110, 125], [17, 255, 255]),    # Orange
    'white': ([0, 0, 20], [180, 50, 255]),        # White
    'red1': ([0, 100, 20], [15, 255, 255]),       # Red1
    'red2': ([170, 200, 20], [180, 255, 255]),    # Red1
    'green': ([45, 100, 20], [70, 255, 255])      # Green
    }

# Color threshold to find the squares
open_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
for color, (lower, upper) in colors.items():
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    color_mask = cv2.inRange(image, lower, upper)
    color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, open_kernel, iterations=1)
    color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_CLOSE, close_kernel, iterations=5)

    color_mask = cv2.merge([color_mask, color_mask, color_mask])
    mask = cv2.bitwise_or(mask, color_mask)

gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

temp_list = list(cnts)
temp_list = [item for item in cnts if 8000 < cv2.contourArea(item) < 90000]
cnts = tuple(temp_list)
        
# Sort all contours from top-to-bottom or bottom-to-top
(cnts, _) = contours.sort_contours(cnts, method="top-to-bottom")

# Take each row of 3 and sort from left-to-right or right-to-left
cube_rows = []
row = []
for (i, c) in enumerate(cnts, 1):
    row.append(c)
    if i % 3 == 0:  
        (cnts, _) = contours.sort_contours(row, method="left-to-right")
        cube_rows.append(cnts)
        row = []

# Draw text
number = 0
res = []
for row in cube_rows:
    for c in row:
        x,y,w,h = cv2.boundingRect(c)
        cx,cy = x+w/2, y+h/2
        cx = int(cx)
        cy = int(cy)
        
        if w/h < 1.1 and h/w < 1.1: #checks that it is squarish
            cv2.rectangle(original, (x, y), (x + w, y + h), (36,255,12), 2)
    
            cv2.putText(original, "#{}".format(number + 1), (x,y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
            number += 1
            
            color = image[cy,cx,0]
            
            if (color < 12 or color > 160):
                res.append([cx,cy,'R'])
            elif (100 <= color < 160):
                res.append([cx,cy,'B'])
            elif (50 <= color < 100):
                res.append([cx,cy,'G'])
            elif (30 <= color < 50):
                res.append([cx,cy,'W'])
            elif (20 <= color < 30):
                res.append([cx,cy,'Y'])
            elif (12 <= color < 20):
                res.append([cx,cy,'O'])
            
colors = [x[2] for x in res]
print(colors)        
            
            
cv2.imshow('mask', mask)
cv2.imwrite('mask.png', mask)
cv2.imshow('original', original)
cv2.waitKey()
