def enter():
    try:
        a=int(input_value.get())
        b=int(input_value2.get())
        full_result=str(a/b)
        point=full_result.index('.')
        skip=full_result[point+1::]
        result.delete(1.0,END)

        if len(skip)==1:   
            text_to_display=f'{input_value.get()} is divisible by {input_value2.get()} and the result is {int(a/b)}'
            result.insert(END, text_to_display)
        
        else:
            text_to_display=F'{input_value.get()} is not divisible by {input_value2.get()}.'
            result.insert(END, text_to_display)
        
        


    
    except:
        result.insert(END, '')

        messagebox.showinfo('Info','Please Enter A VAILD Number!!!')
def GET(event):
    if input_value.get()=='Enter Value':
        input_value.set('')
        taking_input['fg']='Black'

def GET1(event):
    if input_value.get()=='':
        input_value.set('Enter Value')
        taking_input['fg']='grey'
def GET2(event):
    if input_value2.get()=='Enter Value':
        input_value2.set('')
        e1['fg']='black'
def GET3(event):
    if input_value2.get()=='':
        input_value2.set('Enter Value')
        e1['fg']='grey'
import tkinter.messagebox
from tkinter import*
root=Tk()
root.geometry('400x400')

root.title('Divisibility Calculator')

root.wm_iconbitmap('logo.ico')
root.maxsize(400,400)
r=Label(root,text="Divisibility Calculator",font=('Courier',20,'bold'),fg="black").pack()
number=Label(root,text="""Enter Number Down Below:-""",font=("Courier",15,'bold'),).place(x=45,y=45)
input_value=StringVar()
input_value2=StringVar()
input_value.set('Enter Value')
input_value2.set('Enter Value')
taking_input=Entry(root,font=('Courier',12,'bold'),textvariable=input_value,fg="grey")
taking_input.place(x=75,y=75)
Enter=Button(root,text='Enter',command=enter,font=("Courier",15,'bold'),fg="white",bg="Black").place(x=130,y=160)
taking_input.bind('<FocusIn>',GET)
taking_input.bind('<FocusOut>',GET1)
paragraph=Text(root,fg='red')
paragraph.place(x=1,y=230,height=120, width=200)
paragraph.insert(END,'''About This Calculator:- This is a divisibility 
calculator. The use 
of this calculator 
is to check the 
divisibility of a number by another number.''')
paragraph['state']='disabled'
texttt=Label(text='Divisible By:',font=("Courier",15,'bold'),)
texttt.place(x=95,y=100)
e1=Entry(root,font=('Courier',12,'bold'),textvariable=input_value2,fg="grey")
e1.place(x=75,y=130)
taking_input.bind('<FocusIn>',GET)
taking_input.bind('<FocusOut>',GET1)
e1.bind('<FocusIn>',GET2)
e1.bind('<FocusOut>',GET3)
indict=Label(root,text='Result',font=('Courier',20,'bold'))
indict.place(x=250,y=190)
result=Text(root,font=('Courier',10,'bold'),fg='red')
result.place(x=220,y=230,width=170,height=120)

mainloop()
# CHECK SPELLS