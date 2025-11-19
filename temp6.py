import tkinter as tk


root = tk.Tk() # create a Tk root window

w = 500 # width for the Tk root
h = 350 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws) - (w+10)
y = 0

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(0, 0) #Don't allow resizing in the x or y direction

root.mainloop() # starts the mainloop
