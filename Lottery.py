# Create """" Lottery """" app !!
from tkinter import *
# Create values
SelectNumbers=Tk()
version=1.2
# Create Label(s) and Button(s)
LabelOne=Label(SelectNumbers,text='Number 1:',bg='#030314',fg='white')
LabelTwo=Label(SelectNumbers,text='Number 2:',bg='#030314',fg='white')
LabelThree=Label(SelectNumbers,text='Number 3:',bg='#030314',fg='white')
LabelFour=Label(SelectNumbers,text='Number 4:',bg='#030314',fg='white')
LabelFive=Label(SelectNumbers,text='Number 5:',bg='#030314',fg='white')
LabelSix=Label(SelectNumbers,text='Number 6:',bg='#030314',fg='white')
# .pack(s) |and| .place(s)
# Window options: 
SelectNumbers.config(bg='#030314')
SelectNumbers.resizable(False,False)
SelectNumbers.geometry('600x400')
SelectNumbers.title('Lottery')
SelectNumbers.mainloop()