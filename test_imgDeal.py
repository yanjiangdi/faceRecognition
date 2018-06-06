import os
import cv2
import time
from PIL import Image, ImageFilter ,ImageEnhance
from read_img import readAllImg


img= Image.open("images/hw13.jpg")
img = img.transpose(Image.ROTATE_90)  # 旋转 90 度角。
img = img.filter(ImageFilter.DETAIL)  # 滤镜
img = ImageEnhance.Contrast(img)
img.enhance(1.5).show()

img = img.transpose(Image.ROTATE_90)  # 旋转 90 度角。
img= img.resize((500, 500), Image.ANTIALIAS)  # 改变图片大小
img = img.rotate(45)  # 逆时针旋转 45 度角。
img = img.transpose(Image.FLIP_LEFT_RIGHT)  # 左右对换。
img = img.transpose(Image.FLIP_TOP_BOTTOM)  # 上下对换。