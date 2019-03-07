# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:34:39 2019

@author: Administrator
"""
# 导入库
import cv2
import os
import numpy as np
import random
import operator
#遍历主文件夹下所有的文件名,返回文件名称
def get_all_fileName(path):
    pathDir = os.listdir(path)

    file_name=[]
    for allDir in pathDir:
        if '.DS_Store' not in allDir:
            camid = os.path.join('%s' % allDir)
            file_name.append(camid)
    # print(child)
    return file_name
#遍历主文件夹下所有的文件名,返回文件夹的路径
def get_all_filePath(path):
    pathDir = os.listdir(path)
    dir=[]
    for allDir in pathDir:
        if '.DS_Store' not in allDir:
            child = os.path.join('%s/%s' % (path,allDir))
            dir.append(child)
    # print(child)
    return dir

def contour(path1,path2):
    
    filelist = os.listdir(path1)  #获取文件下的所有文件名
    count=0
    for i in range(0,len(filelist)):
        
        Olddir = path1 + filelist[i]  #原来的文件路径
        if os.path.isdir(Olddir):  #如果是文件夹则跳过
            continue
   
        img =cv2.imread(Olddir)   
        img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,binary = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)
        #先将图像转化成灰度，再转化成二值图像
        binary=255-binary
        contours, hierarchy=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #检测边缘
    
        for c in contours:
            x,y,w,h = cv2.boundingRect(c)
            #用一个最小的矩形，把找到的形状包起来
            #返回(x,y)为矩形左上角坐标，w,h分别是宽和高
            out_img=img[y:y+h,x:x+w]
            cv2.imwrite(path2+filelist[i],out_img)
    
def rename(path1,path2):   #对文件重命名
     
    filelist = os.listdir(path1)  #获取文件下的所有文件名
    count=0
    for i in range(0,len(filelist)):
        
        Olddir = path1 + filelist[i]  #原来的文件路径
        if os.path.isdir(Olddir):  #如果是文件夹则跳过
            continue
#        filename = os.path.splitext(filelist[i])[0] #文件名
#        filetype = os.path.splitext(filelist[i])[1] #后缀名,是一个列表
        
#        if(filetype=='.bmp'):
        img=cv2.imread(Olddir) 
        cv2.imwrite(path2+str(count)+'.png',img)
        count=count+1

def splice(main_image,splice_image,mask1, init_px, init_py, main_px, main_py):
    #白色是要提取的区域
   
    mask = cv2.split(mask1)[0]
    mask_rows,mask_cols = mask.shape
   
    splice_roi = splice_image[init_px:(init_px + mask_rows) , init_py:(init_py + mask_cols)]
    main_roi=main_image[main_px:(main_px + mask_rows) , main_py:(main_py + mask_cols)]
    
    mask_inv = cv2.bitwise_not(mask)
    
    print(splice_roi.shape)
    print(main_roi.shape)
    print(mask.shape)
#    cv2.imshow('splice',splice_roi)
#    cv2.imshow('main',main_roi)
#    cv2.imshow('mask',mask)
#    cv2.imshow('mask_inv',mask_inv)
#    cv2.waitKey(0)
    
    
    splice_block = cv2.bitwise_and(splice_roi,splice_roi,mask=mask)
    main_block=cv2.bitwise_and(main_roi,main_roi,mask=mask_inv)
    
    dst = cv2.add(main_block,splice_block)
    main_image[main_px:main_px + mask_rows , main_py:main_py + mask_cols] = dst
    
    return main_image
    
    
if __name__ == '__main__':
    
    #需要生成mask图的图像文件路径
    dir_path='F:/rowdata/sp-society-camera-model-identification/train'
    #纯颜色掩膜的路径
    picmask_path='E:/data/camera_verification_data/sp2018mask/'
    #二值掩膜的路径
    mask_path='E:/data/cocomask/splicemask'
    #输出路径
    out_img_path='E:/data/camera_verification_data/splice/'
    out_mask_path='E:/data/camera_verification_data/splice_mask/'
    
    dir_file=get_all_fileName(dir_path)
        
    for cam_id in dir_file:
        """cam_id保存了相机型号，image_path保存了各个图像的路径"""
        image_dir=dir_path+'/'+cam_id  
        image_path=get_all_filePath(image_dir)
        image_name=get_all_fileName(image_dir)
        
        for t in range(0,274):
            main_image=cv2.cvtColor(cv2.imread(image_path[t],-1), cv2.COLOR_BGR2RGB)
#        main_mask=cv2.imread(picmask_path+image_name[t])
        
            for ref_cam in dir_file:
                if(operator.eq(cam_id,ref_cam)==False):
                    main_image=cv2.cvtColor(cv2.imread(image_path[t],-1), cv2.COLOR_BGR2RGB)
                    main_mask=cv2.cvtColor(cv2.imread(picmask_path+image_name[t],-1), cv2.COLOR_BGR2RGB)
                    print(picmask_path+image_name[t])
                    refimage_dir=dir_path+'/'+ref_cam  
                    refimage_path=get_all_filePath(refimage_dir)
                    refimage_name=get_all_fileName(refimage_dir)
                    rt=random.randint(0,274)
                    """splice image的读入"""
                    splice_image=cv2.cvtColor(cv2.imread(refimage_path[rt],-1), cv2.COLOR_BGR2RGB)
                    splice_mask=cv2.cvtColor(cv2.imread(picmask_path+refimage_name[rt],-1), cv2.COLOR_BGR2RGB)
            
                    """mask的读入"""
                    mt=random.randint(0,3372)
                    realmask_path=get_all_filePath(mask_path)
                    mask=cv2.imread(realmask_path[mt])
                    
                    mask_row,mask_col,channels = mask.shape
                    splice_rows,splice_cols,channels = splice_image.shape
                    main_rows,main_cols,channels = main_image.shape
                    
                    rate_row=min(splice_rows//mask_row,main_rows//mask_row)
                    rate_col=min(splice_cols//mask_col,main_cols//mask_col)
                    rate=min(rate_row,rate_col)
                    size_rate=random.randint(max(1,rate//4),max(1,rate//2))
                    
#                    print(rate_row,rate_col,rate,size_rate)
                    
                    mask_rows=mask_row*size_rate
                    mask_cols=mask_col*size_rate
                    size=(int(mask_cols),int(mask_rows))
        #                cv2.imshow('1',mask)
                   
                    mask1 = cv2.resize(mask,size, interpolation=cv2.INTER_NEAREST)
        #                cv2.imshow('2',mask1)
                    
                    t1=max(mask_cols,mask_rows)
                    
                    init_px=random.randint(10,splice_rows-t1-10)
                    init_py=random.randint(10,splice_cols-t1-10)
                    main_px=random.randint(10,main_rows-t1-10)
                    main_py=random.randint(10,main_cols-t1-10)
#                    init_px=splice_rows//2
#                    init_py=splice_cols//2
#                    main_px=main_rows//2
#                    main_py=main_cols//2
        #                print(mask_row-init_px-mask_rows)
                   
#                    cv2.imshow('1',main_mask)
#                 
#                    cv2.imshow('2',splice_mask)
#                    cv2.waitKey(0)
                    result_img=splice(main_image,splice_image,mask1,init_px, init_py, main_px, main_py)
                    result_mask=splice(main_mask,splice_mask,mask1,init_px, init_py, main_px, main_py)
                    
                    img_str=os.path.splitext(image_name[t])[0]+refimage_name[rt]
                    mask_str=os.path.splitext(image_name[t])[0]+refimage_name[rt]
                    
                    cv2.imwrite(out_img_path+img_str,cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR))
                    cv2.imwrite(out_mask_path+mask_str,cv2.cvtColor(result_mask, cv2.COLOR_RGB2BGR))
                    
                    
                
                
                