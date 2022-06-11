#import modules
import tkinter 
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector


def vote_cand1():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voting_result')
    cursor = conn.cursor()
    sql_retrieve= 'SELECT `Candidate_Name`, `Votes` FROM `chera` WHERE Candidate_Name="Name_1";'
    cursor.execute(sql_retrieve)
    result=cursor.fetchall()
    for x in result:
        x=list(x)
        print(x)
        new_val_vote=x[1]+1
        print(x[1]+1)
        sql_add= "UPDATE chera SET Votes={} WHERE Candidate_Name='Name_1';".format(new_val_vote)
        cursor.execute(sql_add)
        conn.commit()
    conn.close()


def vote_cand2():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voting_result')
    cursor = conn.cursor()
    sql_retrieve= 'SELECT `Candidate_Name`, `Votes` FROM `chera` WHERE Candidate_Name="Name_2";'
    cursor.execute(sql_retrieve)
    result=cursor.fetchall()
    for x in result:
        x=list(x)
        new_val_vote=x[1]+1
        print(x[1]+1)
        sql_add= "UPDATE chera SET Votes={} WHERE Candidate_Name='Name_2';".format(new_val_vote)
        cursor.execute(sql_add)
        conn.commit()
    conn.close()


def vote_cand3():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voting_result')
    cursor = conn.cursor()
    sql_retrieve= 'SELECT `Candidate_Name`, `Votes` FROM `chera` WHERE Candidate_Name="Name_3";'
    cursor.execute(sql_retrieve)
    result=cursor.fetchall()
    for x in result:
        x=list(x)
        new_val_vote=x[1]+1
        print(x[1]+1)
        sql_add= "UPDATE chera SET Votes={} WHERE Candidate_Name='Name_3';".format(new_val_vote)
        cursor.execute(sql_add)
        conn.commit()
    conn.close()

def vote_cand4():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voting_result')
    cursor = conn.cursor()
    sql_retrieve= 'SELECT `Candidate_Name`, `Votes` FROM `chera` WHERE Candidate_Name="Name_4";'
    cursor.execute(sql_retrieve)
    result=cursor.fetchall()
    for x in result:
        x=list(x)
        new_val_vote=x[1]+1
        print(x[1]+1)
        sql_add= "UPDATE chera SET Votes={} WHERE Candidate_Name='Name_4';".format(new_val_vote)
        cursor.execute(sql_add)
        conn.commit()
    conn.close()


def vote_cand5():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voting_result')
    cursor = conn.cursor()
    sql_retrieve= 'SELECT `Candidate_Name`, `Votes` FROM `chera` WHERE Candidate_Name="Name_5";'
    cursor.execute(sql_retrieve)
    result=cursor.fetchall()
    for x in result:
        x=list(x)
        new_val_vote=x[1]+1
        print(x[1]+1)
        sql_add= "UPDATE chera SET Votes={} WHERE Candidate_Name='Name_5';".format(new_val_vote)
        cursor.execute(sql_add)
        conn.commit()
    conn.close()


def vote_cand6():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='voting_result')
    cursor = conn.cursor()
    sql_retrieve= 'SELECT `Candidate_Name`, `Votes` FROM `chera` WHERE Candidate_Name="Name_6";'
    cursor.execute(sql_retrieve)
    result=cursor.fetchall()
    for x in result:
        x=list(x)
        new_val_vote=x[1]+1
        print(x[1]+1)
        sql_add= "UPDATE chera SET Votes={} WHERE Candidate_Name='Name_6';".format(new_val_vote)
        cursor.execute(sql_add)
        conn.commit()
    conn.close()


def back():
    window.destroy()
    import user

window=tkinter.Tk()

window.title("VNPS Chera House (OASIS)")
window.geometry('1500x750')
window.configure(background='white')

#set logo
logo_set=PhotoImage(file='logo1.png',master=window)
label_logo=Label(window,image=logo_set,bd=0,relief=SUNKEN)
label_logo.place(x=-10,y=-10)

#set the main label
main_head=Label(window,text='VIDHYA NIKETAN STUDENT COUNCIL ELECTION',fg='orange',bg='white',font=('Helvetica',30,'underline'))
main_head.place(x=260,y=50)

#first candidate
img1=Image.open("BIN/CAND_IMAGES/CHERA/img1.png")
img1=img1.resize((150,180))
img1=ImageTk.PhotoImage(img1)
lab1=Label(window,bd=1,bg='white',image=img1,relief=SUNKEN)
lab1.place(x=300,y=170)
lab1_name=Label(window,text='name',font=('Helvetica',16))
lab1_name.place(x=350,y=350)

vote_cand=PhotoImage(file='button_vote.png')
vote_cand1=Button(window,bd=0,image=vote_cand,relief=SUNKEN,command=vote_cand1)
vote_cand1.place(x=305,y=380)

#second candidate
img2=Image.open("BIN/CAND_IMAGES/CHERA/img1.png")
img2=img2.resize((150,180))
img2=ImageTk.PhotoImage(img2)
lab2=Label(window,bd=1,bg='white',image=img2,relief=SUNKEN)
lab2.place(x=600,y=170)
lab2_name=Label(window,text='name',font=('Helvetica',16))
lab2_name.place(x=650,y=350)

vote_cand2=Button(window,bd=0,image=vote_cand,relief=SUNKEN,command=vote_cand2)
vote_cand2.place(x=605,y=380)

#third candidate
img3=Image.open("BIN/CAND_IMAGES/CHERA/img1.png")
img3=img3.resize((150,180))
img3=ImageTk.PhotoImage(img3)
lab3=Label(window,bd=1,bg='white',image=img3,relief=SUNKEN)
lab3.place(x=900,y=170)
lab3_name=Label(window,text='name',font=('Helvetica',16))
lab3_name.place(x=950,y=350)

vote_cand3=Button(window,bd=0,image=vote_cand,relief=SUNKEN,command=vote_cand3)
vote_cand3.place(x=905,y=380)

#fourth candidate
img4=Image.open("BIN/CAND_IMAGES/CHERA/img1.png")
img4=img4.resize((150,180))
img4=ImageTk.PhotoImage(img4)
lab4=Label(window,bd=1,bg='white',image=img4,relief=SUNKEN)
lab4.place(x=300,y=435)
lab4_name=Label(window,text='name',font=('Helvetica',16))
lab4_name.place(x=350,y=615)

vote_cand4=Button(window,bd=0,image=vote_cand,relief=SUNKEN,command=vote_cand4)
vote_cand4.place(x=305,y=650)

#fifth candidate
img5=Image.open("BIN/CAND_IMAGES/CHERA/img1.png")
img5=img5.resize((150,180))
img5=ImageTk.PhotoImage(img5)
lab5=Label(window,bd=1,bg='white',image=img5,relief=SUNKEN)
lab5.place(x=600,y=435)
lab5_name=Label(window,text='name',font=('Helvetica',16))
lab5_name.place(x=650,y=620)

vote_cand5=Button(window,bd=0,image=vote_cand,relief=SUNKEN,command=vote_cand5)
vote_cand5.place(x=605,y=650)

#sixth candidate
img6=Image.open("BIN/CAND_IMAGES/CHERA/img1.png")
img6=img6.resize((150,180))
img6=ImageTk.PhotoImage(img6)
lab6=Label(window,bd=1,bg='white',image=img6,relief=SUNKEN)
lab6.place(x=900,y=435)
lab6_name=Label(window,text='name',font=('Helvetica',16))
lab6_name.place(x=950,y=620)

vote_cand6=Button(window,bd=0,image=vote_cand,relief=SUNKEN,command=vote_cand6)
vote_cand6.place(x=905,y=650)

back_button=PhotoImage(file='button_back.png')
back=Button(window,bd=0,image=back_button,relief=SUNKEN,command=back)
back.place(x=10,y=650)

window.mainloop()


