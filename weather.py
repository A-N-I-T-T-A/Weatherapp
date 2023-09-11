from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import os

global root
root=Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.resizable(False,False)
#icon
image_icon=PhotoImage(file="Images\logo.png")
root.iconphoto(False,image_icon)
def onclick1():
     for wids in frame1.winfo_children():
          wids.destroy()
     frame2=tk.Frame(frame1,width=900,height=290,bg="#57adff")
     frame2.pack(side = TOP)
     global day12,imagenew,date1,city1
     city1=Label(frame2,fg="White",bg="#57adff",font="arial 25 bold")
     city1.place(x=120,y=50)
     city1.config(text=city)
     day12=Label(frame2,fg="White",bg="#57adff",font="arial 10 bold")
     day12.place(x=10,y=3)
     date1=Label(frame2,fg="White",bg="#57adff",font="arial 10 bold")
     date1.place(x=10,y=20)
     imagenew=Label(frame2,bg="#57adff")
     imagenew.place(x=130,y=100)
     back=Button(frame2,width=20,pady=7,text='Home',cursor="hand2",bg='white',fg='#57adff',border=0,command=search)
     back.place(x=720,y=250)
     
     label1=Label(frame2,text="Min Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label1.place(x=300,y=50)
     label2=Label(frame2,text="Max Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label2.place(x=300,y=80)
     label3=Label(frame2,text="Humidity   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label3.place(x=300,y=110)
     label4=Label(frame2,text="Pressure   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label4.place(x=300,y=140)
     label5=Label(frame2,text="Wind Speed :",font=("Helvetica",15),fg="black",bg="#57adff")
     label5.place(x=300,y=170)
     
     tmin2=Label(frame2,font=("Helvetica",15),fg="black",bg="#57adff")
     tmin2.place(x=450,y=50)
     tmax2=Label(frame2,font=("Helvetica",15),fg="black",bg="#57adff")
     tmax2.place(x=450,y=80)
     h2=Label(frame2,font=("Helvetica",15),fg="black",bg="#57adff")
     h2.place(x=450,y=110)
     p2=Label(frame2,font=("Helvetica",15),fg="black",bg="#57adff")
     p2.place(x=450,y=140)
     w2=Label(frame2,font=("Helvetica",15),fg="black",bg="#57adff")
     w2.place(x=450,y=170)
     d2=Label(frame2,font="arial 15 bold",fg="White",bg="#57adff")
     d2.place(x=80,y=150)
     
     d12=datetime.now()+ timedelta(1)
     temp2min= json_data['daily'][1]['temp']['min']
     temp2max= json_data['daily'][1]['temp']['max']
     pressure2=json_data['daily'][1]['pressure']
     humidity2=json_data['daily'][1]['humidity']
     wind2=json_data['daily'][1]['wind_speed']
     description2=json_data['daily'][1]['weather'][0]['description']
     
     tmin2.config(text=(temp2min,"°C"))
     tmax2.config(text=(temp2max,"°C"))
     h2.config(text=(humidity2,"%"))
     p2.config(text=(pressure2,"hPa"))
     w2.config(text=(wind2,"m/s"))
     d2.config(text=(description2))
     day12.config(text=second.strftime("%A"))
     date1.config(text=d12.strftime('%d-%m-%Y'))
     #date1.config(text=d12.strftime('%d-%m-%Y'))
     imagenew.config(image=photo2)
     imagenew.image=photo2
        
def onclick2():
     for wids in frame1.winfo_children():
          wids.destroy()
     frame3=tk.Frame(frame1,width=900,height=290,bg="#57adff")
     frame3.pack(side = TOP)
     global day12,imagenew,date1,city1
     city1=Label(frame3,fg="White",bg="#57adff",font="arial 25 bold")
     city1.place(x=120,y=50)
     city1.config(text=city)
     day12=Label(frame3,fg="White",bg="#57adff",font="arial 10 bold")
     day12.place(x=10,y=3)
     date1=Label(frame3,fg="White",bg="#57adff",font="arial 10 bold")
     date1.place(x=10,y=20)
     imagenew=Label(frame3,bg="#57adff")
     imagenew.place(x=130,y=100)
     back=Button(frame3,width=20,pady=7,text='Home',cursor="hand2",bg='white',fg='#57adff',border=0,command=search)
     back.place(x=720,y=250)
     
     label1=Label(frame3,text="Min Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label1.place(x=300,y=50)
     label2=Label(frame3,text="Max Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label2.place(x=300,y=80)
     label3=Label(frame3,text="Humidity   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label3.place(x=300,y=110)
     label4=Label(frame3,text="Pressure   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label4.place(x=300,y=140)
     label5=Label(frame3,text="Wind Speed :",font=("Helvetica",15),fg="black",bg="#57adff")
     label5.place(x=300,y=170)
     
     tmin2=Label(frame3,font=("Helvetica",15),fg="black",bg="#57adff")
     tmin2.place(x=450,y=50)
     tmax2=Label(frame3,font=("Helvetica",15),fg="black",bg="#57adff")
     tmax2.place(x=450,y=80)
     h2=Label(frame3,font=("Helvetica",15),fg="black",bg="#57adff")
     h2.place(x=450,y=110)
     p2=Label(frame3,font=("Helvetica",15),fg="black",bg="#57adff")
     p2.place(x=450,y=140)
     w2=Label(frame3,font=("Helvetica",15),fg="black",bg="#57adff")
     w2.place(x=450,y=170)
     d2=Label(frame3,font="arial 15 bold",fg="White",bg="#57adff")
     d2.place(x=80,y=150)
     
     d3=d1+timedelta(2)
     temp2min= json_data['daily'][2]['temp']['min']
     temp2max= json_data['daily'][2]['temp']['max']
     pressure2=json_data['daily'][2]['pressure']
     humidity2=json_data['daily'][2]['humidity']
     wind2=json_data['daily'][2]['wind_speed']
     description2=json_data['daily'][2]['weather'][0]['description']
     
     tmin2.config(text=(temp2min,"°C"))
     tmax2.config(text=(temp2max,"°C"))
     h2.config(text=(humidity2,"%"))
     p2.config(text=(pressure2,"hPa"))
     w2.config(text=(wind2,"m/s"))
     d2.config(text=(description2))
     day12.config(text=third.strftime("%A"))
     date1.config(text=d3.strftime('%d-%m-%Y'))
     imagenew.config(image=photo3)
     imagenew.image=photo3
         
def onclick3():
     for wids in frame1.winfo_children():
          wids.destroy()
     frame4=tk.Frame(frame1,width=900,height=290,bg="#57adff")
     frame4.pack(side = TOP)
     global day12,imagenew,date1,city1
     city1=Label(frame4,fg="White",bg="#57adff",font="arial 25 bold")
     city1.place(x=120,y=50)
     city1.config(text=city)
     day12=Label(frame4,fg="White",bg="#57adff",font="arial 10 bold")
     day12.place(x=10,y=3)
     date1=Label(frame4,fg="White",bg="#57adff",font="arial 10 bold")
     date1.place(x=10,y=20)
     imagenew=Label(frame4,bg="#57adff")
     imagenew.place(x=130,y=100)
     back=Button(frame4,width=20,pady=7,text='Home',cursor="hand2",bg='white',fg='#57adff',border=0,command=search)
     back.place(x=720,y=250)
     
     label1=Label(frame4,text="Min Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label1.place(x=300,y=50)
     label2=Label(frame4,text="Max Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label2.place(x=300,y=80)
     label3=Label(frame4,text="Humidity   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label3.place(x=300,y=110)
     label4=Label(frame4,text="Pressure   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label4.place(x=300,y=140)
     label5=Label(frame4,text="Wind Speed :",font=("Helvetica",15),fg="black",bg="#57adff")
     label5.place(x=300,y=170)
     
     tmin2=Label(frame4,font=("Helvetica",15),fg="black",bg="#57adff")
     tmin2.place(x=450,y=50)
     tmax2=Label(frame4,font=("Helvetica",15),fg="black",bg="#57adff")
     tmax2.place(x=450,y=80)
     h2=Label(frame4,font=("Helvetica",15),fg="black",bg="#57adff")
     h2.place(x=450,y=110)
     p2=Label(frame4,font=("Helvetica",15),fg="black",bg="#57adff")
     p2.place(x=450,y=140)
     w2=Label(frame4,font=("Helvetica",15),fg="black",bg="#57adff")
     w2.place(x=450,y=170)
     d2=Label(frame4,font="arial 15 bold",fg="White",bg="#57adff")
     d2.place(x=80,y=150)
     
     d4=d1+timedelta(3)
     temp2min= json_data['daily'][3]['temp']['min']
     temp2max= json_data['daily'][3]['temp']['max']
     pressure2=json_data['daily'][3]['pressure']
     humidity2=json_data['daily'][3]['humidity']
     wind2=json_data['daily'][3]['wind_speed']
     description2=json_data['daily'][3]['weather'][0]['description']
     
     tmin2.config(text=(temp2min,"°C"))
     tmax2.config(text=(temp2max,"°C"))
     h2.config(text=(humidity2,"%"))
     p2.config(text=(pressure2,"hPa"))
     w2.config(text=(wind2,"m/s"))
     d2.config(text=(description2))
     day12.config(text=fourth.strftime("%A"))
     date1.config(text=d4.strftime('%d-%m-%Y'))
     imagenew.config(image=photo4)
     imagenew.image=photo4
       
def onclick4(): 
     for wids in frame1.winfo_children():
          wids.destroy()
     frame5=tk.Frame(frame1,width=900,height=290,bg="#57adff")
     frame5.pack(side = TOP)
     global day12,imagenew,date1,city1
     city1=Label(frame5,fg="White",bg="#57adff",font="arial 25 bold")
     city1.place(x=120,y=50)
     city1.config(text=city)
     day12=Label(frame5,fg="White",bg="#57adff",font="arial 10 bold")
     day12.place(x=10,y=3)
     date1=Label(frame5,fg="White",bg="#57adff",font="arial 10 bold")
     date1.place(x=10,y=20)
     imagenew=Label(frame5,bg="#57adff")
     imagenew.place(x=130,y=100)
     back=Button(frame5,width=20,pady=7,text='Home',cursor="hand2",bg='white',fg='#57adff',border=0,command=search)
     back.place(x=720,y=250)
     
     label1=Label(frame5,text="Min Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label1.place(x=300,y=50)
     label2=Label(frame5,text="Max Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label2.place(x=300,y=80)
     label3=Label(frame5,text="Humidity   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label3.place(x=300,y=110)
     label4=Label(frame5,text="Pressure   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label4.place(x=300,y=140)
     label5=Label(frame5,text="Wind Speed :",font=("Helvetica",15),fg="black",bg="#57adff")
     label5.place(x=300,y=170)
     
     tmin2=Label(frame5,font=("Helvetica",15),fg="black",bg="#57adff")
     tmin2.place(x=450,y=50)
     tmax2=Label(frame5,font=("Helvetica",15),fg="black",bg="#57adff")
     tmax2.place(x=450,y=80)
     h2=Label(frame5,font=("Helvetica",15),fg="black",bg="#57adff")
     h2.place(x=450,y=110)
     p2=Label(frame5,font=("Helvetica",15),fg="black",bg="#57adff")
     p2.place(x=450,y=140)
     w2=Label(frame5,font=("Helvetica",15),fg="black",bg="#57adff")
     w2.place(x=450,y=170)
     d2=Label(frame5,font="arial 15 bold",fg="White",bg="#57adff")
     d2.place(x=80,y=150)
       
     d5=d1+timedelta(4) 
     temp2min= json_data['daily'][4]['temp']['min']
     temp2max= json_data['daily'][4]['temp']['max']
     pressure2=json_data['daily'][4]['pressure']
     humidity2=json_data['daily'][4]['humidity']
     wind2=json_data['daily'][4]['wind_speed']
     description2=json_data['daily'][4]['weather'][0]['description']
     
     tmin2.config(text=(temp2min,"°C"))
     tmax2.config(text=(temp2max,"°C"))
     h2.config(text=(humidity2,"%"))
     p2.config(text=(pressure2,"hPa"))
     w2.config(text=(wind2,"m/s"))
     d2.config(text=(description2))
     day12.config(text=fifth.strftime("%A"))
     date1.config(text=d5.strftime('%d-%m-%Y'))
     imagenew.config(image=photo5)
     imagenew.image=photo5
     
def onclick5(): 
     for wids in frame1.winfo_children():
          wids.destroy()
     frame6=tk.Frame(frame1,width=900,height=290,bg="#57adff")
     frame6.pack(side = TOP)
     global day12,imagenew,date1,city1
     city1=Label(frame6,fg="White",bg="#57adff",font="arial 25 bold")
     city1.place(x=120,y=50)
     city1.config(text=city)
     day12=Label(frame6,fg="White",bg="#57adff",font="arial 10 bold")
     day12.place(x=10,y=3)
     date1=Label(frame6,fg="White",bg="#57adff",font="arial 10 bold")
     date1.place(x=10,y=20)
     imagenew=Label(frame6,bg="#57adff")
     imagenew.place(x=130,y=100)
     back=Button(frame6,width=20,pady=7,text='Home',cursor="hand2",bg='white',fg='#57adff',border=0,command=search)
     back.place(x=720,y=250)
     
     label1=Label(frame6,text="Min Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label1.place(x=300,y=50)
     label2=Label(frame6,text="Max Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label2.place(x=300,y=80)
     label3=Label(frame6,text="Humidity   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label3.place(x=300,y=110)
     label4=Label(frame6,text="Pressure   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label4.place(x=300,y=140)
     label5=Label(frame6,text="Wind Speed :",font=("Helvetica",15),fg="black",bg="#57adff")
     label5.place(x=300,y=170)
     
     tmin2=Label(frame6,font=("Helvetica",15),fg="black",bg="#57adff")
     tmin2.place(x=450,y=50)
     tmax2=Label(frame6,font=("Helvetica",15),fg="black",bg="#57adff")
     tmax2.place(x=450,y=80)
     h2=Label(frame6,font=("Helvetica",15),fg="black",bg="#57adff")
     h2.place(x=450,y=110)
     p2=Label(frame6,font=("Helvetica",15),fg="black",bg="#57adff")
     p2.place(x=450,y=140)
     w2=Label(frame6,font=("Helvetica",15),fg="black",bg="#57adff")
     w2.place(x=450,y=170)
     d2=Label(frame6,font="arial 15 bold",fg="White",bg="#57adff")
     d2.place(x=80,y=150)
     
     d6=d1+timedelta(5)
     temp2min= json_data['daily'][5]['temp']['min']
     temp2max= json_data['daily'][5]['temp']['max']
     pressure2=json_data['daily'][5]['pressure']
     humidity2=json_data['daily'][5]['humidity']
     wind2=json_data['daily'][5]['wind_speed']
     description2=json_data['daily'][5]['weather'][0]['description']
     
     tmin2.config(text=(temp2min,"°C"))
     tmax2.config(text=(temp2max,"°C"))
     h2.config(text=(humidity2,"%"))
     p2.config(text=(pressure2,"hPa"))
     w2.config(text=(wind2,"m/s"))
     d2.config(text=(description2))
     day12.config(text=sixth.strftime("%A"))
     date1.config(text=d6.strftime('%d-%m-%Y'))
     imagenew.config(image=photo6)
     imagenew.image=photo6
         
def onclick6():
     for wids in frame1.winfo_children():
          wids.destroy()
     frame7=tk.Frame(frame1,width=900,height=290,bg="#57adff")
     frame7.pack(side = TOP)
     global day12,imagenew,date1,city1
     city1=Label(frame7,fg="White",bg="#57adff",font="arial 25 bold")
     city1.place(x=120,y=50)
     city1.config(text=city)
     day12=Label(frame7,fg="White",bg="#57adff",font="arial 10 bold")
     day12.place(x=10,y=3)
     date1=Label(frame7,fg="White",bg="#57adff",font="arial 10 bold")
     date1.place(x=10,y=20)
     imagenew=Label(frame7,bg="#57adff")
     imagenew.place(x=130,y=100)
     back=Button(frame7,width=20,pady=7,text='Home',cursor="hand2",bg='white',fg='#57adff',border=0,command=search)
     back.place(x=720,y=250)
     
     label1=Label(frame7,text="Min Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label1.place(x=300,y=50)
     label2=Label(frame7,text="Max Temp   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label2.place(x=300,y=80)
     label3=Label(frame7,text="Humidity   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label3.place(x=300,y=110)
     label4=Label(frame7,text="Pressure   :",font=("Helvetica",15),fg="black",bg="#57adff")
     label4.place(x=300,y=140)
     label5=Label(frame7,text="Wind Speed :",font=("Helvetica",15),fg="black",bg="#57adff")
     label5.place(x=300,y=170)
     
     tmin2=Label(frame7,font=("Helvetica",15),fg="black",bg="#57adff")
     tmin2.place(x=450,y=50)
     tmax2=Label(frame7,font=("Helvetica",15),fg="black",bg="#57adff")
     tmax2.place(x=450,y=80)
     h2=Label(frame7,font=("Helvetica",15),fg="black",bg="#57adff")
     h2.place(x=450,y=110)
     p2=Label(frame7,font=("Helvetica",15),fg="black",bg="#57adff")
     p2.place(x=450,y=140)
     w2=Label(frame7,font=("Helvetica",15),fg="black",bg="#57adff")
     w2.place(x=450,y=170)
     d2=Label(frame7,font="arial 15 bold",fg="White",bg="#57adff")
     d2.place(x=80,y=150)
     
     d7=d1+timedelta(6)
     temp2min= json_data['daily'][6]['temp']['min']
     temp2max= json_data['daily'][6]['temp']['max']
     pressure2=json_data['daily'][6]['pressure']
     humidity2=json_data['daily'][6]['humidity']
     wind2=json_data['daily'][6]['wind_speed']
     description2=json_data['daily'][6]['weather'][0]['description']
     
     tmin2.config(text=(temp2min,"°C"))
     tmax2.config(text=(temp2max,"°C"))
     h2.config(text=(humidity2,"%"))
     p2.config(text=(pressure2,"hPa"))
     w2.config(text=(wind2,"m/s"))
     d2.config(text=(description2))
     day12.config(text=seventh.strftime("%A"))
     date1.config(text=d7.strftime('%d-%m-%Y'))
     imagenew.config(image=photo7)
     imagenew.image=photo7
def search():
     root.destroy()
     os.system('python weather.py')

def getWeather():
     global city,location,long_lat
     city=textfield.get()
     geolocator=Nominatim(user_agent="geoapiExcercises")
     location= geolocator.geocode(city)
     obj= TimezoneFinder()
     result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
 
     timezone.config(text=result)
     long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
     home=pytz.timezone(result)
     local_time=datetime.now(home)
     today = date.today()
     current_time=local_time.strftime("%I:%M %p")
     clock.config(text=current_time) 
     date1.config(text=today.strftime("%b-%d-%Y"))
     
     #weather
     global json_data,api 
     api=f"https://api.openweathermap.org/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly&appid=######################"
     json_data=requests.get(api).json()
     #current
     temp= json_data['current']['temp']
     pressure=json_data['current']['pressure']
     humidity=json_data['current']['humidity']
     wind=json_data['current']['wind_speed']
     description=json_data['current']['weather'][0]['description']
     
     t.config(text=(temp,"°C"))
     h.config(text=(humidity,"%"))
     p.config(text=(pressure,"hPa"))
     w.config(text=(wind,"m/s"))
     d.config(text=description)
     global photo1,photo2,photo3,photo4,photo5,photo6,photo7
     #1st cell
     firstdayimage= json_data['daily'][0]['weather'][0]['icon']
     photo1=ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
     firstimage.config(image=photo1)
     firstimage.image=photo1   
     tempday1=json_data['daily'][0]['temp']['day']
     tempnight1=json_data['daily'][0]['temp']['night'] 
     day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")
     #2 cell
     seconddayimage= json_data['daily'][1]['weather'][0]['icon']
     img=(Image.open(f"icon/{seconddayimage}@2x.png"))
     resized_image=img.resize((50,50))
     photo2= ImageTk.PhotoImage(resized_image)
     secondimage.config(image=photo2)
     secondimage.image=photo2
     global tempday2,tempnight2
     tempday2=json_data['daily'][1]['temp']['day']
     tempnight2=json_data['daily'][1]['temp']['night']
     day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")
     
     #3 cell
     thirddayimage= json_data['daily'][2]['weather'][0]['icon']
     img=(Image.open(f"icon/{thirddayimage}@2x.png"))
     resized_image=img.resize((50,50))
     photo3= ImageTk.PhotoImage(resized_image)
     thirdimage.config(image=photo3)
     thirdimage.image=photo3
     temp3= json_data['daily'][2]['temp']['day']
     tempn3= json_data['daily'][2]['temp']['day']  
     day3temp.config(text=f"Day:{temp3}\n Night:{tempn3}")
     
     #4 cell
     fourthdayimage= json_data['daily'][3]['weather'][0]['icon']
     img=(Image.open(f"icon/{fourthdayimage}@2x.png"))
     resized_image=img.resize((50,50))
     photo4= ImageTk.PhotoImage(resized_image)
     fourthimage.config(image=photo4)
     fourthimage.image=photo4 
     tempday4=json_data['daily'][3]['temp']['day']
     tempnight4=json_data['daily'][3]['temp']['night'] 
     day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")
     
     #5 cell
     fifthdayimage= json_data['daily'][4]['weather'][0]['icon']
     img=(Image.open(f"icon/{fifthdayimage}@2x.png"))
     resized_image=img.resize((50,50))
     photo5= ImageTk.PhotoImage(resized_image)
     fifthimage.config(image=photo5)
     fifthimage.image=photo5
     tempday5=json_data['daily'][4]['temp']['day']
     tempnight5=json_data['daily'][4]['temp']['night']
     day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")
               
     #6 cell
     sixthdayimage= json_data['daily'][5]['weather'][0]['icon']
     img=(Image.open(f"icon/{sixthdayimage}@2x.png"))
     resized_image=img.resize((50,50))
     photo6= ImageTk.PhotoImage(resized_image)
     sixthimage.config(image=photo6)
     sixthimage.image=photo6
     tempday6=json_data['daily'][5]['temp']['day']
     tempnight6=json_data['daily'][5]['temp']['night']
     day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")
     
     #7 cell
     seventhdayimage= json_data['daily'][6]['weather'][0]['icon']
     img=(Image.open(f"icon/{seventhdayimage}@2x.png"))
     resized_image=img.resize((50,50))
     photo7= ImageTk.PhotoImage(resized_image)
     seventhimage.config(image=photo7)
     seventhimage.image=photo7
     tempday7=json_data['daily'][6]['temp']['day']
     tempnight7=json_data['daily'][6]['temp']['night'] 
     day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")
     
     #days
     global first,second,third,fourth,fifth,sixth,seventh
     global d1,d2,d3,d4,d5,d6,d7
     d1 =datetime.now()
     first = datetime.now()
     day1.config(text=first.strftime("%A"))
     da1.config(text=d1.strftime('%d-%m-%Y'))
     
     second=first+timedelta(days=1)
     day2.config(text=second.strftime("%A"))
      
     third=first+timedelta(days=2)
     day3.config(text=third.strftime("%A"))
       
     fourth=first+timedelta(days=3)
     day4.config(text=fourth.strftime("%A"))
  
     fifth=first+timedelta(days=4)
     day5.config(text=fifth.strftime("%A"))
       
     sixth=first+timedelta(days=5)
     day6.config(text=sixth.strftime("%A"))
     
     seventh=first+timedelta(days=6)
     day7.config(text=seventh.strftime("%A"))

def mainWindow():
     global frame1
     frame1=tk.Frame(root,width=900,height=290,bg="#57adff")
     frame1.pack(side = TOP)
     Round_box=PhotoImage(file="Images\Rounded Rectangle 1.png")
     Label(frame1,image=Round_box,bg="#57adff").place(x=30,y=110)

     #label
     label1=Label(frame1,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
     label1.place(x=50,y=120)
     label2=Label(frame1,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
     label2.place(x=50,y=140)
     label3=Label(frame1,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
     label3.place(x=50,y=160)
     label4=Label(frame1,text="Wind speed",font=('Helvetica',11),fg="white",bg="#203243")
     label4.place(x=50,y=180)
     label5=Label(frame1,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
     label5.place(x=50,y=200)
     

     ##search box
     Search_image=PhotoImage(file="Images\Rounded Rectangle 3.png")
     myimage=Label(frame1,image=Search_image,bg="#57adff")
     myimage.place(x=270,y=120)

     weat_image=PhotoImage(file="Images\Layer 7.png")
     weatherimage=Label(frame1,image=weat_image,bg="#203243")
     weatherimage.place(x=290,y=127)
     
     global textfield
     textfield=tk.Entry(frame1,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",fg='white')
     textfield.place(x=370,y=130)
     textfield.focus()

     Search_icon=PhotoImage(file="Images\Layer 6.png")
     myimage_icon=Button(frame1,image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
     myimage_icon.place(x=645,y=125)

     #Bottom box
     frame=Frame(root,width=900,height=180,bg="#212120")
     frame.pack(side = BOTTOM)

     #bottom boxes
     firstbox=PhotoImage(file="Images\Rounded Rectangle 2.png")
     secondbox=PhotoImage(file="Images\Rounded Rectangle 2 copy.png")
     
     Button(frame,image=firstbox,borderwidth=0,cursor="hand2",bg="#212120").place(x=30,y=20)
     Button(frame,image=secondbox,borderwidth=0,cursor="hand2",bg="#212120",command=onclick1).place(x=300,y=30)
     Button(frame,image=secondbox,borderwidth=0,cursor="hand2",bg="#212120",command=onclick2).place(x=400,y=30)
     Button(frame,image=secondbox,borderwidth=0,cursor="hand2",bg="#212120",command=onclick3).place(x=500,y=30)
     Button(frame,image=secondbox,borderwidth=0,cursor="hand2",bg="#212120",command=onclick4).place(x=600,y=30)
     Button(frame,image=secondbox,borderwidth=0,cursor="hand2",bg="#212120",command=onclick5).place(x=700,y=30)
     Button(frame,image=secondbox,borderwidth=0,cursor="hand2",bg="#212120",command=onclick6).place(x=800,y=30)
     
     global clock, long_lat,timezone,date1
     #clock(here will place time)
     clock=Label(frame1,font=("Helvetica",20,'bold'),fg="white",bg="#57adff")
     clock.place(x=30,y=50)
     date1=Label(frame1,font=("Helvetica",20,'bold'),fg="white",bg="#57adff")
     date1.place(x=30,y=20)
     #timezone
     timezone=Label(frame1,font=("Helvetica",20),fg="white",bg="#57adff")
     timezone.place(x=700,y=20)
     long_lat=Label(frame1,font=("Helvetica",10),fg="white",bg="#57adff")
     long_lat.place(x=700,y=50)
     
     global t,h,p,w,d
     #thpwd
     t=Label(frame1,font=("Helvetica",11,),fg="white",bg="#203243")
     t.place(x=150,y=120)
     h=Label(frame1,font=("Helvetica",11),fg="white",bg="#203243")
     h.place(x=150,y=140)
     p=Label(frame1,font=("Helvetica",11),fg="white",bg="#203243")
     p.place(x=150,y=160)
     w=Label(frame1,font=("Helvetica",11),fg="white",bg="#203243")
     w.place(x=150,y=180)
     d=Label(frame1,font=("Helvetica",11),fg="white",bg="#203243")
     d.place(x=150,y=200)

     #first cell
     firstframe=Frame(root,width=230,height=132,bg="#282829")
     firstframe.place(x=35,y=315)
     global day1,firstimage,day1temp,da1
     day1=Label(firstframe,font="arial 10",bg="#282829",fg="#fff")
     day1.place(x=100,y=3)
     da1=Label(firstframe,font="arial 10",bg="#282829",fg="#fff")
     da1.place(x=100,y=25)
     firstimage=Label(firstframe,bg="#282829")
     firstimage.place(x=1,y=15)
     day1temp=Label(firstframe,bg="#282829",fg="#57adff",font="arial 15 bold")
     day1temp.place(x=100,y=60)

     #second cell
     secondframe=Frame(root,width=70,height=115,bg="#282829")
     secondframe.place(x=305,y=325)
     global day2,secondimage,day2temp
     day2=Label(secondframe,bg="#282829",fg="#fff")
     day2.place(x=10,y=5)
     secondimage=Label(secondframe,bg="#282829")
     secondimage.place(x=7,y=20)
     day2temp=Label(secondframe,bg="#282829",fg="#fff")
     day2temp.place(x=2,y=70)

     #third cell
     thirdframe=Frame(root,width=70,height=115,bg="#282829")
     thirdframe.place(x=405,y=325)
     global day3,day3temp,thirdimage   
     day3=Label(thirdframe,bg="#282829",fg="#fff")
     day3.place(x=10,y=5)
     thirdimage=Label(thirdframe,bg="#282829")
     thirdimage.place(x=7,y=20)
     day3temp=Label(thirdframe,bg="#282829",fg="#fff")
     day3temp.place(x=2,y=70)

     #fourth cell
     fourthframe=Frame(root,width=70,height=115,bg="#282829")
     fourthframe.place(x=505,y=325)
     global day4,day4temp,fourthimage
     day4=Label(fourthframe,bg="#282829",fg="#fff")
     day4.place(x=10,y=5)
     fourthimage=Label(fourthframe,bg="#282829")
     fourthimage.place(x=7,y=20)
     day4temp=Label(fourthframe,bg="#282829",fg="#fff")
     day4temp.place(x=2,y=70)

     #fifth cell
     fifthframe=Frame(root,width=70,height=115,bg="#282829")
     fifthframe.place(x=605,y=325)
     global day5,day5temp,fifthimage
     day5=Label(fifthframe,bg="#282829",fg="#fff")
     day5.place(x=10,y=5)
     fifthimage=Label(fifthframe,bg="#282829")
     fifthimage.place(x=7,y=20)
     day5temp=Label(fifthframe,bg="#282829",fg="#fff")
     day5temp.place(x=2,y=70)

     #sixth cell
     sixthframe=Frame(root,width=70,height=115,bg="#282829")
     sixthframe.place(x=705,y=325)
     global day6,day6temp,sixthimage
     day6=Label(sixthframe,bg="#282829",fg="#fff")
     day6.place(x=10,y=5)
     sixthimage=Label(sixthframe,bg="#282829")
     sixthimage.place(x=7,y=20)
     day6temp=Label(sixthframe,bg="#282829",fg="#fff")
     day6temp.place(x=2,y=70)

     #seventh cell
     seventhframe=Frame(root,width=70,height=115,bg="#282829")
     seventhframe.place(x=805,y=325)
     global day7,day7temp,seventhimage
     day7=Label(seventhframe,bg="#282829",fg="#fff")
     day7.place(x=10,y=5)
     seventhimage=Label(seventhframe,bg="#282829")
     seventhimage.place(x=7,y=20)
     day7temp=Label(seventhframe,bg="#282829",fg="#fff")
     day7temp.place(x=2,y=70)
     logout=Button(frame1,width=20,pady=7,text='Sign out',cursor="hand2",bg='white',fg='#57adff',border=0,command=signout)
     logout.place(x=720,y=250)
     root.mainloop()
     
def signout():
     root.destroy()
     os.system('python WeatherApp.py')
     
mainWindow()