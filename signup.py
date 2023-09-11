from tkinter import *
from tkinter import messagebox
import ast 
import os

root=Tk()
root.title('Weather App')
root.geometry("890x470+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
image_icon=PhotoImage(file="Images\logo.png")
root.iconphoto(False,image_icon)

def signup():
    username=user.get()
    password=code.get()
    reset=recode.get()
    if password==reset:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)
            
            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()
            
            file=open('datasheet.txt','w')
            w=file.write(str(r))
            messagebox.showinfo('Signup','Successfully sign up')
        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'Password'})
            file.write(pp)
            file.close()
            
    else:
        messagebox.showerror('Invalid','Both password should match')

def signinB():
    root.destroy()
    #filename='WeatherApp.py'
    os.system('python WeatherApp.py')
    

img= PhotoImage(file='signup.png')
Label(root,image=img,bg='White').place(x=40,y=50)
frame=Frame(root,width=400,height=400,bg="white")
frame.place(x=480,y=40)

heading=Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=5)
########__-------------------------------------------------
def onenter(e):
    user.delete(0,'end')
def onleave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',onenter)
user.bind('<FocusOut>',onleave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
######------------------------------------------------------
def onenter(e):
    code.delete(0,'end')
def onleave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',onenter)
code.bind('<FocusOut>',onleave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
######################--------------------------------------
def onenter(e):
    recode.delete(0,'end')
def onleave(e):
    name=recode.get()
    if name=='':
        recode.insert(0,'Conform Password')

recode=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
recode.place(x=30,y=220)
recode.insert(0,'Confirm Password')
recode.bind('<FocusIn>',onenter)
recode.bind('<FocusOut>',onleave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
###########----------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="I have an account",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',command=signinB,fg="#57a1f8")
signin.place(x=200,y=340)

root.mainloop()