#-*-coding:utf8-*-
__author__ = 'yjd '

import os
import cv2
import time
from PIL import Image, ImageFilter ,ImageEnhance 
from read_img import readAllImg

#从源路径中读取所有图片放入一个list，然后逐一进行检查，把其中的脸扣下来，存储到目标路径中
def dealImg(sourcePath,destPath):
    try:
        #读取照片,注意第一个元素是文件名

        #对list中图片逐一进行检查,找出其中的人脸然后写到目标文件夹下

        count = 0;
        for filename in os.listdir(sourcePath):              #listdir的参数是文件夹的路径
            count +=1
            
            img=Image.open(sourcePath + os.sep + filename)
            img = img.convert('RGB')
            dealImage(img,destPath,"old_" + filename)
                
            Out1	= img.resize((500, 500), Image.ANTIALIAS)  	# 改变图片大小
            dealImage(Out1,destPath,"changeSize_" + filename)
                
            Out2	= img.rotate(45)  			# 逆时针旋转 45 度角。
            dealImage(Out2,destPath,"Counterclockwise_rotation_" + filename)

                
            Out3	= img.transpose(Image.FLIP_LEFT_RIGHT)  	# 左右对换。
            dealImage(Out3,destPath,"lr_exchange_" + filename)

                
            Out4 = img.transpose(Image.FLIP_TOP_BOTTOM) 	# 上下对换。
            dealImage(Out4,destPath,"ud_exchange_" + filename)
                
            Out5 = img.transpose(Image.ROTATE_90)  	# 旋转 90 度角。
            dealImage(Out5,destPath,"rotation_" + filename)
                


    except IOError:
        print("Error")

    else:
        print('Already read '+str(count-1)+' Faces to Destination ')

def dealImage(img,destPath,filename):
    enh = img.filter(ImageFilter.DETAIL)     	#滤镜
    enh = ImageEnhance.Contrast(enh)
    enh.enhance(1.3).save(destPath + os.sep + filename)

    
if __name__ == '__main__':
     dealImg('images\ymh_sc','images\ymh_deal')
     
     
     
     