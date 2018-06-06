from tkinter import *
from PIL import Image, ImageTk
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

root = Tk()
root.geometry("500x800")
image_frame = Frame(root)

image_file = im = image_label = None
image_file = Image.open("images/result.jpg")

im = ImageTk.PhotoImage(image_file)
image_label = Label(image_frame,image = im)
image_label.grid(row = 3, column = 0, pady = 20, padx = 30,)

def create_image_label():
    global image_file, im, image_label
    image_file = Image.open("images/result.jpg")
    im = ImageTk.PhotoImage(image_file)
    image_label = Label(image_frame,image = im)
    image_label.grid(row = 3, column = 0, pady = 20, padx = 30)

button = Button(image_frame,text='人脸识别',anchor = 'center',command = create_image_label)
button.grid(row = 2, column = 0, sticky = NW, pady = 8, padx = 20)
image_frame.pack()
t = Text(root, height=10)  # 这里设置文本框高，可以容纳两行
t.pack()
image_label.after(2000)
root.update_idletasks()
root.mainloop()
