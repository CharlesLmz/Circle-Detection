# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:06:52 2020

@author: Charles Lee
"""

import cv2
import numpy as np
import math
import sys
from time import time

start = time()
def seg_circle(img):
    h, w = img.shape[:2]
    result = np.zeros([h, w, 3])
    circles = detect_circle(img)
    print("圆心：", circles[0][0], circles[0][1])
    print("半径：", circles[0][2])
    time2 = time()
    print(time2-time1)
    
    # for i in range(w):
    #     for j in range(h):
    #         if distance(i, j, circles[0][1], circles[0][0]) < circles[0][2]:
    #             result[i][j][:] = img[i][j][:]
    cv2.circle(img,(circles[0][0],circles[0][1]),circles[0][2],(0,255,0),2)
    time3 = time()
    print(time3-time2)

    # cv2.imwrite('result.jpg', img)
    time4 = time()
    print(time4-time3)
    print('图片输出完成')

def detect_circle(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
    circles1 = cv2.HoughCircles(gaussian, cv2.HOUGH_GRADIENT, 1, 100, param1=200, param2=30, minRadius=0, maxRadius=0)
    try:
        circles = circles1[0, :, :]
    except:
        print('detect_circle 未检测到圆形')
        sys.exit()
    circles = np.uint16(np.around(circles))
    return circles

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1 - y2)**2)

while 1:
    cap=cv2.VideoCapture(0)
    sucess,img=cap.read()
    # img = cv2.imread('bigcircle2.jpg')
    time1 = time()
    seg_circle(img)
    end = time()
    # print('运行时间：',end-start)