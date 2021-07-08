import os
import tkinter as tk
import tkinter.messagebox
import traceback
from tkinter import filedialog
from tkinter import *
from PIL import Image

def resize(image, new_size):
    file_name = os.path.splitext(image)[0]
    file_extension = os.path.splitext(image)[1]

    if file_extension == '.webp':
        try:
            new_image_file = webp_to_jpg(image)
            resize_jpg(new_image_file, new_size)
            #convert back to webp
            convert_to_original(new_image_file,file_extension)
        except:
            tkinter.messagebox.showerror(title="warning", message="Not support webp type")
    else:
        resize_jpg(image, new_size)


def resize_jpg (image, new_size):
    file_name = os.path.splitext(image)[0]
    file_extension = os.path.splitext(image)[1]
    im = Image.open(image)
    old_width = int(im.size[0])
    # new_size is only 1 value
    if len(new_size) == 1:
        scale_rate = int(new_size[0]) / old_width
        width_rescale = int(im.size[0]) * scale_rate
        height_rescale = int(im.size[1]) * scale_rate
        out = im.resize((int(width_rescale), int(height_rescale)))
    else:
        out = im.resize((int(new_size[0]), int(new_size[1])))
    # print(out.format, out.size)
    outfile = file_name + file_extension
    out.save(outfile)

def webp_to_jpg(image):
    im_name= os.path.splitext(image)[0]
    new_name = im_name+".jpg"
    new_image = Image.open(image).convert('RGB')
    new_image.save(new_name,'jpeg')
    return new_name

def convert_to_original(image, original_type):
    im_name = os.path.splitext(image)[0]
    new_name = im_name + original_type
    new_type = original_type.replace(".","")
    new_image = Image.open(image).convert('RGB')
    new_image.save(new_name, new_type)
    return new_name

def resize_pgmagick(image, new_size):
    file_name = os.path.splitext(image)[0]
    file_extension = os.path.splitext(image)[1]
    im = Image.open(image)

    old_width = int(im.size[0])


    #new_size is only 1 value
    if len(new_size) ==1:
        scale_rate = int(new_size[0]) / old_width
        width_rescale = int(im.size[0]) * scale_rate
        height_rescale = int(im.size[1]) * scale_rate
        out = im.resize((int(width_rescale), int(height_rescale)))
    else:
        out = im.resize((int(new_size[0]), int(new_size[1])))
    # print(out.format, out.size)
    outfile = file_name + file_extension
    out.save(outfile)

def scale(image, scale_rate):
    file_name = os.path.splitext(image)[0]
    im = Image.open(image)
    width_rescale = int(im.size[0]) * int(scale_rate) /100
    height_rescale = int(im.size[1]) * int(scale_rate) /100
    out = im.resize((int(width_rescale), int(height_rescale)))
    outfile = file_name + ".jpg"
    out.save(outfile)

def compress(image, rate):
    pass

def browse_btn():
    global folder_path
    folder_path=filedialog.askdirectory()



def start_btn():

    new_size = size_entry.get()
    new_size = new_size.split("x")

    # scale_rate = scale_entry.get()


    try:
        os.chdir(folder_path)
        for image in os.listdir(folder_path):
            # if size_entryText.get() != "Width x Height" and scale_text.get() != "Percentage (ex: 30)":
            #     tkinter.messagebox.showwarning(title="warning",
            #                                    message="Warning !! Can't resize and rescale images at the same time!!")
            #     size_entryText.set("Width x Height")
            #     # scale_text.set("Percentage (ex: 30)")
            #     break
            # elif size_entryText.get() != "Width x Height" :
                resize(image, new_size)
            # elif scale_text.get() != "Percentage (ex: 30)":
                # scale(image, scale_rate)
        size_entryText.set("Width x Height or Width")
        new_size = "Width x Height or Width"
        # scale_text.set("Percentage (ex: 30)")
        # scale_rate = "Percentage (ex: 30)"
    except:
        tkinter.messagebox.showerror(title="warning",message = traceback.format_exc())
        # tkinter.messagebox.showerror(title="warning",
        #                              message="Need to set the Folder first. Close this message then Click Browse!")
        # size_entryText.set("Width x Height or Width")
        # scale_text.set("Percentage (ex: 30)")


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

    #resize
    size_label = Label(text="Enter new image size")
    size_label.grid(row=3, column=0)
    global size_entryText
    size_entryText= StringVar()
    #global size_entry
    size_entry= Entry(window, textvariable=size_entryText,bd=10)
    size_entryText.set("Width x Height or Width")
    size_entry.grid(row=3, column=1)

    #rescale
    # scale_label = Label(text="Enter rate to scale")
    # scale_label.grid(row=4, column=0)
    global scale_text
    scale_text = StringVar()
    # scale_entry = Entry(window, textvariable=scale_text, bd=10)
    # scale_text.set("Percentage (ex: 30)")
    # scale_entry.grid(row=4, column=1)


    #start
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



