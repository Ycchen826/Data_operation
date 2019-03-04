# -*- coding: utf-8 -*-
"""
@time:2019.02.28
@author: Cyc
"""
# 导入库
import numpy as np
import cv2
from  PIL import Image as Img

#伽马矫正
def gamma_trans(img, gamma):
    gamma_table = [np.power(x / 255.0, gamma)*255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    return cv2.LUT(img, gamma_table)

"""path_in和path_out都是路径名加文件名（含后缀）如F:\Cam1.png, rate是压缩的比率"""
def compress(path_in,path_out,rate):
        # 打开图片
        image = Img.open(path_in)
        # 图片另存到output文件夹中，图片质量压缩到60%
        image.save(path_out, quality=rate)

def augmentation():
    
    img = cv2.imread('F:\Cam1.png')
        
    cv2.imshow('src',img)
    
    
    img1 = gamma_trans(img, 0.5)
    img2 = gamma_trans(img, 1.5)

    
    cv2.imshow('gamma=0.5',img1)
    cv2.imshow('gamma=1.5',img2)
    cv2.waitKey(0)
    

augmentation()