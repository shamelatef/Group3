from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk                    
from tkinter import ttk
from tkinter import messagebox
import pygame

# Create an instance of Tk
window= Tk()
window.geometry("700x400")
#window.configure(background='sky blue')

img = PhotoImage(file="Hacker-Thumb-a1.png")
label = Label(
    window,
    image=img
)
label.place(x=0, y=0)

pygame.mixer.init()

#Add image file
#imagepath="sui.png"
#image = ImageTk.PhotoImage(Image.open(imagepath))
#labelimage =Label(window,image=image)
# Create Canvas
#canvas1 = Canvas( window, width = 400,height = 100)

#canvas1.pack(fill = "both", expand = True)


# Display image
#canvas1.create_image( 250, 10, image = image,anchor = "nw")
window.title("Sayyad's CallCenter")

Name=StringVar()
Type=StringVar()
Context=StringVar()
Secret=StringVar()
Host="dynamic"
Disallow="all"
Allow="ulaw"
MailBox=StringVar()


def submit():
    NewName=Name.get()
    NewType=Type.get()
    NewContext=Context.get()
    NewSecret=Secret.get()
    #NewHost=Host.get()
    #NewDisallow=Disallow.get()
   # NewAllow=Allow.get()
    NewMailBox=MailBox.get()
    msg = ''

    if (len(NewName) == 0 or len(NewType) == 0 or len(NewContext) == 0 or len(NewSecret) == 0  or len(NewMailBox)== 0):
            msg = 'At least one label field is empty'
    else:
            try:
           
                if (NewType != "friend" and NewType != "peer" and NewType != "user"):
                 msg = "Wrong Type"
                
                else:
                 f = open("/home/shamel/Desktop/sayyad.txt", "a")
                 f.write("[" + NewName +"]\n")
                 f.write("type="+NewType +"\n")
                 f.write("context="+NewContext +"\n")
                 f.write("secret="+NewSecret +"\n")
                 f.write("host="+Host +"\n")
                 f.write("disallow="+Disallow+"\n")
                 f.write("allow="+Allow +"\n")
                 f.write("mailbox="+NewMailBox +"@VoiceMail\n")
                 f.close()
                 Name.set("")
                 Type.set("")
                 Context.set("")
                 Secret.set("")
                 MailBox.set("")
                 msg = 'Success!'
                 pygame.mixer.music.load("waa.mp3")
                 pygame.mixer.music.play()
            except Exception as ep:
                messagebox.showerror('error', ep)

    messagebox.showinfo('message', msg)



    

    


Header1 = Label(window,text = "Please, Put your info to be Registered in the SIP file",font=('calibre',10, 'bold'),bg="yellow").place(x=150,y=10)

name_label = Label(window, text = '[Name]', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=70)
name_entry = Entry(window,textvariable = Name, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=70)




type_label = Label(window, text = 'type=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=110)
type_entry = Entry(window,textvariable = Type, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=110)

context_label = Label(window, text = 'context=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=150)
context_entry = Entry(window,textvariable = Context, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=150)

secret_label = Label(window, text = 'secret=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=190)
secret_entry = Entry(window,textvariable = Secret, font=('calibre',10,'normal'),show='*',bg="black",foreground="white").place (x=250,y=190)
"""
host_label = Label(window, text = 'host=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=230)
host_entry = Entry(window,textvariable = Host, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=230)

disallow_label = Label(window, text = 'disallow=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=270)
disallow_entry = Entry(window,textvariable = Disallow, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=270)


allow_label = Label(window, text = 'allow=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=310)
allow_entry = Entry(window,textvariable = Allow, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=310)
"""
mailbox_label = Label(window, text = 'mailbox=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=230)
mailbox_entry = Entry(window,textvariable = MailBox, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=230)

submit_button=Button(window,text = 'Submit', command = submit).place(x=300,y=350)


##############################
"""
Header1.grid(row=0, column=1)

#name_label.grid(row=2,column=1)
name_entry.grid(row=2,column=2)

#type_label.grid(row=4,column=1)
type_entry.grid(row=4,column=2)

context_label.grid(row=6,column=1)
context_entry.grid(row=6,column=2)

secret_label.grid(row=8,column=1)
secret_entry.grid(row=8,column=2)

host_label.grid(row=10,column=1)
host_entry.grid(row=10,column=2)


disallow_label.grid(row=12,column=1)
disallow_entry.grid(row=12,column=2)

allow_label.grid(row=14,column=1)
allow_entry.grid(row=14,column=2)

mailbox_label.grid(row=16,column=1)
mailbox_entry.grid(row=16,column=2)


submit_button.grid(row=18,column=2)
"""
window.mainloop()

