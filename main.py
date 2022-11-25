from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk                    
from tkinter import ttk
from tkinter import messagebox


# Create an instance of Tk
window= Tk()
window.geometry("700x500")
# Add image file
imagepath="sui.png"
image = ImageTk.PhotoImage(Image.open(imagepath))
labelimage =Label(window,image=image)
# Create Canvas
canvas1 = Canvas( window, width = 700,height = 100)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = image,anchor = "nw")
window.title("Sayyad's CallCenter")


window.configure(background='black')
 


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



#def submit():

#	NewName=Name.get()
#	NewType=Type.get()
#	NewContext=Context.get()
#	NewSecret=Secret.get()
#	NewHost=Host.get()
#	NewDisallow=Disallow.get()
#	NewAllow=Allow.get()
#	NewMailBox=MailBox.get()
#	msg = ''
    #if (NewName != "" and NewType != "" and NewContext != ""and NewSecret != "" and NewHost != "" and NewDisallow != "" and 	 NewAllow != "" and NewMailBox != ""):
  #  if len(NewName) == 0:
        #msg = 'name can\'t be empty'
 #   else:
   #     try:
   #         if any(ch.isdigit() for ch in name):

    #	f = open("sayyad.txt", "a")
    #	f.write("[" + NewName +"]\n")
    #	f.write("type="+NewType +"\n")
    #	f.write("context="+NewContext +"\n")
    #	f.write("secret="+NewSecret +"\n")
    #	f.write("host="+NewHost +"\n")
    #	f.write("disallow="+NewDisallow+"\n")
    #	f.write("allow="+NewAllow +"\n")
    #	f.write("mailbox="+NewMailBox +"@VoiceMail\n")
    #	f.close()
    #	Name.set("")
    #	Type.set("")
    #	Context.set("")
    #	Secret.set("")
    #	Host.set("")
    ##	Disallow.set("")
    #	Allow.set("")
    #	MailBox.set("")
    

    
# Create a tab control that manages multiple tabs
tabsystem = ttk.Notebook(window)

# Create new tabs using Frame widget
tab1 = Frame(tabsystem)


tabsystem.add(tab1, text='SIP')

tabsystem.pack(expand=1, fill="both")

Header1 = Label(tab1,text = "Please, Put your info to be Registered in the SIP file",font=('calibre',10, 'bold'))

name_label = Label(tab1, text = '[Name]', font=('calibre',10, 'bold'))
name_entry = Entry(tab1,textvariable = Name, font=('calibre',10,'normal'))

type_label = Label(tab1, text = 'type=', font=('calibre',10, 'bold'))
type_entry = Entry(tab1,textvariable = Type, font=('calibre',10,'normal'))

context_label = Label(tab1, text = 'context=', font=('calibre',10, 'bold'))
context_entry = Entry(tab1,textvariable = Context, font=('calibre',10,'normal'))

secret_label = Label(tab1, text = 'secret=', font=('calibre',10, 'bold'))
secret_entry = Entry(tab1,textvariable = Secret, font=('calibre',10,'normal'),show='*')

host_label = Label(tab1, text = 'host=', font=('calibre',10, 'bold'))
host_entry = Entry(tab1,textvariable = Host, font=('calibre',10,'normal'))

disallow_label = Label(tab1, text = 'disallow=', font=('calibre',10, 'bold'))
disallow_entry = Entry(tab1,textvariable = Disallow, font=('calibre',10,'normal'))


allow_label = Label(tab1, text = 'allow=', font=('calibre',10, 'bold'))
allow_entry = Entry(tab1,textvariable = Allow, font=('calibre',10,'normal'))

mailbox_label = Label(tab1, text = 'mailbox=', font=('calibre',10, 'bold'))
mailbox_entry = Entry(tab1,textvariable = MailBox, font=('calibre',10,'normal'))



submit_button=Button(tab1,text = 'Submit', command = submit)
Header1.grid(row=0,column=1)
name_label.grid(row=1,column=1)
name_entry.grid(row=1,column=2)

type_label.grid(row=3,column=1)
type_entry.grid(row=3,column=2)

context_label.grid(row=5,column=1)
context_entry.grid(row=5,column=2)

secret_label.grid(row=7,column=1)
secret_entry.grid(row=7,column=2)

host_label.grid(row=9,column=1)
host_entry.grid(row=9,column=2)


disallow_label.grid(row=11,column=1)
disallow_entry.grid(row=11,column=2)

allow_label.grid(row=13,column=1)
allow_entry.grid(row=13,column=2)

mailbox_label.grid(row=15,column=1)
mailbox_entry.grid(row=15,column=2)


submit_button.grid(row=17,column=3)


window.mainloop()
