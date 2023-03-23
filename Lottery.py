# Create """" Lottery """" app !!
from tkinter import *
# Create values
SelectNumbers=Tk()
version = 1.2
# Create Label(s) and Button(s)
LabelOne = Label(SelectNumbers, text='Number 1: ', bg='#030314', fg='white')
# Window options: 
SelectNumbers.config(bg='#030314')
SelectNumbers.resizable(False,False)
SelectNumbers.geometry('600x400')
SelectNumbers.title('Lottery')
SelectNumbers.mainloop()