from tkinter import *
from playsound import playsound
from gtts import gTTS
w = Tk()
w.geometry('500x300')
w.resizable(0,0)
w.title("My Text-To-Speech APP")
Label(w,text = 'TEXT TO SPEECH', font ='Arial 18 bold').pack()
#Create Field to Enter Link
Label(w, text = 'Enter Text:', font = 'arial 15').place(x= 160 , y = 60)
link_enter = Entry(w, width = 70)
link_enter.place(x = 32, y = 90)

#Create Function to Start Downloading


def sts():
    text = link_enter.get()
    audio = gTTS(text)
    audio.save("sound.mp3")
    playsound("sound.mp3")




Button(w,text = 'READ TEXT', font = 'arial 15 bold' ,bg = 'blue', padx = 2, command =sts).place(x=180 ,y = 150)



w.mainloop()
#https://youtu.be/VKvILElJd4w
