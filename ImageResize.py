import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image

def resize(image, new_size):
    file_name = os.path.splitext(image)[0]
    im = Image.open(image)
    out = im.resize((int(new_size[0]), int(new_size[1])))
    # print(out.format, out.size)
    outfile = file_name + ".jpg"
    out.save(outfile)

def compress(image, rate):
    pass

def browse_btn():
    global folder_path
    folder_path=filedialog.askdirectory()



def start_btn():
    global new_size
    new_size = size_entry.get()
    new_size = new_size.split("x")
    os.chdir(folder_path)
    for image in os.listdir(folder_path):
        resize(image, new_size)


if __name__ =="__main__":
    window = tk.Tk()

    folder_path = StringVar()
    new_size = StringVar()
    #lbl1 = Label(master=window,textvariable=folder_path)
    #lbl1.grid(row=0,column=1)
    title = Label(text="Resize each image in a folder to new size!!")
    title.grid(row=0)
    label = Label(text="Click browse to find the folder")
    label.grid(row=1,column=0)


    browse_button = Button(text="Browse", command=browse_btn)
    browse_button.grid(row=1, column=1)
    # folder_text_var = StringVar()
    # folder_text = Message(window, textvariable=folder_text_var)
    # folder_text_var.set("Click browse to find the folder")
    # folder_text.grid(row=1,column=2)


    size_label = Label(text="Enter new image size")
    size_label.grid(row=3, column=0)

    entryText= StringVar()
    global size_entry
    size_entry= Entry(window, textvariable=entryText,bd=10)
    entryText.set("Width x Height")
    size_entry.grid(row=3, column=1)
    start = Button(text="Start", height=5,width=10, command=start_btn)
    start.grid(row=1, column=4)

    # label.pack(side=LEFT)
    # size_entry.pack(side = RIGHT)
    # browse_button.pack(side = RIGHT)
    # size_label.pack(side=LEFT)



    window.mainloop()
    #
    # location = input("Enter folder path (ex: C://downloads/folder): ")
    # new_size = input("Enter image size to scale (width x height ) (ex: 1000x500) : ")
    # start_btn(folder_path, new_size)



