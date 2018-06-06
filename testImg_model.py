# -*-coding:utf8-*-
__author__ = 'yjd '
import  tkinter as tk
from PIL import Image, ImageTk
from read_data import read_name_list, read_file
from train_model import Model
import cv2
from PIL import Image,ImageDraw,ImageFont
from tkinter import *
from PIL import Image, ImageTk
from tkinter import *
from PIL import Image, ImageTk

def Get():
    global image_file, im, image_label
    path = ent.get()
    if path == "":
        path = "TwoF.jpg"
    t.delete(0.0, END)
    image_file = Image.open("images/" + path)
    im = ImageTk.PhotoImage(image_file)
    image_label = Label(image_frame, image=im)
    image_label.grid(row=4, column=0, pady=20, padx=30)
    t.insert('insert', "                           Driver info(left - > right)\n\n")
    t.insert('insert', "There is information of drivers !!!\n")

def test_onePicture2():
    global image_file, im, image_label
    path = ent.get()
    if path == "":
        path = "TwoF.jpg"
    t.delete(0.0, END)
    t.insert('insert',"                           Driver info(left - > right)\n\n")
    model = Model()
    model.load()
    color = (0,255,0)
    name_list = read_name_list('dataset')

    img1 = cv2.imread("images\\" + path)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 图像灰化
    face_cascade = cv2.CascadeClassifier(
        'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
    faceRects = face_cascade.detectMultiScale(gray, 1.2, 3, minSize=(32, 32))  # 识别人脸
    hight = 0
    if len(faceRects) > 0:  # 大于0则检测到人脸
        for (x, y, w, h) in faceRects:  # 单独框出每一张人脸
            hight = hight + 1
            ROI = gray[x:x + w, y:y + h]
            ROI = cv2.resize(ROI, (128, 128), interpolation=cv2.INTER_LINEAR)
            label, prob = model.predict(ROI)  # 利用模型对cv2识别出的人脸进行比对
            if prob > 0.4:  # 如果模型认为概率高于70%则显示为模型中已有的label
                show_name = name_list[label]
            else:
                show_name = 'Stranger'
            img1 = cv2.rectangle(img1, (x, y), (x + w, y + h), color, 2)  # 在人脸区域画一个正方形出来
            if show_name!="Stranger":
                info = show_name.split('_')
                cv2.putText(img1, info[0], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  # 显示陌生人信息
                infoName = 'Name:  ' + info[0]
                infoAge = 'Age:  ' + info[1]
                infoUniversity = 'University:  ' + info[2]
                infoSex = 'Sex:  ' + info[3]
                infoDrivingLN = 'DriverNumber:  ' + info[4]
                t.insert('insert',"            driver" + str(hight) + "   " + infoDrivingLN + "\n")
                t.insert('insert', "                            " + infoName + "\n")
                t.insert('insert', "                            " + infoAge + "\n")
                t.insert('insert', "                            " + infoUniversity + "\n")
                t.insert('insert', "                            " + infoSex  + "\n\n")
            else:
                cv2.putText(img1, show_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  # 显示陌生人信息
                t.insert('insert', "It is a Stranger!!!")
        cv2.imwrite("images/result.jpg", img1)
        image_file = Image.open("images/result.jpg")
        im = ImageTk.PhotoImage(image_file)
        image_label = Label(image_frame, image=im)
        image_label.grid(row=4, column=0, pady=20, padx=30)
    else:
        image_file = Image.open("images/" + path)
        im = ImageTk.PhotoImage(image_file)
        image_label = Label(image_frame, image=im)
        image_label.grid(row=4, column=0, pady=20, padx=30)
        t.insert('insert', "No driver in this picture !!!")


def test_onePicture(path):
    model = Model()
    model.load()

    color = (0, 255, 0)
    img1 = cv2.imread(path)
    img = cv2.resize(img1, (128, 128))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    classfier = cv2.CascadeClassifier(
        "C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml")
    faceRects = classfier.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

    if len(faceRects) > 0:  # 大于0则检测到人脸
        for faceRect in faceRects:  # 单独框出每一张人脸
            x, y, w, h = faceRect
            cv2.rectangle(img1, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 3)  # 5控制绿色框的粗细
        picType, prob = model.predict(img)
        if picType != -1:
            name_list = read_name_list('dataset')
            info = name_list[picType].split('_')
            infoName='Name:'+ info[0]
            infoAge='Age:' + info[1]
            infoUniversity = 'University:'+ info[2]
            infoSex = 'Sex:' + info[3]
            infoDrivingLN = 'Driving number:' + info[4]
            cv2.rectangle(img1, (0, 0),(300, 255) ,color, 3)  # 5控制绿色框的粗细
            cv2.putText(img1, "Driver Info", (80, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, 2)  # 显示性别
            cv2.putText(img1, infoDrivingLN, (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, 2)  # 显示驾驶证号码
            cv2.putText(img1, infoName, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, 2)  # 显示名字
            cv2.putText(img1, infoAge, (0, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, 2)  # 显示年龄
            cv2.putText(img1, infoUniversity, (0, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, 2)  # 显示学历
            cv2.putText(img1, infoSex, (0, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, 2)  # 显示性别
            cv2.imshow("Camera", img1)
            # cv2.imshow(name_list[picType],img1)
            cv2.waitKey(0)
            print(name_list[picType], prob)
        else:
            cv2.imshow(" Don't know this person", img1)
            cv2.waitKey(0)
            print(" Don't know this person")
    else:
        cv2.imshow("No Face in this picture !!!", img1)
        cv2.waitKey(0)
        print("No Face in this picture")


# 读取文件夹下子文件夹中所有图片进行识别
def test_onBatch(path):
    model = Model()
    model.load()
    index = 0
    img_list, label_lsit, counter = read_file(path)
    for img in img_list:
        picType, prob = model.predict(img)
        if picType != -1:
            index += 1
            name_list = read_name_list('dataset')
            print(name_list[picType])
        else:
            print(" Don't know this person")

    return index

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x2000")
    image_frame = Frame(root)
    lab=Label(root, text='Name of the picture',font=("Helvatica",20))
    ent=Entry(root, bg='white',font=("Helvatica",20),width=30)
    lab.focus
    ent.pack()
    image_file = im = image_label = None
    image_file = Image.open("images/ex.jpg")
    im = ImageTk.PhotoImage(image_file)
    image_label = Label(image_frame, image=im)
    image_label.grid(row=4, column=0,  pady=15, padx=20)

    button1 = Button(image_frame,text='原图像显示',command = Get)
    button1.grid(row=2, column=0,pady = 8, padx = 100,sticky=W)
    button2 = Button(image_frame,text='人脸识别',command = test_onePicture2)
    button2.grid(row=2, column=0,pady = 8, padx = 100,sticky=E)
    image_frame.pack()
    t = Text(root, font = ('Helvetica', '11', 'bold'),height=15, width = 48,background = "black",foreground = 'white')  # 这里设置文本框高，可以容纳两行
    t.insert('insert', "                           Driver info(left - > right)\n\n")
    t.insert('insert', "There  is  information  of  drivers !!!\n")
    t.pack()
    root.mainloop()
