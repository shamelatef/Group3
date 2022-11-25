from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk                    
from tkinter import ttk
from tkinter import messagebox


# Create an instance of Tk
window= Tk()
window.geometry("700x300")
#window.configure(background='sky blue')

img = PhotoImage(file="Hacker-Thumb-a1.png")
label = Label(
    window,
    image=img
)
label.place(x=0, y=0)


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
Host=StringVar()
Disallow=StringVar()
Allow=StringVar()
MailBox=StringVar()


def submit():
    NewName=Name.get()
    NewType=Type.get()
    NewContext=Context.get()
    NewSecret=Secret.get()
    NewHost=Host.get()
    NewDisallow=Disallow.get()
    NewAllow=Allow.get()
    NewMailBox=MailBox.get()
    msg = ''

    if (len(NewName) == 0 or len(NewType) == 0 or len(NewContext) == 0 or len(NewSecret) == 0 or len(NewHost) == 0 or len(NewDisallow)== 0 or len(NewAllow)== 0 or len(NewMailBox)== 0):
            msg = 'At least one label field is empty'
    else:
            try:
           
                if (NewType != "friend" and NewType != "peer" and NewType != "user"):
                 msg = "Wrong Type"
                elif (NewHost != "dynamic"):
                 msg = "Host should be dynamic"
                else:
                 f = open("sayyad.txt", "a")
                 f.write("[" + NewName +"]\n")
                 f.write("type="+NewType +"\n")
                 f.write("context="+NewContext +"\n")
                 f.write("secret="+NewSecret +"\n")
                 f.write("host="+NewHost +"\n")
                 f.write("disallow="+NewDisallow+"\n")
                 f.write("allow="+NewAllow +"\n")
                 f.write("mailbox="+NewMailBox +"@VoiceMail\n")
                 f.close()
                 Name.set("")
                 Type.set("")
                 Context.set("")
                 Secret.set("")
                 Host.set("")
                 Disallow.set("")
                 Allow.set("")
                 MailBox.set("")
                 msg = 'Success!'
            except Exception as ep:
                messagebox.showerror('error', ep)
        
    messagebox.showinfo('message', msg)



    

    


Header1 = Label(window,text = "Please, Put your info to be Registered in the SIP file",font=('calibre',10, 'bold'),bg="yellow")

name_label = Label(window, text = '[Name]', font=('calibre',10, 'bold'),bg="skyblue")
name_entry = Entry(window,textvariable = Name, font=('calibre',10,'normal'),bg="orange")



type_label = Label(window, text = 'type=', font=('calibre',10, 'bold'),bg="skyblue")
type_entry = Entry(window,textvariable = Type, font=('calibre',10,'normal'),bg="orange")

context_label = Label(window, text = 'context=', font=('calibre',10, 'bold'),bg="skyblue")
context_entry = Entry(window,textvariable = Context, font=('calibre',10,'normal'),bg="orange")

secret_label = Label(window, text = 'secret=', font=('calibre',10, 'bold'),bg="skyblue")
secret_entry = Entry(window,textvariable = Secret, font=('calibre',10,'normal'),show='*',bg="orange")

host_label = Label(window, text = 'host=', font=('calibre',10, 'bold'),bg="skyblue")
host_entry = Entry(window,textvariable = Host, font=('calibre',10,'normal'),bg="orange")

disallow_label = Label(window, text = 'disallow=', font=('calibre',10, 'bold'),bg="skyblue")
disallow_entry = Entry(window,textvariable = Disallow, font=('calibre',10,'normal'),bg="orange")


allow_label = Label(window, text = 'allow=', font=('calibre',10, 'bold'),bg="skyblue")
allow_entry = Entry(window,textvariable = Allow, font=('calibre',10,'normal'),bg="orange")

mailbox_label = Label(window, text = 'mailbox=', font=('calibre',10, 'bold'),bg="skyblue")
mailbox_entry = Entry(window,textvariable = MailBox, font=('calibre',10,'normal'),bg="orange")

submit_button=Button(window,text = 'Submit', command = submit,bg="pink")


##############################

Header1.grid(row=0, column=1)

name_label.grid(row=2,column=1)
name_entry.grid(row=2,column=2)

type_label.grid(row=4,column=1)
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


submit_button.grid(row=18,column=3)

window.mainloop()

