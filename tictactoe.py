from tkinter import*
from functools import partial
from tkinter import messagebox
import random
global board
board=[[" "for x in range(3)]for y in range(3)]
u=0
def winner(b,w):
    return (
        (b[0][0]==w and b[0][1]==w and b[0][2]==w) or
        (b[1][0]==w and b[1][1]==w and b[1][2]==w) or
        (b[2][0]==w and b[2][1]==w and b[2][2]==w) or
        (b[0][0]==w and b[1][1]==w and b[2][2]==w) or
        (b[0][2]==w and b[1][1]==w and b[2][0]==w) or
        (b[0][0]==w and b[1][0]==w and b[2][0]==w) or
        (b[0][1]==w and b[1][1]==w and b[2][1]==w) or
        (b[0][2]==w and b[1][2]==w and b[2][2]==w)
    )
def get_text(i,j,l1,l2,k):
    if board[i][j]==' ':
        if u%2==0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j]="x"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j]="o"
        u+=1
        button[i][j].config(text=board[i][j])
    if winner(board,"x"):
        k.destroy()
        messagebox.showinfo("Winner","Player 1 won the match")

    elif winner(board,"o"):
        k.destroy()
        messagebox.showinfo("Winner","Player 2 won the match")

    elif isfull():
        k.destroy()
        messagebox.showinfo("Tie game")   
def isfull():
    flag=True
    for i in board:
        if i.count(' ')>0:
            flag=False
    return flag
        
def gameboard(game):
    button=[]
    for i in range(3):
        t=3+i
        button.append(i)
        button[i]=[]
        for j in range(3):
            y=j
            button[i].append(j)
           # get_t= partial(get_text_pc,i,j,gameboard,l1,l2)
            button[i][j] = Button(game,bd=5,height=4,width=8)
            button[i][j].grid(row=t,column=y)
    game.mainloop()
def withpc(window):
    window.destroy()
    window=Tk()
    window.title("<Tic-Tac-Toe>")
    q=Button(window,text="Player:x",width=10)
    q.grid(row=1,column=1)
    w=Button(window,text="Computer:o",width=10)
    w.grid(row=2,column=1)
    gameboard(window)
def play():
    root=Tk()
    root.title("Tic-Tac-Toe")
    root.geometry("500x500")
    r=partial(withpc,root)
    b=Button(root,text="welcome to Tic-Tac-Toe",fg="Orange",bg="Black",width=500,font="summer",bd=5)
    c=Button(root,text="Single Player",fg="White",bg="Black",width=500,font="summer",bd=5,command=r)
    d=Button(root,text="Multiplayer",fg="Cyan",bg="Black",width=500,font="summer",bd=5)
    e=Button(root,text="Exit",fg="Red",bg="Black",width=500,font="summer",bd=5)
    b.pack()
    c.pack()
    d.pack()
    e.pack()
    root.mainloop()
if __name__=="__main__":
    play()
