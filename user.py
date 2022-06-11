#import modules
import tkinter
from tkinter import *
from PIL import ImageTk,Image

window=tkinter.Tk()

window.title("VNPS Student Council Election (OASIS)")
window.geometry('1500x750')
window.configure(background='white')

#set logo
logo_set=PhotoImage(name='logo',file='logo.png')
label_logo=Label(window,image=logo_set,bd=0,relief=SUNKEN)
label_logo.place(x=-10,y=-10)

#set the main label
main_head=Label(window,text='VIDHYA NIKETAN STUDENT COUNCIL ELECTION',fg='orange',bg='white',font=('Helvetica',30,'underline'))
main_head.place(x=260,y=50)

	
def pandya():
	window.destroy()
	import PANDYA
def chera():
	window.destroy()
	import CHERA
def pallava():
	window.destroy()
	import PALLAVA
	exit()
def chola():
	window.destroy()
	import CHOLA
def spl():
	window.destroy()
	import SPL
def aspl():
	window.destroy()
	import ASPL

pandya_button_reg=PhotoImage(file='button_pandya.png')
pandya_button=Button(window,bd=0,bg='white',image=pandya_button_reg,command=pandya,relief=SUNKEN)
pandya_button.place(x=300,y=250)

pallava_button_reg=PhotoImage(file='button_pallava.png')
pallava_button=Button(window,bd=0,bg='white',image=pallava_button_reg,command=pallava,relief=SUNKEN)
pallava_button.place(x=300,y=350)

chera_button_reg=PhotoImage(file='button_chera.png')
chera_button=Button(window,bd=0,bg='white',image=chera_button_reg,command=chera,relief=SUNKEN)
chera_button.place(x=300,y=450)

chola_button_reg=PhotoImage(file='button_chola.png')
chola_button=Button(window,bd=0,bg='white',image=chola_button_reg,command=chola,relief=SUNKEN)
chola_button.place(x=300,y=550)

spl_button_reg=PhotoImage(file='button_spl.png')
spl_button=Button(window,bd=0,bg='white',image=spl_button_reg,command=spl,relief=SUNKEN)
spl_button.place(x=536,y=350)

aspl_button_reg=PhotoImage(file='button_aspl.png')
aspl_button=Button(window,bd=0,bg='white',image=aspl_button_reg,command=aspl,relief=SUNKEN)
aspl_button.place(x=536,y=450)

lbl_c=Label(window,text='OASIS Created By @white_feather',font=('Times New Roman',10))
lbl_c.place(x=550,y=670)


window.mainloop()
