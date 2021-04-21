from tkinter import *
import os
import math

def clk(num):
    global op
    op+=str(num)
    text_input.set(op)
def clear():
    global op
    op=''
    text_input.set('')
    
def eq():
    global op
    result=str(eval(op))
    text_input.set(result)
    op=''
    
window=Tk()
op=''
text_input=StringVar()
window.title('Calculator')
window.geometry('400x360')
window.configure(background='black')

label1=Label(window,text='CALCULATOR',height=2,width=15,bg='light blue')
label1.place(x=150,y=20)

b0=Button(window,text='0',width=8,height=1,command=lambda:clk(1),bg='light blue')
b0.place(x=200,y=128)

b1=Button(window,text='1',width=8,height=1,command=lambda:clk(1),bg='light blue')
b1.place(x=40,y=180)

b2=Button(window,text='2',width=8,height=1,command=lambda:clk(2),bg='light blue')
b2.place(x=120,y=180)

b3=Button(window,text='3',width=8,height=1,bg='light blue',command=lambda:clk(3))
b3.place(x=200,y=180)

b4=Button(window,text='4',width=8,height=1,bg='light blue',command=lambda:clk(4))
b4.place(x=40,y=230)

b5=Button(window,text='5',width=8,height=1,bg='light blue',command=lambda:clk(5))
b5.place(x=120,y=230)

b6=Button(window,text='6',width=8,height=1,bg='light blue',command=lambda:clk(6))
b6.place(x=200,y=230)

b7=Button(window,text='7',width=8,height=1,bg='light blue',command=lambda:clk(7))
b7.place(x=40,y=280)

b8=Button(window,text='8',width=8,height=1,bg='light blue',command=lambda:clk(8))
b8.place(x=120,y=280)

b9=Button(window,text='9',width=8,height=1,bg='light blue',command=lambda:clk(9))
b9.place(x=200,y=280)

add=Button(window,text='+',width=5,height=1,bg='grey',command=lambda:clk('+'),font=('bold'))
add.place(x=280,y=120)

sub=Button(window,text='-',width=5,height=1,bg='grey',command=lambda:clk('-'),font=('bold'))
sub.place(x=280,y=170)

mul=Button(window,text='*',width=5,height=1,bg='grey',command=lambda:clk('*'),font=('bold'))
mul.place(x=280,y=220)

div=Button(window,text='/',width=5,height=1,bg='grey',command=lambda:clk('/'),font=('bold'))
div.place(x=280,y=270)

cl=Button(window,text='C',width=5,height=1,bg='red',command=clear,font=('bold'))
cl.place(x=40,y=120)

equal=Button(window,text='=',width=5,height=1,bg='light green',command=eq,font=('bold'))
equal.place(x=120,y=120)

display=Entry(window,bg='light green',width=50,textvariable=text_input,justify='right')
display.place(x=40,y=80)

window.resizable(0,0)
window.mainloop()

#Made by Dilpreet kaur
