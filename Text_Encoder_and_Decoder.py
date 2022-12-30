
#import tkinker module and others
from tkinter import *
import random
import time
import datetime

#creating root object
root = Tk()
# defining size of window
root.geometry("1200x6000")
root['background'] = '#32a8a2'
#setting up title of window
root.title("Message Encoder And Decoder")
Tops = Frame(root, width = 1600, relief= SUNKEN)
Tops.pack(side='top')
f1 = Frame(root, width= 800, height= 700, relief = SUNKEN)
f1.pack(side = LEFT)


# =============
#       TIME
# =============
localtime = time.asctime(time.localtime(time.time()))

label_info = Label(Tops, font = ('helvetica', 40, 'italic', 'bold'),
            text="MESSAGE ENCODER/DECODER\n vigenere cipher", fg="#7a4653", bd=10, anchor='w')
label_info.grid(row = 0, column=0)
label_info = Label(Tops, font = ('arial', 20, 'italic'),
            text=localtime, fg="Steel Blue", bd=10, anchor='w')
label_info.grid(row= 1, column= 0)


rand= StringVar()
Msg = StringVar()
key = StringVar()
mode =StringVar()
Result = StringVar()

#exit function
def qExit():
    root.destroy()
#function to reset window
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")
#reference
label_Ref = Label(f1, font=('arial', 16, 'bold'),
            text = "Name:", bd = 16, anchor= "w")
label_Ref.grid(row = 0, column= 0)
txtReference = Entry(f1, font = ('arial', 16, 'bold'),
                textvariable =rand, bd = 10, insertwidth = 4,
                    bg ='powder blue', justify = 'right')
txtReference.grid(row=0, column=1)

#labels

label_Msg =Label(f1, font=('arial', 16, 'bold'),
            text = "MESSAGE", bd = 16, anchor= "w")
label_Msg.grid(row =1 , column=0)

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
            textvariable =Msg, bd = 10, insertwidth = 4,
                bg ='powder blue', justify = 'right')
txtMsg.grid(row=1, column=1)

label_key =Label(f1, font=('arial', 16, 'bold'),
            text = "KEY", bd = 16, anchor= "w")
label_key.grid(row =2 , column=0)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),
                textvariable =key, bd = 10, insertwidth = 4,
                    bg ='powder blue', justify = 'right')
txtkey.grid(row=2, column=1)

label_mode =Label(f1, font=('arial', 16, 'bold'),
            text = "MODE(e for encrypt, d for decrypt) ", bd = 16, anchor= "w")
label_mode.grid(row =3 , column=0)

txtmode = Entry(f1, font = ('arial', 16, 'bold'),
                textvariable =mode, bd = 10, insertwidth = 4,
                    bg ='powder blue', justify = 'right')
txtmode.grid(row=3, column=1)

label_service =Label(f1, font=('arial', 16, 'bold'),
            text = "The Result", bd = 16, anchor= "w")
label_service.grid(row =2 , column=2)

txtservice = Entry(f1, font = ('arial', 16, 'bold'),
                textvariable =Result, bd = 10, insertwidth = 4,
                    bg ='powder blue', justify = 'right')
txtservice.grid(row=2, column=3)

label_footer = Label(f1,padx=8, pady=4, font = ('arial', 14, 'italic'),
            text="Implemented By:\n Abdul(softClaws).", fg="#49658a", bd=10, anchor='w').grid(row=8, column=3)

#Vigenere cipher
import base64
#function to encode
def encode(key, clear):
    enc =[]
    for i in range(len(clear)):
        key_c = key[i% len(key)]
        enc_c = chr(ord(clear[i]) + ord(key_c)%256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode
def decode(key, enc):
    dec =[]
    enc = base64.urlsafe_b64encode(enc).decode()
    for i in range (len(enc)):
        key_c = key[i%len(key)]
        dec_c = chr((256 + ord(enc[i])- ord(key_c))%256)
        dec.append(dec_c)
    return "".join(dec)

def Ref():
    print("Message = ", (Msg.get()))
    clear = Msg.get()
    k = key.get()
    m = mode.get()
    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))

#Show message button
btnTotal = Button(f1, padx=16, pady=8, bd = 16, fg ="black",
                font = ('arial', 16, 'bold'), width =10,
                text = "Show Message", command = Ref,
                    bg ='powder blue').grid(row = 7, column=1)

#Show Reset button
btnReset = Button(f1, padx=16, pady=8, bd = 16, fg ="black",
                font = ('arial', 16, 'bold'), width =10,
                text = "Reset", command = Reset,
                    bg ='green').grid(row = 7, column=2)

#Show Exit button
btnTotal = Button(f1, padx=16, pady=8, bd = 16, fg ="black",
                font = ('arial', 16, 'bold'), width =10,
                text = "Exit", command = qExit,
                    bg ='red').grid(row = 7, column=3)

#keeps window alive
root.mainloop()