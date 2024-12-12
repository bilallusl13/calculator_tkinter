from tkinter import *
import tkinter

w=Tk()
w.geometry("600x600+100+200")
w.title("calculator")
w.resizable(False,False)
w.configure(bg="black")


label_result=Label(w,height='2',width='25',font=('arial',30,'bold'),text="")
label_result.pack()
equation=""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
def clear():
    global equation
    equation=""
    label_result.config(text="")
def calculate():

    global equation
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation="" 
    label_result.config(text=result)



    
Button(w,width=5,height=1,text="c",font=('arial',30,'bold'),bd=13,fg='white',bg='#000080',command=lambda:clear()).place(x=10,y=100)
Button(w,width=5,height=1,text="/",font=('arial',30,'bold'),bd=13,fg='white',bg='#000080',command=lambda: show("/")).place(x=158,y=100)
Button(w,width=5,height=1,text="%",font=('arial',30,'bold'),bd=13,fg='white',bg='#000080',command=lambda: show("%")).place(x=308,y=100)
Button(w,width=5,height=1,text="*",font=('arial',30,'bold'),bd=11,fg='white',bg='#000080',command=lambda: show("*")).place(x=450,y=100)
Button(w,width=5,height=1,text="7",font=('arial',30,'bold'),bd=8,fg='white',bg='#000080',command=lambda: show("7")).place(x=10,y=200)
Button(w,width=5,height=1,text="8",font=('arial',30,'bold'),bd=8,fg='white',bg='#000080',command=lambda: show("8")).place(x=158,y=200)
Button(w,width=5,height=1,text="9",font=('arial',30,'bold'),bd=8,fg='white',bg='#000080',command=lambda: show("9")).place(x=308,y=200)
Button(w,width=5,height=1,text="-",font=('arial',30,'bold'),bd=8,fg='white',bg='#000080',command=lambda: show("-")).place(x=450,y=200)
Button(w,width=5,height=1,text="4",font=('arial',30,'bold'),bd=9,fg='white',bg='#000080',command=lambda: show("4")).place(x=10,y=300)
Button(w,width=5,height=1,text="5",font=('arial',30,'bold'),bd=9,fg='white',bg='#000080',command=lambda: show("5")).place(x=158,y=300)
Button(w,width=5,height=1,text="6",font=('arial',30,'bold'),bd=9,fg='white',bg='#000080',command=lambda: show("6")).place(x=308,y=300)
Button(w,width=5,height=1,text="+",font=('arial',30,'bold'),bd=10,fg='white',bg='#000080',command=lambda: show("+")).place(x=450,y=300)
Button(w,width=5,height=1,text="1",font=('arial',30,'bold'),bd=10,fg='white',bg='#000080',command=lambda: show("1")).place(x=10,y=400)
Button(w,width=5,height=1,text="2",font=('arial',30,'bold'),bd=10,fg='white',bg='#000080',command=lambda: show("2")).place(x=158,y=400)
Button(w,width=5,height=1,text="3",font=('arial',30,'bold'),bd=10,fg='white',bg='#000080',command=lambda: show("3")).place(x=308,y=400)
Button(w,width=10,height=1,text="0",font=('arial',30,'bold'),bd=1,fg='white',bg='#000080',command=lambda: show("0")).place(x=10,y=500)
Button(w,width=7,height=1,text=".",font=('arial',30,'bold'),bd=1,fg='white',bg='#000080',command=lambda: show(".")).place(x=270,y=500)
Button(w,width=5,height=4,text="=",font=('arial',30,'bold'),bd=1,fg='white',bg='#000080',command=lambda: calculate()).place(x=450,y=400)

w.mainloop()