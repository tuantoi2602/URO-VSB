from tkinter import *
import math

class calc:
    def getandreplace(self):
        self.expression = self.e.get()
        self.newtext = self.expression.replace('/', '/')
        self.newtext = self.newtext.replace('x', '*')

    def equals(self):
        self.getandreplace()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def squareroot(self):
        self.getandreplace()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.sqrtval = math.sqrt(self.value)
            self.e.delete(0, END)
            self.e.insert(0, self.sqrtval)

    def square(self):
        self.getandreplace()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.sqval = math.pow(self.value, 2)
            self.e.delete(0, END)
            self.e.insert(0, self.sqval)

    def clearall(self):
        self.e.delete(0, END)


    def clear1(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi):
        self.e.insert(END, argi)


    def __init__(self, master):
        master.title('Example 2')
        master.geometry()
        self.e = Entry(master, font=("Time New Roman", 18),bg ="Black", bd=12,fg="White", insertwidth=9, width=21, justify=RIGHT)
        self.e.grid(row=0, column=0, columnspan=9)
        self.e.focus_set()


        button1=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text="1", width=5, height=3,command=lambda: self.action(1))
        button2=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text="2", width=5, height=3,command=lambda: self.action(2))
        button3=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text="3", width=5, height=3,command=lambda: self.action(3))
        button4=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text="4", width=5, height=3,command=lambda: self.action(4))
        button5=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White",text="5", width=5, height=3,command=lambda: self.action(5))
        button6=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text="6", width=5, height=3,command=lambda: self.action(6))
        button7=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text="7", width=5, height=3,command=lambda: self.action(7))
        button8=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White",text="8", width=5, height=3,command=lambda: self.action(8))
        button9=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White",text="9", width=5, height=3,command=lambda: self.action(9))
        button0=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text="0", width=5, height=3,command=lambda: self.action(0))

        button1divX=Button(master,font=("Time New Roman", 17,), bg="Grey19",fg="White",text="1/x", width=5, height=3, command=lambda: self.action('1/x'))
        buttonEqual=Button(master,font=("Time New Roman", 17,), bg="Grey19",fg="White",text="=", width=5, height=3, command=lambda: self.equals())
        buttonClearAll1=Button(master,font=("Time New Roman", 17,),bg="Grey19",fg="White", text='CE', width=5, height=3,command=lambda: self.clearall())
        buttonClearAll2=Button(master,font=("Time New Roman", 17,),bg="Grey19",fg="White", text='C', width=5, height=3,command=lambda: self.clearall())
        buttonClear=Button(master, font=("Time New Roman", 17,),bg="Grey19",fg="White",text='', width=5, height=3,command=lambda: self.clear1())
        buttonPlus=Button(master,font=("Time New Roman", 17,),bg="Grey19",fg="White", text="+", width=5, height=3,command=lambda: self.action('+'))
        buttonMulti=Button(master,font=("Time New Roman", 17,),bg="Grey19",fg="White", text="x", width=5, height=3,command=lambda: self.action('x'))
        buttonSub=Button(master, font=("Time New Roman", 17,),bg="Grey19",fg="White",text="-", width=5, height=3,command=lambda: self.action('-'))
        buttonDiv=Button(master,font=("Time New Roman", 17,),bg="Grey19",fg="White", text="÷", width=5, height=3,command=lambda: self.action('/'))
        buttonPercent=Button(master,font=("Time New Roman", 17,),bg="Grey19",fg="White", text="%", width=5, height=3,command=lambda: self.action('%'))

        buttondot=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text=".", width=5, height=3,command=lambda: self.action('.'))
        buttonPlus_and_Sub=Button(master,font=("Time New Roman", 17,),bg="Black",fg="White", text="+/-", width=5, height=3,command=lambda: self.action('+/x'))
        buttonSquareRoot=Button(master,font=("Time New Roman", 17,),bg="Grey19",fg="White", text="√x", width=5, height=3,command=lambda: self.squareroot())
        buttonSquare=Button(master,font=("Time New Roman", 17,),bg="Grey19",fg="White", text="x²", width=5, height=3,command=lambda: self.square())
#row1
        buttonPercent.grid(row=1, column=0)
        buttonClearAll1.grid(row=1, column=1)
        buttonClearAll2.grid(row=1, column=2)
        buttonClear.grid(row=1, column=3)
#row2
        button1divX.grid(row=2,column=0)
        buttonSquare.grid(row=2, column=1)
        buttonSquareRoot.grid(row=2, column=2)
        buttonDiv.grid(row=2, column=3)
#row3
        button7.grid(row=3, column=0)
        button8.grid(row=3, column=1)
        button9.grid(row=3, column=2)
        buttonMulti.grid(row=3, column=3)
#row4
        button4.grid(row=4, column=0)
        button5.grid(row=4, column=1)
        button6.grid(row=4, column=2)
        buttonSub.grid(row=4, column=3)
#row5

        button1.grid(row=5, column=0)
        button2.grid(row=5, column=1)
        button3.grid(row=5, column=2)
        buttonPlus.grid(row=5, column=3)

#row6
        buttonPlus_and_Sub.grid(row=6, column=0)
        button0.grid(row=6, column=1)
        buttondot.grid(row=6, column=2)
        buttonEqual.grid(row=6, column=3)

root = Tk()
obj = calc(root)
root.mainloop()