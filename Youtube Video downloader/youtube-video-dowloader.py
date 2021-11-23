from tkinter import *
import  pytube

#Create Display Window
from pytube import YouTube

w = Tk()
w.geometry('500x300')
w.resizable(0,0)
w.title("Makerlab youtube video downloader")



Label(w,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()



#Create Field to Enter Link
link = StringVar()

Label(w, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(w, width = 70,textvariable = link).place(x = 32, y = 90)

#Create Function to Start Downloading


def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(w, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(w,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

w.mainloop()
