#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
root = tk.Tk()
root.title("Properties/Settings")
#event select listbox



frmMainLeft = tk.Frame(root)
frmMainLeft.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

frmL00 = tk.Frame(frmMainLeft)
frmL00.grid( sticky=tk.W)
Optionss = tk.Listbox(frmL00,selectmode=tk.SINGLE,height = 14,width=24)

Optionss.pack(side=tk.TOP)
Optionss.insert(1, "Start/Exit Options")
Optionss.insert(2, "JPG/PCD/GIF")
Optionss.insert(3, "Extensions")
Optionss.insert(4, "Viewing")
Optionss.insert(5, "Zoom/Color management")
Optionss.insert(6, "Browsing/Editing")
Optionss.insert(7, "Full screen/Slideshow")
Optionss.insert(8, "Video/Sound")
Optionss.insert(9, "File Handiling")
Optionss.insert(10, "Language")
Optionss.insert(11, "Toolbar")
Optionss.insert(12, "PlugIns")
Optionss.insert(tk.END, "Miscellaneous")

frmButton = tk.LabelFrame(frmL00)
frmButton.pack(fill="both",side = tk.TOP)

frmLeftB00 = tk.Frame(frmButton)
frmLeftB00.grid(row=0, column=0, sticky=tk.W+tk.E)
btnChooseOK = tk.Button(frmLeftB00, text="OK",width=10,command=quit)
btnChooseOK.pack(side=tk.TOP,padx=35,pady=10)
btnChooseCancel= tk.Button(frmLeftB00,text="Cancel",width=10,command=quit)
btnChooseCancel.pack(side=tk.BOTTOM,padx=35,pady=10)
#--------------------------------------------------------------------------------------------------------

frmMainRight = tk.Frame(root)
frmMainRight.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)

lbTitle_var = tk.StringVar()
lbTitle_var.set("Browsing/Editing")
lbTitle = ttk.Label(frmMainRight, text="Browsing/Editing",width = 100,relief=tk.SUNKEN, borderwidth = 2,justify = tk.RIGHT, textvariable=lbTitle_var)
lbTitle.pack(side=tk.TOP)
lbTitle.config(anchor="center")



#-----------------------------------------------------------------------------------------------------------------------------------------
# begin Browsing frame
frmBr = tk.LabelFrame(frmMainRight,text="Browsing: ")
frmBr.pack(fill="both",side = tk.TOP)

frmB10 = tk.Frame(frmBr)
frmB10.grid(row=1, column=0, sticky=tk.W)
cb10Var = tk.BooleanVar()
cb10Var.set(True)
cb10 = tk.Checkbutton(frmB10, variable=cb10Var, text="View other files in folder (moving/browsing through folder; thumbnails windows)")
cb10.pack(side=tk.LEFT)

frmB20 = tk.Frame(frmBr)
frmB20.grid(row=2, column=0, sticky=tk.W)
cb20Var = tk.BooleanVar()
cb20Var.set(True)
cb20 = tk.Checkbutton(frmB20, variable=cb20Var, text="Show hidden files/folders while moving/browsing through folder")
cb20.pack(side=tk.LEFT)

lbl30 = tk.Label(frmBr, text="If the end/begin of the folder is reached(during browsing): ")
lbl30.grid(row=3, column=0, sticky=tk.W)

frmB40 = tk.Frame(frmBr)
frmB40.grid(row=4, column=0, sticky=tk.W)
cb40Var = tk.StringVar()
cb40Var.set(True)
values = {"Show Browse dialog": "1",
          "Loop current folder": "2",
          "Do nothing": "3"}
for (text, value) in values.items():
    tk.Radiobutton(frmB40, text=text, variable=cb40Var,
                value=value).pack(side=tk.LEFT, ipady=7,ipadx=20)

frmB50 = tk.Frame(frmBr)
frmB50.grid(row=5, column=0, sticky=tk.W)
cb50Var = tk.BooleanVar()
cb50Var.set(True)
cb50 = tk.Checkbutton(frmB50, variable=cb50Var, text="Beep on folder loop, stop or screenshot save")
cb50.pack(side=tk.LEFT)

frmB60 = tk.Frame(frmBr)
frmB60.grid(row=6, column=0, sticky=tk.W)
cb60Var = tk.BooleanVar()
cb60Var.set(False)
cb60 = tk.Checkbutton(frmB60, variable=cb60Var, text="Jump to next image if Page keys or Mouse wheel used (if vertical scrollbar visible)")
cb60.pack(side=tk.LEFT)

frmB70 = tk.Frame(frmBr)
frmB70.grid(row=7, column=0, sticky=tk.W)
cb70Var = tk.BooleanVar()
cb70Var.set(True)
cb70 = tk.Checkbutton(frmB70, variable=cb70Var, text="Multipage images: Change pages using Page Up/Down keys")
cb70.pack(side=tk.LEFT)

# end Browsing frame
#-------------------------------------------------------------------------------------------------------------------------
# begin Editing frame
frmEdit = tk.LabelFrame(frmMainRight, text="Editing:")
frmEdit.pack(fill="both",side=tk.TOP)
# row 0
lbl00 = tk.Label(frmEdit, text="Set the number of Undo/Redo steps:")
lbl00.grid(row=0, column=0, sticky=tk.W)

frm02 = tk.Frame(frmEdit)
frm02.grid(row=0, column=2, sticky=tk.W)
ent02Var = tk.StringVar()
ent02Var.set("5")
ent02 = tk.Entry(frm02, textvariable=ent02Var, width=5,state=tk.DISABLED)
ent02.pack(side=tk.LEFT)
lbl02 = tk.Label(frm02, text="(0 - 20; 0 = disable Undo/Redo)")
lbl02.pack(side=tk.LEFT)
# row 1
def co():
    color = colorchooser.askcolor(initialcolor='#ff0000')
    frm10 = tk.Frame(frmEdit)
    frm10.grid(row=1, column=0, sticky=tk.W)
    chk10Var = tk.BooleanVar()
    chk10Var.set(False)
    chk10 = tk.Checkbutton(frm10, variable=chk10Var, text="Select selection/grid color")
    chk10.pack(side=tk.LEFT)
    lblColor10 = tk.Label(frm10,width=8, bg=color[1], relief=tk.SUNKEN)
    lblColor10.pack(side=tk.LEFT)
frm10 = tk.Frame(frmEdit)
frm10.grid(row=1, column=0, sticky=tk.W)
chk10Var = tk.BooleanVar()
chk10Var.set(False)
chk10 = tk.Checkbutton(frm10, variable=chk10Var, text="Select selection/grid color")
chk10.pack(side=tk.LEFT)
lblColor10 = tk.Label(frm10, width=8, bg="gray", relief=tk.SUNKEN)
lblColor10.pack(side=tk.LEFT)

frm12 = tk.Frame(frmEdit)
frm12.grid(row=1, column=2, sticky=tk.W)
btnChoose12 = tk.Button(frm10, text="Choose",width=8,command=co)
btnChoose12.pack(side=tk.LEFT,padx=10)
lbl2 = tk.Label(frm12, text="(selection color is inverted)")
lbl2.pack(side=tk.LEFT)
#row 3
chk20Var = tk.BooleanVar()
chk20Var.set(True)
chk20 = tk.Checkbutton(frmEdit, variable=chk20Var, text="Import palette: Use nearest color")
chk20.grid(row=2, column=0, columnspan=3, sticky=tk.W)
#row 4
chk30Var = tk.BooleanVar()
chk30Var.set(False)
chk30 = tk.Checkbutton(frmEdit, variable=chk30Var, text="Paste into selection: Fit to selection (default: stretch to selection)")
chk30.grid(row=3, column=0, columnspan=3, sticky=tk.W)
#row5
chk40Var = tk.BooleanVar()
chk40Var.set(True)
chk40 = tk.Checkbutton(frmEdit, variable=chk40Var, text="Paste Special: Fit clipboard image to display image")
chk40.grid(row=4, column=0, columnspan=3, sticky=tk.W)
#row6
lbl50 = tk.Label(frmEdit,text="Selection border size:")
lbl50.grid(row=5, column=0, sticky=tk.W)

frm52 = tk.Frame(frmEdit)
frm52.grid(row=5, column=2, sticky=tk.W)
ent52Var = tk.StringVar()
ent52Var.set("1")
ent52 = tk.Entry(frm52, textvariable=ent52Var, width=5)
ent52.pack(side=tk.LEFT)
lbl52 = tk.Label(frm52, text="(1-10 pixels)")
lbl52.pack(side=tk.LEFT)
#row 7
lbl60 = tk.Label(frmEdit,text="Set grid cell size (edit menu):")
lbl60.grid(row=6, column=0, sticky=tk.W)

frm62 = tk.Frame(frmEdit)
frm62.grid(row=6, column=2, sticky=tk.W)
ent62Var = tk.StringVar()
ent62Var.set("64")
ent62 = tk.Entry(frm62, textvariable=ent62Var, width=5)
ent62.pack(side=tk.LEFT)
lbl62 = tk.Label(frm62, text="pixels")
lbl62.pack(side=tk.LEFT)

#row 8
lbl70 = tk.Label(frmEdit,text="Tolerance value for 'Auto crop borders':")
lbl70.grid(row=7, column=0, sticky=tk.W)

frm72 = tk.Frame(frmEdit)
frm72.grid(row=7, column=2, sticky=tk.W)
ent72Var = tk.StringVar()
ent72Var.set("0")
ent72 = tk.Entry(frm72, textvariable=ent72Var, width=5)
ent72.pack(side=tk.LEFT)
lbl72 = tk.Label(frm72, text="(0 - 128)")
lbl72.pack(side=tk.LEFT)
# ...
# end Editing frame
#-----------------------------------------------------------------------------------
# begin Cut frame
frmC = tk.LabelFrame(frmMainRight,text="Cut: ")
frmC.pack(fill="both",side = tk.TOP)

lbc00 = tk.Label(frmC, text="Background color for ")
lbc00.grid(row=0, column=0, sticky=tk.W)
def co1():
    color = colorchooser.askcolor(initialcolor='#ff0000')
    frmC02 = tk.Frame(frmC)
    frmC02.grid(row=0, column=2, sticky=tk.W)
    cbC02Var = tk.BooleanVar()
    cbC02Var.set(False)
    lbC1Color02 = tk.Label(frmC02,width=8, bg=color[1], relief=tk.SUNKEN)
    lbC1Color02.pack(side=tk.LEFT)
frmC02 = tk.Frame(frmC)
frmC02.grid(row=0, column=2, sticky=tk.W)
cbC02Var = tk.BooleanVar()
cbC02Var.set(False)
lbC1Color02 = tk.Label(frmC02, width=8, bg="black", relief=tk.SUNKEN)
lbC1Color02.pack(side=tk.LEFT)

frmC03 = tk.Frame(frmC)
frmC03.grid(row=0, column=3, sticky=tk.W)
btnChoose03 = tk.Button(frmC03, text="Choose",command=co1)
btnChoose03.pack(side=tk.LEFT,padx=10)
lbC03 = tk.Label(frmC03, text="(or click in the loaded image)")
lbC03.pack(side=tk.LEFT)

#end cut
#------------------------------------------------------------------------------------------------------------------------------------------
# begin Options for TXT files/Text-paste:
frmOp = tk.LabelFrame(frmMainRight,text="Options for TXT files/Text-paste: ")
frmOp.pack(fill="both",side = tk.TOP)

frmOp00 = tk.Frame(frmOp)
frmOp00.grid(row=0, column=0, sticky=tk.W)
cbOp00Var = tk.StringVar()
cbOp00Var.set(True)
cbOp00 = tk.Radiobutton(frmOp00,variable=cbOp00Var, text="Custom font (True Type): ",value = 0)
cbOp00.pack(side = tk.LEFT)

frmOp01 = tk.Frame(frmOp)
frmOp01.grid(row=0, column=1, sticky=tk.W)
lbOp01 = tk.Label(frmOp01, text="Courier New.Size: 10",width = 25,relief=tk.SUNKEN, borderwidth = 4)
lbOp01.pack(side=tk.LEFT)



frmOp10 = tk.Frame(frmOp)
frmOp10.grid(row=1, column=0, sticky=tk.W)
cbOp10 = tk.Radiobutton(frmOp10,variable=cbOp00Var, text="ANSI font",value = 1)
cbOp10.pack(side = tk.LEFT)

frmOp20 = tk.Frame(frmOp)
frmOp20.grid(row=2, column=0, sticky=tk.W)
cbOp20 = tk.Radiobutton(frmOp20,variable=cbOp00Var, text="ASCII font",value = 2)
cbOp20.pack(side = tk.LEFT)

frmOp30 = tk.Frame(frmOp)
frmOp30.grid(row=3, column=0, sticky=tk.W)
cbOp30 = tk.Radiobutton(frmOp30,variable=cbOp00Var, text="ANSI thin font",value = 3)
cbOp30.pack(side = tk.LEFT)

def open():
    top = tk.Toplevel(root)

    font = tk.Frame(top)
    font.grid(row=0, column=0, sticky=tk.W)
    ty = tk.Label(font,text="Font:")
    ty.pack(side=tk.LEFT)

    entry = tk.Frame(top)
    entry.grid(row=1, column=0, sticky=tk.W)
    en = tk.Entry(entry)
    en.pack(side=tk.LEFT)

    list_font = tk.Frame(top)
    list_font.grid(row=2, column=0, sticky=tk.W)
    lst_font = tk.Listbox(list_font,selectmode=tk.SINGLE,height = 14,width=24)
    lst_font.pack(side=tk.TOP)

    lst_font.insert(1, "Start/Exit Options")
    lst_font.insert(2, "JPG/PCD/GIF")
    lst_font.insert(3, "Extensions")
    lst_font.insert(4, "Viewing")
    lst_font.insert(5, "Zoom/Color management")
    lst_font.insert(6, "Browsing/Editing")
    lst_font.insert(tk.END, "Miscellaneous")


    font_style = tk.Frame(top)
    font_style.grid(row=0, column=1, sticky=tk.W)
    ty1 = tk.Label(font_style,text="Font Style:")
    ty1.pack(side=tk.LEFT)

    entry1 = tk.Frame(top)
    entry1.grid(row=1, column=1, sticky=tk.W)
    en1 = tk.Entry(entry1)
    en1.pack(side=tk.LEFT)

    list_style = tk.Frame(top)
    list_style.grid(row=2, column=1, sticky=tk.W)
    lst_style = tk.Listbox(list_style, selectmode=tk.SINGLE, height=14, width=10)
    lst_style.pack(side=tk.TOP)

    lst_style.insert(1, "Regular")
    lst_style.insert(2, "Italic")
    lst_style.insert(3, "Bold")

    top.mainloop()

frmOp02 = tk.Frame(frmOp)
frmOp02.grid(row=0, column=2, sticky=tk.W)
btnChooseOp02 = tk.Button(frmOp02, text="Choose",command=open)
btnChooseOp02.pack(side=tk.LEFT,padx=10)

def co2():
    color = colorchooser.askcolor(initialcolor='#ff0000')
    frmOp21 = tk.Frame(frmOp)
    frmOp21.grid(row=2, column=1, sticky=tk.W)
    cbOp21Var = tk.BooleanVar()
    cbOp21Var.set(False)
    lbOp1Color21 = tk.Label(frmOp21,width=5, bg=color[1], relief=tk.SUNKEN)
    lbOp1Color21.pack(side=tk.LEFT)
frmOp11 = tk.Frame(frmOp)
frmOp11.grid(row=1, column=1, sticky=tk.W)
lbOp11 = tk.Label(frmOp11, text="Color font")
lbOp11.pack(side=tk.LEFT)

frmOp21 = tk.Frame(frmOp)
frmOp21.grid(row=2, column=1, sticky=tk.W)
cbOp21Var = tk.BooleanVar()
cbOp21Var.set(False)
lbOp1Color21 = tk.Label(frmOp21, width=5, bg="green", relief=tk.SUNKEN)
lbOp1Color21.pack(side=tk.LEFT)
btnChooseOp21 = tk.Button(frmOp21, text="Choose",command=co2)
btnChooseOp21.pack(side=tk.LEFT,padx=10)

def co3():
    color = colorchooser.askcolor(initialcolor='#ff0000')
    frmOp22 = tk.Frame(frmOp)
    frmOp22.grid(row=2, column=2, sticky=tk.W)
    cbOp22Var = tk.BooleanVar()
    cbOp22Var.set(False)
    lbOp2Color22 = tk.Label(frmOp22,width=5, bg=color[1], relief=tk.SUNKEN)
    lbOp2Color22.pack(side=tk.LEFT)

frmOp12 = tk.Frame(frmOp)
frmOp12.grid(row=1, column=2, sticky=tk.W)
lbOp12 = tk.Label(frmOp12, text="Background font")
lbOp12.pack(side=tk.LEFT)

frmOp22 = tk.Frame(frmOp)
frmOp22.grid(row=2, column=2, sticky=tk.W)
cbOp22Var = tk.BooleanVar()
cbOp22Var.set(False)
lbOp2Color22 = tk.Label(frmOp22, width=5, bg="white", relief=tk.SUNKEN)
lbOp2Color22.pack(side=tk.LEFT)
btnChooseOp22 = tk.Button(frmOp22, text="Choose",command=co3)
btnChooseOp22.pack(side=tk.LEFT,padx=10)

def setState(widget, state='disabled'):
    try:
        widget.configure(state=state)
    except:
        pass
    for child in widget.winfo_children():
        setState(child, state=state)
#event select listbox
def onSelect(val):
    sender = val.widget
    idx = sender.curselection()
    value = sender.get(idx)
    lbTitle_var.set(value)
    if value != "Browsing/Editing":
        setState(frmBr)
        setState(frmEdit)
        setState(frmC)
        setState(frmOp)
    else:
        setState(frmBr,state="normal")
        setState(frmEdit,state="normal")
        setState(frmC,state="normal")
        setState(frmOp,state="normal")

Optionss.bind("<<ListboxSelect>>", onSelect)



root.mainloop()
