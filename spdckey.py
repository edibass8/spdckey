from tkinter import *
import random
import os
import math
import time
import tkinter.font as tkFont
from datetime import datetime as dt
master = Tk()
#this gets the resolution of system and sets the geometry of master(tkinter)
width,height=master.winfo_screenwidth(),master.winfo_screenheight()
master.geometry('%dx%d+0+0' %(width,height))
l = Label(master,text="",width=10,bg="yellow")
l.pack(anchor='w') 
l = Label(master,text="SPDC",font=(None, 15),fg="red")
l.pack(anchor='w')
#creating the entry for the month and year
month=dt.now().month
year=dt.now().year
month_word=""
if month==1:
    month_word="January"
elif month==2:
    month_word="Febuary"
elif month==3:
    month_word="March"
elif month==4:
    month_word="April"
elif month==5:
    month_word="May"
elif month==6:
    month_word="June"
elif month==7:
    month_word="July"
elif month==8:
    month_word="August"
elif month==9:
    month_word="September"
elif month==10:
    month_word="October"
elif month==11:
    month_word="November"
elif month==12:
    month_word="December"
l = Label(master,text="KEY PERFORMANCE INDICES: "+month_word+" "+str(year),font=(None, 15),fg="red")
l.pack(anchor='w')
#creating the table 
height = 1
width = 13
#using frame for the table
frame=Frame(master)
frame.pack(anchor='w')
month_word=""
for i in range(height): #Rows
    for j in range(width): #Columns
       if j==0:
           month_word="KPL-YTD"
           l = Label(frame,text=month_word,width=10,bg="yellow")
           l.pack(side=LEFT) 
       elif j==1:
         month_word="January"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==2:
         month_word="February"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==3:
         month_word="March"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==4:
         month_word="April"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==5:
         month_word="May"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==6:
         month_word="June"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==7:
         month_word="July"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==8:
         month_word="August"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==9:
         month_word="September" 
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==10:
         month_word="October"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==11:
         month_word="November"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       elif j==12:
         month_word="December"
         l = Label(frame,text=month_word,width=10,bg="yellow")
         l.pack(side=LEFT) 
       
      
frame2=Frame(master)
frame2.pack(anchor='w')      
#to create the circle part of the table 2nd row
myCanvas = Canvas(frame2, width=1100, height=50)
myCanvas.pack(side=LEFT)
colour=""
def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    number=random.randrange(1,101)
    if number<60:
        colour="red"
    elif number>=60 and number<85:
        colour="#f8bf2c"
    elif number>=85:
        colour="green"
    return canvasName.create_oval(x0, y0, x1, y1,fill=colour)

for i in range(height): #Rows
    for j in range(width): #Columns
       if j==0:
           myCanvas.create_rectangle(0, 0, 85,45,
            outline="#f50", fill="yellow") 
           myCanvas.create_text(5, 5, text = "KPI 1", anchor = "nw")
       elif j==1:
         create_circle(110,25, 20, myCanvas)
       elif j==2:
         create_circle(185, 25, 20, myCanvas) 
       elif j==3:
         create_circle(265, 25, 20, myCanvas)
       elif j==4:
         create_circle(340, 25, 20, myCanvas)
       elif j==5:
         create_circle(415, 25, 20, myCanvas)
       elif j==6:
         create_circle(495, 25, 20, myCanvas) 
       elif j==7:
         create_circle(570, 25, 20, myCanvas)
       elif j==8:
         create_circle(645, 25, 20, myCanvas)
       elif j==9:
         create_circle(725, 25, 20, myCanvas)
       elif j==10:
         create_circle(800, 25, 20, myCanvas) 
       elif j==11:
         create_circle(875, 25, 20, myCanvas)
       elif j==12:
         create_circle(950, 25, 20, myCanvas)

frame3=Frame(master)
frame3.pack(anchor='w')      
#to create the circle path of the table 3rd row
myCanvas = Canvas(frame3, width=1100, height=50)
myCanvas.pack(side=LEFT)

for i in range(height): #Rows
    for j in range(width): #Columns
       if j==0:
           myCanvas.create_rectangle(0, 0, 85,45,
            outline="#f50", fill="yellow")
           myCanvas.create_text(5, 5, text = "KPI 2", anchor = "nw")
       elif j==1:
         create_circle(110, 25, 20, myCanvas)
       elif j==2:
         create_circle(185, 25, 20, myCanvas) 
       elif j==3:
         create_circle(265, 25, 20, myCanvas)
       elif j==4:
         create_circle(340, 25, 20, myCanvas)
       elif j==5:
         create_circle(415, 25, 20, myCanvas)
       elif j==6:
         create_circle(495, 25, 20, myCanvas) 
       elif j==7:
         create_circle(570, 25, 20, myCanvas)
       elif j==8:
         create_circle(645, 25, 20, myCanvas)
       elif j==9:
         create_circle(725, 25, 20, myCanvas)
       elif j==10:
         create_circle(800, 25, 20, myCanvas) 
       elif j==11:
         create_circle(875, 25, 20, myCanvas)
       elif j==12:
         create_circle(950, 25, 20, myCanvas)


frame4=Frame(master)
frame4.pack(anchor='w')      
#to create the circle path of the table 4th row
myCanvas = Canvas(frame4, width=1100, height=50)
myCanvas.pack(side=LEFT)

for i in range(height): #Rows
    for j in range(width): #Columns
       if j==0:
           myCanvas.create_rectangle(0, 0, 85,45,
            outline="#f50", fill="yellow")
           myCanvas.create_text(5, 5, text = "KPI 3", anchor = "nw")
       elif j==1:
         create_circle(110, 25, 20, myCanvas)
       elif j==2:
         create_circle(185, 25, 20, myCanvas) 
       elif j==3:
         create_circle(265, 25, 20, myCanvas)
       elif j==4:
         create_circle(340, 25, 20, myCanvas)
       elif j==5:
         create_circle(415, 25, 20, myCanvas)
       elif j==6:
         create_circle(495, 25, 20, myCanvas) 
       elif j==7:
         create_circle(570, 25, 20, myCanvas)
       elif j==8:
         create_circle(645, 25, 20, myCanvas)
       elif j==9:
         create_circle(725, 25, 20, myCanvas)
       elif j==10:
         create_circle(800, 25, 20, myCanvas) 
       elif j==11:
         create_circle(875, 25, 20, myCanvas)
       elif j==12:
         create_circle(950, 25, 20, myCanvas)

frame5=Frame(master)
frame5.pack(anchor='w')      
#to create the circle path of the table 5th row
myCanvas = Canvas(frame5, width=1100, height=50)
myCanvas.pack(side=LEFT)

for i in range(height): #Rows
    for j in range(width): #Columns
       if j==0:
            myCanvas.create_rectangle(0, 0, 85,45,
            outline="#f50", fill="yellow") 
            myCanvas.create_text(5, 5, text = "KPI 4", anchor = "nw")
       elif j==1:
         create_circle(110, 25, 20, myCanvas)
       elif j==2:
         create_circle(185, 25, 20, myCanvas) 
       elif j==3:
         create_circle(265, 25, 20, myCanvas)
       elif j==4:
         create_circle(340, 25, 20, myCanvas)
       elif j==5:
         create_circle(415, 25, 20, myCanvas)
       elif j==6:
         create_circle(495, 25, 20, myCanvas) 
       elif j==7:
         create_circle(570, 25, 20, myCanvas)
       elif j==8:
         create_circle(645, 25, 20, myCanvas)
       elif j==9:
         create_circle(725, 25, 20, myCanvas)
       elif j==10:
         create_circle(800, 25, 20, myCanvas) 
       elif j==11:
         create_circle(875, 25, 20, myCanvas)
       elif j==12:
         create_circle(950, 25, 20, myCanvas)


master.mainloop()

