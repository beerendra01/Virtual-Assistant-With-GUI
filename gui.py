from tkinter import *

win = Tk()
win.title("Master")
btn = Button(win, text= "Speak", width=10, height=3,bg="yellow", fg="black")
btn.place(x=650,y=500)
btn = Button(win,text="Close",width=10,height=3,bg="Green")
btn.place(x=725,y=500)
canvas =Canvas(width=500,height=500)
canvas.pack()
photo = PhotoImage(file='C:/Users/ASUS/Downloads/abcd.png')
canvas.create_image(200,200,image=photo,anchor=CENTER)
win.mainloop()