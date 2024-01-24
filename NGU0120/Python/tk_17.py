import tkinter as tk
from tkinter import ttk

# Creating tkinter root
root = tk.Tk()
root.title('Benchmark')

frmMain = tk.Frame(root)
frmMain.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, padx=8, pady=8)
w = 12

def open():
    top = tk.Toplevel(root)
    top.title('Help')
    po= tk.LabelFrame(top)
    po.pack(side=tk.LEFT)
    ty=tk.Label(po,text="Mọi người thông tin chi tiết liên hệ với thầy của tôi dạy môn URO = User Interface")
    ty.pack(side=tk.LEFT)
    bt=tk.Button(po,text="Press OK for go out",command=exit)
    bt.pack(side=tk.BOTTOM)
    top.mainloop()
#-------------------------------------------------------------------------------------------------


frmB00 = tk.Frame(frmMain)
frmB00.pack(side=tk.TOP, fill=tk.X, expand=tk.NO)

lbl00 = tk.Label(frmB00, text="Dictionary size:")
lbl00.grid(row=0, column=0, sticky=tk.W)

# Combobox
size = ttk.Combobox(frmB00, width=10)
size['values'] = (' 32 MB',' 64 MB',)

size.grid(row=0, column=1, sticky=tk.W)
size.current(0)
#-----------------------------------
lb02 = tk.Label(frmB00, text="Memory Usage:\n 3530 MB/65487 MB")
lb02.grid(row=0, column=2, sticky=tk.W)

btnChoose1 = tk.Button(frmB00,width=w, text="Restart")
btnChoose1.grid(row=0, column=3, sticky=tk.W)

lb10 = tk.Label(frmB00,text="Number of CPU threads: ")
lb10.grid(row=1, column=0, sticky=tk.W)

size = ttk.Combobox(frmB00, width=10)
size['values'] = ( '16','8','4')

size.grid(row=1, column=1, sticky=tk.W)
size.current(0)

lb12 = tk.Label(frmB00, text="/16")
lb12.grid(row=1, column=2, sticky=tk.W)

btnChoose1 = tk.Button(frmB00, text="Stop",width=w,state=tk.DISABLED)
btnChoose1.grid(row=1, column=3, sticky=tk.W)

frmB01 = tk.Frame(frmMain)
frmB01.columnconfigure(0, weight=1)
frmB01.pack(side=tk.TOP, fill=tk.X, expand=tk.NO, pady=8)

tk.Label(frmB01,text="Speed", width=w).grid(row=0, column=1, sticky=tk.E)
tk.Label(frmB01,text="CPU Usage", width=w).grid(row=0, column=2, sticky=tk.E)
tk.Label(frmB01,text="Rating/ Usage", width=w).grid(row=0, column=3, sticky=tk.E)
tk.Label(frmB01,text="Rating", width=w).grid(row=0, column=4, sticky=tk.E)

#-----------------------------------------------------------------------------------------------------------------
#-----COMPRESSING LABEL FRAME --------------------------------------------------------------
frmB11 = tk.LabelFrame(frmB01, text="Compressing")
frmB11.columnconfigure(0, weight=1)
frmB11.grid(row=1, column=0, sticky=tk.W+tk.E, columnspan=5)

frmB01 = tk.Label(frmB11, text ="Current")
frmB01.grid(row=0,column=0,sticky=tk.W)

frmB001 = tk.Label(frmB11, text = "61125 KB/s",width=w)
frmB001.grid(row=0,column=1, sticky=tk.W)

frmB002 = tk.Label(frmB11, text = "1506%",width=w)
frmB002.grid(row=0,column=2, sticky=tk.W)

frmB003 = tk.Label(frmB11, text = "4634MIPS",width=w)
frmB003.grid(row=0,column=3, sticky=tk.W)

frmB004 = tk.Label(frmB11, text = "69790 MIPS",width=w)
frmB004.grid(row=0,column=4, sticky=tk.W)
#-------------------------------------------------
frm001 = tk.Label(frmB11, text="Resulting")
frm001.grid(row=1, column=0, sticky=tk.W)

frm11 = tk.Label(frmB11, text="61125 KB/s", width=w)
frm11.grid(row=1, column=1, sticky=tk.E)

frm12 = tk.Label(frmB11, text="1505%", width=w)
frm12.grid(row=1, column=2, sticky=tk.E)

frm13 = tk.Label(frmB11, text="4637 MIPS", width=w)
frm13.grid(row=1, column=3, sticky=tk.E)

frm14= tk.Label(frmB11,text ="69790 MIPS",width=w)
frm14.grid(row=1, column=4, sticky=tk.E)

#-----------------------------------------------------------------------------------------------------------
#-------------DECOMPRESSING LABEL FRAME-----------------------------------------------------------------------
frmB02 = tk.Frame(frmMain)
frmB02.columnconfigure(0, weight=1)
frmB02.pack(side=tk.TOP, fill=tk.X, expand=tk.NO, pady=8)

frmB12 = tk.LabelFrame(frmB02, text="Decompressing")
frmB12.columnconfigure(0, weight=1)
frmB12.grid(row=0, column=0, sticky=tk.W, columnspan=5)

frmB01 = tk.Label(frmB12, text ="Current")
frmB01.grid(row=0,column=0,sticky=tk.W)

frmB001 = tk.Label(frmB12, text = "1017245 KB/s",width=w)
frmB001.grid(row=0,column=1, sticky=tk.W)

frmB002 = tk.Label(frmB12, text = "1585%",width=w)
frmB002.grid(row=0,column=2, sticky=tk.W)

frmB003 = tk.Label(frmB12, text = "5709 MIPS",width=w)
frmB003.grid(row=0,column=3, sticky=tk.W)

frmB004 = tk.Label(frmB12, text = "90590 MIPS",width=w)
frmB004.grid(row=0,column=4, sticky=tk.W)

#-----------------------------------------------------------------------------------------------------------
frm001 = tk.Label(frmB12, text="Resulting")
frm001.grid(row=1, column=0, sticky=tk.W)

frm11 = tk.Label(frmB12, text="1031236 KB/s", width=w)
frm11.grid(row=1, column=1, sticky=tk.E)

frm12 = tk.Label(frmB12, text="1575%", width=w)
frm12.grid(row=1, column=2, sticky=tk.E)

frm13 = tk.Label(frmB12, text="5823 MIPS", width=w)
frm13.grid(row=1, column=3, sticky=tk.E)

frm14= tk.Label(frmB12,text ="91749 MIPS",width=w)
frm14.grid(row=1, column=4, sticky=tk.E)

#-----------------------------------------------------------------------------------------------------------
#--------ELAPSED TIME ---------------------------------------------------
frmB03 = tk.Frame(frmMain)
frmB03.columnconfigure(0, weight=1)
frmB03.pack(side=tk.TOP, fill=tk.X, expand=tk.NO, pady=8)

frm1114= tk.Label(frmB03,text ="Elapsed time:")
frm1114.grid(row=0, column=0, sticky=tk.W)

frm1115= tk.Label(frmB03,text ="00:00:41")
frm1115.grid(row=0, column=1, sticky=tk.W)

frm11116= tk.Label(frmB03,text ="Size:")
frm11116.grid(row=1, column=0, sticky=tk.W)

frm11117= tk.Label(frmB03,text ="256 MB")
frm11117.grid(row=1, column=1, sticky=tk.W)

frm11118= tk.Label(frmB03,text ="Passes:")
frm11118.grid(row=2, column=0, sticky=tk.W)

frm11119= tk.Label(frmB03,text ="5")
frm11119.grid(row=2, column=1, sticky=tk.W)
#-------------------TOTAL RATING----------------------------------------------
frmB13 = tk.LabelFrame(frmB03, text="Total Rating")
frmB13.columnconfigure(0, weight=1)
frmB13.grid(row=0, column=2, sticky=tk.E, columnspan=5,rowspan=3,ipady=7)

frm1116= tk.Label(frmB13,text ="1540%",width = w)
frm1116.grid(row=0, column=1, sticky=tk.W)

frm1117= tk.Label(frmB13,text ="5230 MIPS",width = w)
frm1117.grid(row=0, column=2, sticky=tk.W)

frm1118= tk.Label(frmB13,text ="80770 MIPS",width = w)
frm1118.grid(row=0, column=3, sticky=tk.W)

#--------------------------------------------------------------------------------------------------
#-------------------FINAL ROW--------------------------------------------
frmB04 = tk.Frame(frmMain)
frmB04.columnconfigure(0, weight=1)
frmB04.pack(side=tk.TOP, fill=tk.X, expand=tk.NO, pady=8)

frm11138= tk.Label(frmB04,text ="AMD Ryzen 7 3700X 8-Core Processor")
frm11138.grid(row=0, column=0, sticky=tk.E)

frm11148= tk.Label(frmB04,text ="(870F10)")
frm11148.grid(row=0, column=1, sticky=tk.E)

frm11149= tk.Label(frmB04,text ="7-Zip")
frm11149.grid(row=1, column=0, sticky=tk.E)

frm11141= tk.Label(frmB04,text ="19.00 (x64)")
frm11141.grid(row=1, column=1, sticky=tk.E)

frmB05 = tk.Frame(frmMain)
frmB05.columnconfigure(0, weight=1)
frmB05.pack(side=tk.TOP, fill=tk.X, expand=tk.NO, pady=8)

frm11139= tk.Label(frmB05,text ="x64 17.7100 cpus:16 128T")
frm11139.grid(row=0, column=0, sticky=tk.W)

btnChoose111 = tk.Button(frmB05, text="Help",width=w,command=open)
btnChoose111.grid(row=0, column=1, sticky=tk.E)

btnChoose112 = tk.Button(frmB05, text="Cancel",width=w,command=exit)
btnChoose112.grid(row=0, column=2, sticky=tk.E)

root.mainloop()