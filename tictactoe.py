from tkinter import*
from functools import partial
from tkinter import messagebox
from copy import deepcopy
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
    global u
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

def get_textpc(i,j,l1,l2,k):
    global u
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
    asd=True

    if winner(board,"x"):
        k.destroy()
        asd=False
        messagebox.showinfo("Winner","Player 1 won the match")

    elif winner(board,"o"):
        k.destroy()
        asd=False
        messagebox.showinfo("Winner","Player 2 won the match")

    elif isfull():
        k.destroy()
        asd=False
        messagebox.showinfo("Tie game")  
    if asd:
        if u%2!=0:
           move=pc()
           button[move[0]][move[1]].config(stat=DISABLED)
           get_textpc(move[0],move[1],l1,l2,k)

def isfull():
    flag=True
    for i in board:
        if i.count(' ')>0:
            flag=False
    return flag
def isfree(i,j):
    return board[i][j]==" "

def gameboard(game,l1,l2):
    global button 
    button=[]
    for i in range(3):
        t=3+i
        button.append(i)
        button[i]=[]
        for j in range(3):
            y=j
            button[i].append(j)
            get_t= partial(get_text,i,j,l1,l2,game)
            button[i][j] = Button(game,bd=5,height=4,width=8,command=get_t)
            button[i][j].grid(row=t,column=y)
    game.mainloop()
def gameboardpc(game,l1,l2):
    global button 
    button=[]
    for i in range(3):
        t=3+i
        button.append(i)
        button[i]=[]
        for j in range(3):
            y=j
            button[i].append(j)
            get_t= partial(get_textpc,i,j,l1,l2,game)
            button[i][j] = Button(game,bd=5,height=4,width=8,command=get_t)
            button[i][j].grid(row=t,column=y)
    game.mainloop()
def pc():
    possiblemove=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]

def withpc(window):
    window.destroy()
    window=Tk()
    window.title("<Tic-Tac-Toe>")
    l1=Button(window,text="Player:x",width=10)
    l1.grid(row=1,column=1)
    l2=Button(window,text="Computer:o",width=10,state=DISABLED)
    l2.grid(row=2,column=1)

    gameboardpc(window,l1,l2)
#gameboardpc
def withplayer(window):
    window.destroy()
    window=Tk()
    window.title("<Tic-Tac-Toe>")
    l1=Button(window,text="Player1:x",width=10)
    l1.grid(row=1,column=1)
    l2=Button(window,text="Player2:o",width=10,state=DISABLED)
    l2.grid(row=2,column=1)

    gameboard(window,l1,l2)


def play():
    root=Tk()
    root.title("Tic-Tac-Toe")
    root.geometry("500x500")
    r=partial(withpc,root)
    m=partial(withplayer,root)
    b=Button(root,text="welcome to Tic-Tac-Toe",fg="Orange",bg="Black",width=500,font="summer",bd=5)
    c=Button(root,text="Single Player",fg="White",bg="Black",width=500,font="summer",bd=5,command=r)
    d=Button(root,text="Multiplayer",fg="Cyan",bg="Black",width=500,font="summer",bd=5,command=m)
    e=Button(root,text="Exit",fg="Red",bg="Black",width=500,font="summer",bd=5,command=root.quit)
    b.pack()
    c.pack()
    d.pack()
    e.pack()
    root.mainloop()
if __name__=="__main__":
    play() #confi
