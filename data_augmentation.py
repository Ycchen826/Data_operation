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
#   

    image = cv2.cvtColor(cv2.imread('F:\Cam2.jpg',-1), cv2.COLOR_BGR2RGB) 
    image1 = cv2.cvtColor(cv2.imread('F:\Cam3.jpg',-1), cv2.COLOR_BGR2RGB) 
#    img = cv2.imread('F:\Cam2.jpg')
#    img1=cv2.imread('F:\Cam3.jpg')
    size1=image.shape
    print(size1)
    size2=image1.shape
    print(size2)
    cv2.imwrite('F:\cam4.jpg',cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
##    print(img[2000][4000][1])
#    cv2.imshow('src',img)
#    cv2.waitKey(0)
#    img = Img.open('F:\Cam2.jpg')
#    print (img.size)
#    print (img.size[0])
#    img.show
 
    
#    img1 = gamma_trans(img, 0.5)
#    img2 = gamma_trans(img, 1.5)
#
#    
#    cv2.imshow('gamma=0.5',img1)
#    cv2.imshow('gamma=1.5',img2)
#    cv2.waitKey(0)
    

augmentation()