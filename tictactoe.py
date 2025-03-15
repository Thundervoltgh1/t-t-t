from tkinter import*
import random
root=Tk()
root.title("Tic-Tac-Toe")
root.geometry("500x500")
b=Button(root,text="welcome to Tic-Tac-Toe",fg="Blue",bg="Green",width=500,font="summer",bd=5)
c=Button(root,text="Single Player",fg="Blue",bg="Green",width=500,font="summer",bd=5)
d=Button(root,text="Multiplayer",fg="Blue",bg="Green",width=500,font="summer",bd=5)
e=Button(root,text="Exit",fg="Blue",bg="Green",width=500,font="summer",bd=5)
b.pack()
c.pack()
d.pack()
e.pack()
root.mainloop()