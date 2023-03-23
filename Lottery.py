# Create """" Lottery """" app !!
from tkinter import *
from random import randint as rnin
# Create values:
SelectNumbers=Tk()
version=8.6
NumbersList=[1,2,3,4,5,6,7,8,9]
UserNumbers=[]
# Def(s):
def IfButtonNextClicked():
    # add numbers to my list:
    UserNumbers.append(EntryOne.get())
    UserNumbers.append(EntryTwo.get())
    UserNumbers.append(EntryThree.get())
    UserNumbers.append(EntryFour.get())
    UserNumbers.append(EntryFive.get())
    UserNumbers.append(EntrySix.get())
    # Destroy Label(s) |and| Button(s) |and| Entry(s):
    LabelOne.destroy()
    LabelTwo.destroy()
    LabelThree.destroy()
    LabelFour.destroy()
    LabelFive.destroy()
    LabelSix.destroy()
    ButtonNext.destroy()
    EntryOne.destroy()
    EntryTwo.destroy()
    EntryThree.destroy()
    EntryFour.destroy()
    EntryFive.destroy()
    EntrySix.destroy()
    # Create new values:
    NewWindow=Toplevel()
    # NewWindow options:
# Create Label(s) |and| Button(s) |and| Entry(s):
LabelOne=Label(SelectNumbers,text='Number 1:',bg='#030314',fg='white',font=('',10))
LabelTwo=Label(SelectNumbers,text='Number 2:',bg='#030314',fg='white',font=('',10))
LabelThree=Label(SelectNumbers,text='Number 3:',bg='#030314',fg='white',font=('',10))
LabelFour=Label(SelectNumbers,text='Number 4:',bg='#030314',fg='white',font=('',10))
LabelFive=Label(SelectNumbers,text='Number 5:',bg='#030314',fg='white',font=('',10))
LabelSix=Label(SelectNumbers,text='Number 6:',bg='#030314',fg='white',font=('',10))
ButtonNext=Button(SelectNumbers,text='next',bg='#030314',fg='white',padx=285,pady=70,command=IfButtonNextClicked)
EntryOne=Entry(SelectNumbers,width=15,bg='#060624',fg='white',borderwidth=0)
EntryTwo=Entry(SelectNumbers,width=15,bg='#060624',fg='white',borderwidth=0)
EntryThree=Entry(SelectNumbers,width=15,bg='#060624',fg='white',borderwidth=0)
EntryFour=Entry(SelectNumbers,width=15,bg='#060624',fg='white',borderwidth=0)
EntryFive=Entry(SelectNumbers,width=15,bg='#060624',fg='white',borderwidth=0)
EntrySix=Entry(SelectNumbers,width=15,bg='#060624',fg='white',borderwidth=0)
# .pack(s) |and| .place(s):
LabelOne.place(relx=0.1,rely=0.1)
LabelTwo.place(relx=0.4,rely=0.1)
LabelThree.place(relx=0.7,rely=0.1)
LabelFour.place(relx=0.1,rely=0.4)
LabelFive.place(relx=0.4,rely=0.4)
LabelSix.place(relx=0.7,rely=0.4)
ButtonNext.place(relx=0.0,rely=0.6)
EntryOne.place(relx=0.22,rely=0.1)
EntryTwo.place(relx=0.52,rely=0.1)
EntryThree.place(relx=0.82,rely=0.1)
EntryFour.place(relx=0.22,rely=0.4)
EntryFive.place(relx=0.52,rely=0.4)
EntrySix.place(relx=0.82,rely=0.4)
# Window options: 
SelectNumbers.config(bg='#030314')
SelectNumbers.resizable(False,False)
SelectNumbers.geometry('600x400')
SelectNumbers.title('Lottery')
SelectNumbers.mainloop()