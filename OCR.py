from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import pytesseract     
"""import pyttsx3"""


#creating the application main window.   
app = Tk()
app.title("Multi-Language OCR")
app.geometry("1300x600")
app.resizable(0, 0)

def open_image():
     global imagefile
     app.filename = filedialog.askopenfilename(initialdir="C:",title="Open image",filetypes=(("png files","*.png"),("all files","*.*")))
     width = 400
     height = 400
     img = Image.open(app.filename)
     img = img.resize((width, height), Image.ANTIALIAS)
     img = ImageTk.PhotoImage(img)
     app.img = img
     photo.image = img
     photo.create_image(0, 0, anchor=NW, image=img)
     
def bengali():
    result = pytesseract.image_to_string(app.filename,lang ='ben')
    output.delete('1.0', END)
    output.insert(1.0,result)

def gujrati():
    result = pytesseract.image_to_string(app.filename,lang ='guj')
    output.delete('1.0', END)
    output.insert(1.0,result)

def hindi():
    result = pytesseract.image_to_string(app.filename,lang ='hin')
    output.delete('1.0', END)
    output.insert(1.0,result)

def kannada():
    result = pytesseract.image_to_string(app.filename,lang ='kan')
    output.delete('1.0', END)
    output.insert(1.0,result)

def malyalam():
    result = pytesseract.image_to_string(app.filename,lang ='hin')
    output.delete('1.0', END)
    output.insert(1.0,result)


def marathi():
    result = pytesseract.image_to_string(app.filename,lang ='mar')
    output.delete('1.0', END)
    output.insert(1.0,result)

def nepali():
    result = pytesseract.image_to_string(app.filename,lang ='nep')
    output.delete('1.0', END)
    output.insert(1.0,result)

def punjabi():
    result = pytesseract.image_to_string(app.filename,lang ='pun')
    output.delete('1.0', END)
    output.insert(1.0,result) 

def sanskrit():
    result = pytesseract.image_to_string(app.filename,lang ='san')
    output.delete('1.0', END)
    output.insert(1.0,result)

def sindhi():
    result = pytesseract.image_to_string(app.filename,lang ='snd')
    output.delete('1.0', END)
    output.insert(1.0,result)
    
def tamil():
    result = pytesseract.image_to_string(app.filename,lang ='tam')
    output.delete('1.0', END)
    output.insert(1.0,result)


#button defination 
button_0 = Button(app,text="Open Image",bg="slate gray",fg="black",command=open_image,font="Times",width=90)
button_1 = Button(app, text="Bengali",bg="ivory4",fg="white",width = "15",command=bengali,font="Times")
button_2 = Button(app, text="Gujrati",bg="ivory4",fg="white",width = "15",command=gujrati,font="Times")
button_3 = Button(app, text="Hindi",bg="ivory4",fg="white",width = "15",command=hindi,font="Times")
button_4 = Button(app, text="Kannada",bg="ivory4",fg="white",width = "15",command=kannada,font="Times")
button_5 = Button(app, text="Malyalam",bg="ivory4",fg="white",width = "15",command=malyalam,font="Times")
button_6 = Button(app, text="Marathi",bg="ivory4",fg="white",width = "15",command=marathi,font="Times")
button_7 = Button(app, text="Nepali",bg="ivory4",fg="white",width = "15",command=nepali,font="Times")
button_8 = Button(app, text="Punjabi",bg="ivory4",fg="white",width = "15",command=punjabi,font="Times")
button_9 = Button(app, text="Sanskrit",bg="ivory4",fg="white",width = "15",command=sanskrit,font="Times")
button_10 = Button(app, text="Sindhi",bg="ivory4",fg="white",width = "15",command=sindhi,font="Times")
button_11 = Button(app, text="Tamil",bg="ivory4",fg="white",width = "15",command=tamil,font="Times")


#canvas used to display image

photo = Canvas(app,bg="gray",width="400",height="400")

#label used to print output text;

output = Text(app,bg="LightYellow2",fg="black",)


#grid
button_0.grid(row=0,column=0,columnspan=3,padx=10,pady=5 )

photo.grid(row ="1",column="0",rowspan=11,padx="20")
output.grid(row=2,column = 2,rowspan=11,padx=10)


button_1.grid(row=1 ,column =1)
button_2.grid(row=2 ,column=1)
button_3.grid(row=3 ,column = 1)
button_4.grid(row=4 ,column = 1)
button_5.grid(row=5 ,column = 1)
button_6.grid(row=6 ,column = 1)
button_7.grid(row=7 ,column = 1)
button_8.grid(row=8 ,column = 1)
button_9.grid(row=9 ,column = 1)
button_10.grid(row=10 ,column = 1)
button_11.grid(row=11 ,column = 1)









#Entering the event main loop  
app.mainloop()  
