import tkinter
from tkinter import *
#functions
def isitPrime(a):
    d = 0
    for i in range(1,a):
        if a % i ==0:
            d = d + 1
    if d <=2:
        print("Prime")
    else:
        print("Not Prime")
#build window
w = tkinter.Tk()
w.geometry("600x400")
numberEntry = Entry()
numberEntry.pack()

def getResult():
    number = numberEntry.get()
    number = int(number)
    isitPrime(number)
resultText = Label(text="Enter a value...")
btnCheck = Button(text="Check",command=getResult)
btnCheck.pack()
resultText.pack()





w.mainloop()
