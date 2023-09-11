from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import ast
import os

root=Tk()
root.title('Weather App')
root.geometry("890x470+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
image_icon=PhotoImage(file="Images\logo.png")
root.iconphoto(False,image_icon)

simage=ImageTk.PhotoImage(file='show.png')
himage=ImageTk.PhotoImage(file='hide.png')
def show():
    hbutton=Button(frame,image=himage,command=hide,relief=FLAT,activebackground='white',bd=0,background='white')
    hbutton.place(x=325,y=170)
    code.config(show='')
    
def hide():
    sbutton=Button(frame,image=simage,command=show,relief=FLAT,activebackground='white',bd=0,background='white')
    sbutton.place(x=325,y=170)
    code.config(show='*')


def signin():
    username=user.get()
    password=code.get()
    
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    
    
    if username in r.keys() and password==r[username]:
        root.destroy()
        #filename='weather.py'
        os.system('python weather.py')
    else:
        messagebox.showerror('Invalid','Invalid username or password')

def signupB():
    root.destroy()
    #filename='signup.py'
    os.system('python signup.py') 
          
           
img= PhotoImage(file='login1.png')
Label(root,image=img,bg='White').place(x=40,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=40)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=5)

sbutton=Button(frame,image=simage,command=show,relief=FLAT,activebackground='white',bd=0,background='white')
sbutton.place(x=325,y=170)
############################################################
Label(frame,text='Username',fg='black',bg='white',font=('Microsoft YaHei UI Light',11)).place(x=20,y=70)
user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=100)
#user.insert(0,'Username')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=127)
##########################################################################

Label(frame,text='Password',fg='black',bg='white',font=('Microsoft YaHei UI Light',11)).place(x=20,y=140)
code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('',11),show='*')
code.place(x=30,y=170)
#code.insert(0,'Password')


Frame(frame,width=295,height=2,bg='black').place(x=25,y=197)
###########---------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=230)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=280)

signup=Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',fg="#57a1f8",command=signupB)
signup.place(x=215,y=280)


root.mainloop()