# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:34:39 2019

@author: Administrator
"""

   

# 导入库
import numpy as np
import argparse
import cv2
 
def rename(path):
    
    # 加载猫的图像
    image = cv2.imread('cam2.png')
    cv2.imshow("Cat", image)
     
    mask1=cv2.imread('mask.png')
    mask1=255-mask1
    r,g,b=cv2.split(mask1)
     
    mask = r
    cv2.imshow("Mask", mask)
     
    # Apply out mask -- notice how only the person in the image is cropped out
    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.imwrite('cammask111.png',masked)
    cv2.waitKey(0)



def gamma():
    
    img = cv2.imread('gamma0.jpg',0)
    
    img1 = np.power(img/float(np.max(img)), 1/1.5)
    img2 = np.power(img/float(np.max(img)), 1.5)
    
    cv2.imshow('src',img)
    cv2.imshow('gamma=1/1.5',img1)
    cv2.imshow('gamma=1.5',img2)
    cv2.waitKey(0)

#rename('F:/数据操作代码/2019.02.26/')