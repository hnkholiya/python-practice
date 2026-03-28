from tkinter import *

root = Tk()
root.title("Traffic Signal")

canvas = Canvas(root, width=200, height=400)
canvas.pack()

canvas.create_rectangle(50,50,150,350, fill="black")

canvas.create_oval(70,70,130,130, fill="red")
canvas.create_oval(70,160,130,220, fill="yellow")
canvas.create_oval(70,250,130,310, fill="green")

root.mainloop()