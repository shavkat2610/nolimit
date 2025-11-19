import tkinter as tk
r = tk.Tk()

r.title('The game')
#You can set the geometry attribute to change the root windows size
r.geometry("500x300") #You want the size of the app to be 500x500
r.resizable(0, 0) #Don't allow resizing in the x or y direction

back = tk.Frame(master=r,)
# back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window

w = tk.Label(back, text='pick your next move')
w.pack()
button = tk.Button(back, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()
