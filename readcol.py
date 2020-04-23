#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:46:36 2020

@author: catherinexu
"""

import cv2
import numpy as np

img = cv2.imread('top.jpeg')


grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grayscale, (3, 3), 0)
canny = cv2.Canny(blurred, 20, 40)
kernel = np.ones((3,3), np.uint8)
dilated = cv2.dilate(canny, kernel, iterations=2)

(contours, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow('image',dilated)
#cv2.waitKey(0)

cv2.destroyAllWindows()

