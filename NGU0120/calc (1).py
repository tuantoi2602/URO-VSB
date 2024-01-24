#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as tk      #imports the entire Tk package

class Application(tk.Frame):    # App class inherits from Frame class
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)  # Calls constructor for the parent class
    self.pack(fill="both", expand=1) # Make the app appear on the screen
    self.createWidgets()
    master.minsize(300, 300)
    #master.maxsize(2*300, 2*300)

  def createWidgets(self):  # Function responsible for creating all the widgets
    self.hi_there = tk.Button(self) # Creates the button
    self.hi_there["text"] = "Hello World\n(click me)" # Set button's parameters
    self.hi_there["command"] = self.say_hi
    self.hi_there.pack(side="top") # Places the button

    self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
    self.QUIT.pack(side="bottom")

  def say_hi(self):
    print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)          # Instantiating the App class
app.master.title("Sample application")  # Sets the title of the window
app.mainloop() # Starts the app's main loop; waiting for mouse and keyboard events