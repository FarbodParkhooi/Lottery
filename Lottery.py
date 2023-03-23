# Create """" Lottery """" app !!
from tkinter import *
# Create values
SelectNumbers=Tk()
version=2.8
# Defs:
# Create Label(s) and Button(s):
LabelOne=Label(SelectNumbers,text='Number 1:',bg='#030314',fg='white',font=('',10))
LabelTwo=Label(SelectNumbers,text='Number 2:',bg='#030314',fg='white',font=('',10))
LabelThree=Label(SelectNumbers,text='Number 3:',bg='#030314',fg='white',font=('',10))
LabelFour=Label(SelectNumbers,text='Number 4:',bg='#030314',fg='white',font=('',10))
LabelFive=Label(SelectNumbers,text='Number 5:',bg='#030314',fg='white',font=('',10))
LabelSix=Label(SelectNumbers,text='Number 6:',bg='#030314',fg='white',font=('',10))
ButtonNext=Button(SelectNumbers,text='next',bg='#030314',fg='white',padx=285,pady=70)
# .pack(s) |and| .place(s):
LabelOne.place(relx=0.1,rely=0.1)
LabelTwo.place(relx=0.4,rely=0.1)
LabelThree.place(relx=0.7,rely=0.1)
LabelFour.place(relx=0.1,rely=0.4)
LabelFive.place(relx=0.4,rely=0.4)
LabelSix.place(relx=0.7,rely=0.4)
ButtonNext.place(relx=0.0,rely=0.6)
# Window options: 
SelectNumbers.config(bg='#030314')
SelectNumbers.resizable(False,False)
SelectNumbers.geometry('600x400')
SelectNumbers.title('Lottery')
SelectNumbers.mainloop()