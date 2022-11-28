from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk                    
from tkinter import ttk
from tkinter import messagebox
import pygame
import sys
import os
import subprocess


window= Tk()
window.geometry("700x400")


tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='SIP')
tabControl.add(tab2, text ='Extensions')
tabControl.add(tab3, text ='Logs')

tabControl.pack(expand = 1, fill ="both")




#background image#############################
img = PhotoImage(file="Hacker-Thumb-a1.png")
label = Label(
    tab1,
    image=img
)

label2 = Label(
    tab2,
    image=img
)

label3 = Label(
    tab3,
    image=img
)



label.place(x=0, y=0)
label2.place(x=0,y=0)
label3.place(x=0, y=0)

#################################################

pygame.mixer.init()


window.title("Sayyad's CallCenter")

Name=StringVar()
Type=StringVar()
Context=StringVar()
Secret=StringVar()
Host="dynamic"
Disallow="all"
Allow="ulaw"
MailBox=StringVar()

#Extension tab
Extension=StringVar()
Callerid=StringVar()
Context2=StringVar()


def submit():
    NewName=Name.get()
    NewType=Type.get()
    NewContext=Context.get()
    NewSecret=Secret.get()

    NewMailBox=MailBox.get()
    msg = ''

    if (len(NewName) == 0 or len(NewType) == 0 or len(NewContext) == 0 or len(NewSecret) == 0  or len(NewMailBox)== 0):
            msg = 'At least one label field is empty'
    else:
            try:
                
                if (NewType != "friend" and NewType != "peer" and NewType != "user"):
                    msg = "Wrong Type"
                elif ((NewContext != "Agent") and (NewContext != "incoming") and (NewContext != "Manager")):
                    msg='You can only add employees in contexts (Manager, Agent, incoming)'
                else:
                    
                 with open(r'sayyad.txt', 'r+') as f:
                    data=f.read()
                    if ("["+NewName+"]") in data:
                        msg='Name is Taken'

                        
                    else:

                        f.write("[" + NewName +"]\n")
                        f.write("type="+NewType +"\n")
                        f.write("context="+NewContext +"\n")
                        f.write("secret="+NewSecret +"\n")
                        f.write("host="+Host +"\n")
                        f.write("disallow="+Disallow+"\n")
                        f.write("allow="+Allow +"\n")
                        f.write("mailbox="+NewMailBox +"@VoiceMail\n\n")
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


# GUI --> only can add existing contexts (incoming / Agent / Manager)
    

    


Header1 = Label(tab1,text = "Please, Put your info to be Registered in the SIP file",font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=150,y=10)




name_label = Label(tab1, text = '[Name]', font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=200,y=70)
name_entry = Entry(tab1,textvariable = Name, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=300,y=70)


type_label = Label(tab1, text = 'type=', font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=200,y=110)
type_entry = Entry(tab1,textvariable = Type, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=300,y=110)

context_label = Label(tab1, text = 'context=', font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=200,y=150)
context_entry = Entry(tab1,textvariable = Context, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=300,y=150)

secret_label = Label(tab1, text = 'secret=', font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=200,y=190)
secret_entry = Entry(tab1,textvariable = Secret, font=('calibre',10,'normal'),show='*',bg="black",foreground="white").place (x=300,y=190)
"""
host_label = Label(window, text = 'host=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=230)
host_entry = Entry(window,textvariable = Host, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=230)

disallow_label = Label(window, text = 'disallow=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=270)
disallow_entry = Entry(window,textvariable = Disallow, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=270)


allow_label = Label(window, text = 'allow=', font=('calibre',10, 'bold'),bg="black",foreground="white").place(x=150,y=310)
allow_entry = Entry(window,textvariable = Allow, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=250,y=310)
"""
mailbox_label = Label(tab1, text = 'mailbox=', font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=200,y=230)
mailbox_entry = Entry(tab1,textvariable = MailBox, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=300,y=230)

submit_button=Button(tab1,text = 'Submit', command = submit,bg="skyblue").place(x=300,y=340)


##############################



#TAB - 2

Header2 = Label(tab2,text = "Simple Dial configuration in Extensions.conf",font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=180,y=10)

def submit2():
    NewContext2=Context2.get()
    NewExtension=Extension.get()
    NewCallerid=Callerid.get()
    msg = ''
    replace_text = "[" + NewContext2 +"]\n" + "exten => "+NewExtension +",Dial(SIP/"+NewCallerid+")\n" + "same => n,Hangup()\n\n"
    search = "["+NewContext2+"]"
    #print(replace_text)
    if (len(NewContext2) == 0 or len(NewExtension) == 0 or len(NewCallerid) == 0):
            msg = 'At least one label field is empty'
    else:
            try:              
               
                 with open(r'sayyad.txt', 'r+') as f:
                    data = f.read()
                    if (search) in data:
                        data = data.replace(search, replace_text)
                 with open(r'sayyad.txt', 'w') as file:
                     file.write(data)
                 print(replace_text)

                 f.close()
                 Context2.set("")
                 Extension.set("")
                 Callerid.set("")
                
                 msg = 'Success!'
                 pygame.mixer.music.load("waa.mp3")
                 pygame.mixer.music.play()
            except Exception as ep:
                messagebox.showerror('error', ep)

    messagebox.showinfo('message', msg)

"""
    with open(r'sayyad.txt', 'r+') as file:

    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()

    # Searching and replacing the text
    # using the replace() function
    if 'blabla' in data:
        data = data.replace(search_text, replace_text)
    else:
        file.write(replace_text)
"""

context2_label = Label(tab2, text = 'context', font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=200,y=70)
context2_entry = Entry(tab2,textvariable = Context2, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=300,y=70)

ext_label = Label(tab2, text = 'Extension', font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=200,y=110)
ext_entry = Entry(tab2,textvariable = Extension, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=300,y=110)

callerid_label = Label(tab2, text = 'Caller ID', font=('calibre',10, 'bold'),bg="skyblue",foreground="black").place(x=200,y=150)
callerid_entry = Entry(tab2,textvariable = Callerid, font=('calibre',10,'normal'),bg="black",foreground="white").place(x=300,y=150)

submit_button2=Button(tab2,text = 'Submit', command = submit2,bg="skyblue").place(x=300,y=240)


#TAB - 3

def helloCallBack():
    filename ="/var/log/asterisk/cdr-csv/Master.csv"
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, filename])
    #Keep_both_files_in_the_same_Folder
b1=tk.Button(tab3, text="Call Logs",bg="skyblue",command=helloCallBack)
b1.place(x=310,y=150)




















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

