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
