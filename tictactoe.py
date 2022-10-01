from tkinter import *
import tkinter.messagebox
main_window=Tk()
main_window.title("Tic-Tac-Toe")
main_window.geometry("540x590")
main_window.resizable(False, False)
k=1
count=0
my_font=('Segoe UI Historic',11,'bold')
my_font1=('Adobe Hebrew',10,'bold')
def clearbuttons():
    B1['text']=''
    B1.configure(bg='SystemButtonFace')
    B2['text']=''
    B2.configure(bg='SystemButtonFace')
    B3['text']=''
    B3.configure(bg='SystemButtonFace')
    B4['text']=''
    B4.configure(bg='SystemButtonFace')
    B5['text']=''
    B5.configure(bg='SystemButtonFace')
    B6['text']=''
    B6.configure(bg='SystemButtonFace')
    B7['text']=''
    B7.configure(bg='SystemButtonFace')
    B8['text']=''
    B8.configure(bg='SystemButtonFace')
    B9['text']=''
    B9.configure(bg='SystemButtonFace')
def checking():
    global k,count
    if((B1['text']=='X' and B2['text']=='X' and B3['text']=='X') or (B2['text']=="X" and B5['text']=='X' and B8['text']=='X')
    or (B1['text']=='X' and B4['text']=='X' and B7['text']=='X') or (B3['text']=='X'and B6['text']=='X' and B9['text']=='X')
    or (B1['text']=='X' and B5['text']=='X' and B9['text']=='X') or (B3['text']=='X'and B5['text']=='X' and B7['text']=='X')
    or (B4['text']=='X' and B5['text']=='X' and B6['text']=='X') or (B7['text']=='X'and B8['text']=='X' and B9['text']=='X')):
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Congrats!! X IS THE WINNER")
        k=1
        count=0
        clearbuttons()
    elif((B1['text']=='O' and B2['text']=='O' and B3['text']=='O') or (B2['text']=="O" and B5['text']=='O' and B8['text']=='O')
    or (B1['text']=='O' and B4['text']=='O' and B7['text']=='O') or (B3['text']=='O'and B6['text']=='O' and B9['text']=='O')
    or (B1['text']=='O' and B5['text']=='O' and B9['text']=='O') or (B3['text']=='O'and B5['text']=='O' and B7['text']=='O')
    or (B4['text']=='O' and B5['text']=='O' and B6['text']=='O') or (B7['text']=='O'and B8['text']=='O' and B9['text']=='O')):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Congrats!! O IS THE WINNER")
        k=1
        count=0
        clearbuttons()
    elif(count==9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Oh!! Its a Tie Game")
        k=1
        count=0
        clearbuttons()
def cliking(B):
    global k,count
    if(B['text']==''):
        if(k):
            B['text']='X'
            k=0
            count=count+1
            B.configure(bg='#63f2eb')
        else:
            B['text']='O'
            k=1
            count=count+1
            B.configure(bg='#FF69B4')
    if(count>=5):
        checking()
B1=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B1),font=my_font)
B2=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B2),font=my_font)
B3=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B3),font=my_font)
B4=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B4),font=my_font)
B5=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B5),font=my_font)
B6=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B6),font=my_font)
B7=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B7),font=my_font)
B8=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B8),font=my_font)
B9=Button(main_window,text="",height=8,width=19,command=lambda:cliking(B9),font=my_font)
B1.grid(row=0,column=0)
B2.grid(row=0,column=1)
B3.grid(row=0,column=2)
B4.grid(row=1,column=0)
B5.grid(row=1,column=1)
B6.grid(row=1,column=2)
B7.grid(row=2,column=0)
B8.grid(row=2,column=1)
B9.grid(row=2,column=2)
Label(main_window,text="Player 1 is X,Player 2 is O",font=my_font1).grid(row=4,column=1)
end=Button(main_window,text="End Game",command=main_window.destroy,bg='orange',font=my_font)
end.grid(row=5,column=1)
main_window.mainloop()