import tkinter as tk
import tkinter.messagebox
class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.pack(fill="both", expand=1)
    self.createWidgets()
    master.minsize(300, 300)

  def createWidgets(self):
    self.frmLeft = tk.Frame(self,bg="Black")
    self.frmLeft.pack(side = "left", fill =tk.Y)

    self.frmLeftA = tk.Frame(self.frmLeft,bg ="White")
    self.frmLeftA.pack(side=tk.TOP,padx=5,pady=5)
    self.lblA = tk.Label(self.frmLeftA,text="A= ",width =5)
    self.lblA.pack(side=tk.LEFT)
    self.a = tk.StringVar()
    self.entA = tk.Entry(self.frmLeftA, textvariable = self.a, width=15)
    self.entA.pack(side=tk.LEFT)

    self.frmLeftB = tk.Frame(self.frmLeft, bg="Blue")
    self.frmLeftB.pack(side=tk.TOP, padx=5, pady=5)
    self.lblB = tk.Label(self.frmLeftB, text="B= ", width=5)
    self.lblB.pack(side=tk.LEFT)
    self.b = tk.StringVar()
    self.entB = tk.Entry(self.frmLeftB, textvariable=self.b, width=15)
    self.entB.pack(side=tk.LEFT)

    self.frmButtons = tk.Frame(self,bg ="green")
    self.frmButtons.pack(side=tk.BOTTOM, fill=tk.X)
    self.btnQuit= tk.Button(self.frmButtons,text ="Quit",width= 10,command=self.quit)
    self.btnQuit.pack(side=tk.RIGHT,padx = 10, pady=10)
    self.btnCalc = tk.Button(self.frmButtons,text="Calc",width = 10,command=self.do_calc)
    self.btnCalc.pack(side = tk.RIGHT,padx=10, pady = 10)

    self.lblResult=tk.Label(self, bg="ghost white", text = "Result")
    self.lblResult.pack(expand=1,fill =tk.BOTH)

  def do_calc(self):
    try:
        a = int(self.a.get())
        b = int(self.b.get())
        self.lblResult.configure(text = "{} + {} = {}".format(a,b,a+b))
    except:
        tkinter.messagebox.showinfo("ValueError","Real number required")


root = tk.Tk()
app = Application(master=root)
app.master.title("Example 1")
app.mainloop()