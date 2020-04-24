import numpy as np
import cv2

# loads image
img = cv2.imread('top.jpeg')

# converts to grascale for countours
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# converts to color for color detection
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#finds edges
edges = cv2.Canny(img,50,150)
# finds contours, IDK what Hierarchy is
contours,hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# res is list with centroid data and color data in the the form of ( x centroid pont, y centroid point, Color(first letter)
res = []
for cnt in contours:
    #filters out shapes with low size
    if cv2.contourArea(cnt) > 100:
    	# Postion of top left corner + width and height
        x,y,w,h = cv2.boundingRect(cnt)
        # Calculates centroid data
        cx,cy = x+w/2, y+h/2
        cx = int(cx)
        cy = int(cy)
	# Sets number for each shape based on color
        color = hsv[cy,cx,0]
	# filters each shape and number given by hsv to find color and appends it to res
        if (color < 10 or color > 170):
            res.append([cx,cy,'R'])
        elif(50 < color < 70):
            res.append([cx,cy,'G'])
        elif(20 < color <40):
            res.append([cx,cy,'Y'])
        elif(110 < color < 130):
            res.append([cx,cy,'B'])

# I believe this sorts the res list but only by x centroid data only 
res = sorted(res,key = lambda res : res[0])
# prints x[2] portion of res list which is Color
colors = [x[2] for x in res]
print (colors)
