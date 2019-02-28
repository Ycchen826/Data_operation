# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:34:39 2019

@author: Administrator
"""
# 导入库
import numpy as np
import csv
import os
import operator

def get_label_info(csv_path):
    """
    Retrieve the class names and label values for the selected dataset.
    Must be in CSV format!

    # Arguments
        csv_path: The file path of the class dictionairy
        
    # Returns
        Two lists: one for the class names and the other for the label values
    """
    filename, file_extension = os.path.splitext(csv_path)
    if not file_extension == ".csv":
        return ValueError("File is not a CSV!")

    class_names = []
    label_values = []
    with open(csv_path, 'r') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        header = next(file_reader)
        for row in file_reader:
            class_names.append(row[0])
            label_values.append([int(row[1]), int(row[2]), int(row[3])])
        # print(class_dict)
    return class_names, label_values


#遍历主文件夹下所有的文件名,返回文件夹的路径,和文件名称
def get_all_fileName(path):
    pathDir = os.listdir(path)
    cam_path=[]
    cam_id=[]
    for allDir in pathDir:
        if '.DS_Store' not in allDir:
            child = os.path.join('%s/%s' % (path,allDir))
            camid = os.path.join('%s' % allDir)
            cam_path.append(child)
            cam_id.append(camid)
    # print(child)
    return cam_path,cam_id
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

if __name__ == '__main__':
    #按行获取csv文件，class_names相机名，label_values颜色值
    (class_names,label_values)=get_label_info('E:/yccode/Data_operation/class_dict.csv')
    #需要生成mask图的图像文件路径
    dir_path='F:/rowdata/sp-society-camera-model-identification/train'
    
    cam_path=get_all_filePath(dir_path)
    cam_id=get_all_fileName(dir_path)
    
    for image_dir in cam_path:
        image=get_all_filePath(image_dir)
        for i in image:
            print(i)
        
#        for image in image_dir:
            
#    if(operator.eq(class_names[0],cam_id[0])==True):
#        print('tt')


    

#rename('F:/数据操作代码/2019.02.26/')