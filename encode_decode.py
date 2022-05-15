import tkinter
from tkinter import *
import base64

window = Tk()
window.geometry('500x300')
window.resizable(0,0)

window.title('Text Encoder - Decoder')

Label(window,text='ENCODE DECODE',font='arial 20 bold').pack()
Label(window,text='MYSOFTWARE',font='arial 20 bold').pack(side=BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


def Encode(key,message):
    ''' To decode the message  '''
    enc=[]
    for i in range(len(message)):
        key_c = key[i%len(key)]
        enc.append(chr((ord(message[i])+ord(key_c))%256))
        
    return base64.urlsafe_b64encode(''.join(enc).encode()).decode()

def Decode(key,message):
    ''' To decode the message '''
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i%len(key)]
        dec.append(chr((256+ord(message[i])-ord(key_c))%256))
        
    return ''.join(dec)

def Mode():
    ''' To choose whether to encode or decode the message'''
    if (mode.get() =='e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif (mode.get() =='d'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')
        
def Exit():
    ''' Exit the window'''
    window.destroy()

def Reset():
    ''' to reset the entire window'''
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

Label(window,text='MESSAGE',font='arial 12 bold').place(x=60,y=60)
Entry(window,font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290,y=60)

Label(window,text='KEY',font='arial 12 bold').place(x=60,y=90)
Entry(window,font = 'arial 10', textvariable = private_key, bg = 'ghost white').place(x=290,y=90)

Label(window,text='Mode(e-endode,d-decode)',font='arial 12 bold').place(x=60,y=120)
Entry(window,font = 'arial 10', textvariable = mode,bg = 'ghost white').place(x=290,y=120)

Button(window,text='Result',font='arial 12 bold',command=Mode,padx=2,bg = 'Lightgrey').place(x=60,y=150)
Entry(window,font = 'arial 10 bold', textvariable = Result,bg = 'ghost white').place(x=290,y=150)

Button(window,text='Reset',font='arial 12 bold',command=Reset,bg = 'green',padx=2).place(x=80,y=190)

Button(window,text='Exit',font='arial 12 bold',command=Exit,bg = 'red',padx=2,pady=2).place(x=180,y=190)


window.mainloop()
