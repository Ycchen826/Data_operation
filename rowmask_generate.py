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
import cv2
import shutil

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

# 创建文件夹
def mkdir(path):
    path=path.strip()
    # path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在  True
    isExists=os.path.exists(path)
    
    if not isExists:
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        print(path+' 目录已存在')
        return False

def create_img(height,width,r,g,b):
    """#创建一张三通道图像"""
    img = np.zeros([height,width,3],dtype=np.uint8)
    #创建高600像素，宽800像素，每个像素有BGR三通道的数组（图像）
    #由于元素都在0~255之内，规定数组元素类型为uint8已足够
    img[:,:,0] = np.ones([height,width])*b
    img[:,:,1] = np.ones([height,width])*g
    img[:,:,2] = np.ones([height,width])*r

#    cv2.imshow("created_img",img)
#    cv2.waitKey(0)
    return img


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

if __name__ == '__main__':
    #按行获取csv文件，class_names相机名，label_values颜色值
    (class_names,label_values)=get_label_info('E:/yccode/Data_operation/class_dict.csv')
    #需要生成mask图的图像文件路径
    dir_path='F:/rowdata/sp-society-camera-model-identification/train'
    aim_path='E:/data/camera_verification_data/sp2018/'
    aim_mask_path='E:/data/camera_verification_data/sp2018mask/'
    dir_file=get_all_fileName(dir_path)
        
    for cam_id in dir_file:
        """cam_id保存了相机型号，image_path保存了各个图像的路径"""
        image_dir=dir_path+'/'+cam_id
        
        image_path=get_all_filePath(image_dir)
        image_name=get_all_fileName(image_dir)
        name_count=-1
        print(len(image_path))
        for image in image_path:
            name_count=name_count+1
#            print(name_count)
            img=cv2.imread(image)
            size=img.shape
            
            class_count=-1
            for num in class_names:
                class_count=class_count+1
                if(operator.eq(num,cam_id)==True):
                    r=label_values[class_count][0]
                    g=label_values[class_count][1]
                    b=label_values[class_count][2]
                    mask=create_img(size[0],size[1],r,g,b)
                    
                             
                    shutil.copyfile(image,aim_path+image_name[name_count])
                    cv2.imwrite(aim_mask_path+image_name[name_count],mask)
            
        
