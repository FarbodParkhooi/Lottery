# Create """" Lottery """" app !!
from tkinter import *
from random import randint as rnin
# Create values:
SelectNumbers=Tk()
version=0.0
UserNumbers=[]
Number1=f"number one is: {rnin(1,9)}"
Number2=f"number two is: {rnin(1,9)}"
Number3=f"number three is: {rnin(1,9)}"
Number4=f"number four is: {rnin(1,9)}"
Number5=f"number five is: {rnin(1,9)}"
Number6=f"number six is: {rnin(1,9)}"
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
    # Create Label(s):
    Number1Label=Label(SelectNumbers,text=Number1,bg='#030314',fg='white',font=('',10))
    Number2Label=Label(SelectNumbers,text=Number2,bg='#030314',fg='white',font=('',10))
    Number3Label=Label(SelectNumbers,text=Number3,bg='#030314',fg='white',font=('',10))
    Number4Label=Label(SelectNumbers,text=Number4,bg='#030314',fg='white',font=('',10))
    Number5Label=Label(SelectNumbers,text=Number5,bg='#030314',fg='white',font=('',10))
    Number6Label=Label(SelectNumbers,text=Number6,bg='#030314',fg='white',font=('',10))
    # .place(s):
    Number1Label.place(relx=0.1,rely=0.1)
    Number2Label.place(relx=0.4,rely=0.1)
    Number3Label.place(relx=0.7,rely=0.1)
    Number4Label.place(relx=0.1,rely=0.4)
    Number5Label.place(relx=0.4,rely=0.4)
    Number6Label.place(relx=0.7,rely=0.4)
    # number evaluation:
    if Number1 == UserNumbers[0]:
        if Number1 == UserNumbers[1]:
            if Number1 == UserNumbers[2]:
                if Number1 == UserNumbers[3]:
                    if Number1 == UserNumbers[4]:
                        if Number1 == UserNumbers[5]:
                            None
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