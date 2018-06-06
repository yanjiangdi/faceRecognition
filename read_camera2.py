# -*- coding:utf-8 -*-
__author__ = 'yjd'

import cv2
from train_model import Model
from read_data import read_name_list
from tkinter import *
from PIL import Image, ImageTk
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
class Camera_reader(object):

    #在初始化camera的时候建立模型，并加载已经训练好的模型
    def __init__(self):
        self.model = Model()
        self.model.load()
        self.img_size = 128



    def build_camera(self):
        hight = 0
        color = (0, 255, 0)
        #opencv文件中人脸级联文件的位置，用于帮助识别图像或者视频流中的人脸
        face_cascade = cv2.CascadeClassifier('C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
        #读取dataset数据集下的子文件夹名称
        name_list = read_name_list('dataset')

        #打开摄像头并开始读取画面
        cameraCapture = cv2.VideoCapture(0)
        success, frame = cameraCapture.read()
        count = 0;
        while success and cv2.waitKey(1) == -1:

             success, frame = cameraCapture.read()
             count = count + 1
             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #图像灰化
             faces = face_cascade.detectMultiScale(gray, 1.3, 5) #识别人脸
             cv2.putText(frame, "Driver Info", (80, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, 2)  # 显示信息标题
             if len(faces) == 0:
                 cv2.rectangle(frame, (0, 0), (300, 100), color, 3)  # 5控制绿色框的粗细
                 cv2.putText(frame, "No people !!!", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, 255,
                             2)  # 显示陌生人信息
             else:
                 for (x, y, w, h) in faces:
                     ROI = gray[x:x + w, y:y + h]
                     ROI = cv2.resize(ROI, (self.img_size, self.img_size), interpolation=cv2.INTER_LINEAR)
                     label, prob = self.model.predict(ROI)  # 利用模型对cv2识别出的人脸进行比对
                     if prob > 0.7:  # 如果模型认为概率高于70%则显示为模型中已有的label
                         show_name = name_list[label]
                     else:
                         show_name = 'Stranger'

                     # 当识别出来的不是陌生人时，需要显示出司机信息
                     if show_name != "Stranger":
                         info = show_name.split('_')
                         infoName = 'Name:' + info[0]
                         infoAge = 'Age:' + info[1]
                         infoUniversity = 'University:' + info[2]
                         infoSex = 'Sex:' + info[3]
                         infoDrivingLN = 'DriverNumber:' + info[4]

                         cv2.rectangle(frame, (0, 0), (280, len(faces) * 220), color, 3)  # 5控制绿色框的粗细
                         cv2.putText(frame, info[0], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  # 显示姓名信息
                         cv2.putText(frame, infoDrivingLN, (0, hight + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
                                     3)  # 显示驾驶证号码
                         cv2.putText(frame, infoName, (0, hight + 95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
                                     3)  # 显示名字
                         cv2.putText(frame, infoAge, (0, hight + 130), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
                                     3)  # 显示年龄
                         cv2.putText(frame, infoUniversity, (0, hight + 165), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
                                     3)  # 显示学历
                         cv2.putText(frame, infoSex, (0, hight + 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
                                     3)  # 显示性别
                     else:
                         cv2.rectangle(frame, (0, 0), (300, 100), color, 3)  # 5控制绿色框的粗细
                         cv2.putText(frame, "Stranger", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  # 显示陌生人信息
                         cv2.putText(frame, "It is a Stranger", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, 255,
                                     2)  # 显示陌生人信息
                     frame = cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)  # 在人脸区域画一个正方形出来

                 #cv2.imshow("Camera", frame)
                 cv2.imwrite("images/result.jpg", frame)

        cameraCapture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = Camera_reader()
    camera.build_camera()

