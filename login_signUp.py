
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from homeWindow import *
from fuzzySystem import fuzzy_logics

def login():
    global imglabel
    global regnologin
    global password
    global img
    
    imglabel = Tk()
    imglabel.title("Student Grading System")

    imglabel.configure(background='light blue')
    bg_image = Image.open("GPA11.png")
    image = ImageTk.PhotoImage(bg_image)
    img = Label(imglabel, image = image)
    img.image = image
    img.pack(fill='both', expand=True)
    imglabel.geometry("600x400")
    large_font = ('Verdana',20)

    regnologin = StringVar()
    password = StringVar()

    Label(img, text = "Enter username and password below",fg="black", font=large_font, fill=None).place(y=50, x=50)

    Label(img, text = "Reg Id ",bg="light pink", padx=10, pady=10).place(y=120,x=40)
    e1 = Entry(img, textvariable=regnologin,font=large_font).place(y=120,x=120)

    Label(img, text = "Password ",bg="light pink",padx=10, pady=10).place(y=200,x=40)
    e2 = Entry(img, textvariable=password, show='*',font=large_font).place(y=200,x=120)

    Button(img, text="Register",command=register, width=10, height=1, padx=5, pady=5).place(y=280,x=120)
    Button(img, text="Login",command=verify, width=10, height=1, padx=5, pady=5).place(y=280,x=300)

    imglabel.mainloop()


def verify():
    database()
    loginparams = (str(regnologin.get()), str(password.get()))
    cursor.execute("SELECT * from studentInfo")
    rows = cursor.fetchall()
    regdb = [row[0] for row in rows]
    passdb = [row[2] for row in rows]
    conn.commit()
    

    if (loginparams[0] in regdb) and (loginparams[1] in passdb):
        #funcName()
        imglabel.destroy()
        basewindow(regnologin)
    else:
        Label(img, text = "Enter again",fg="black").place(y=350, x=100)



def Back():
    regt.destroy()
    login()

def regback():
    database()
    params = (str(regno.get()), str(newname.get()), str(newpass.get()))
    cursor.execute("INSERT INTO 'studentInfo' (student_id, username, password) VALUES(?,?,?)", params)
    conn.commit()
    conn.close()
    regt.destroy()
    login()


    
def register():
    
    global newname
    global newpass
    global regt
    global regno
   
    imglabel.destroy()
    regt = Tk()

    bg_reg = Image.open("GPA11.png")
    image = ImageTk.PhotoImage(bg_reg)
    imgreg = Label(regt, image = image)
    imgreg.image = image
    imgreg.pack(fill='both', expand=True)

    regt.title("Sign Up")
    regt.geometry("600x450")
    
    newname = StringVar()
    newpass = StringVar()
    regno = StringVar()
    
    lbl_title = Label(imgreg, text = " Login Application", font=('arial', 15)).place(y=50, x=50)

    lbl_username = Label(imgreg, text = "Username:", font=('arial', 14), padx=10, pady=10).place(y=100,x=40)
    user1 = Entry(imgreg, textvariable=newname, font=('arial', 14)).place(y=100,x=200)

    lbl_regno = Label(imgreg, text = "Reg No:", font=('arial', 14), padx=10, pady=10).place(y=200,x=40)
    regno1 = Entry(imgreg, textvariable=regno, font=('arial', 14)).place(y=200,x=200)

    lbl_password = Label(imgreg, text = "Password:", font=('arial', 14), padx=10, pady=10).place(y=300,x=40)
    passw1 = Entry(imgreg, textvariable=newpass, show="*", font=('arial', 14)).place(y=300,x=200)

    Button(imgreg, text="Back", width=10, command=Back, padx=5, pady=5).place(y=380,x=120)
    Button(imgreg, text="Register", width=10, command=regback, padx=5, pady=5).place(y=380,x=280)
    

    lbl_text = Label(imgreg).place(y=300, x=150)
    

    if newname.get() == "" or newpass.get() == "" or regno.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")

    regt.mainloop()


def database():
    global conn, cursor
    conn = sqlite3.connect("studentDetails.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'studentInfo' (student_id TEXT NOT NULL PRIMARY KEY, username TEXT, password TEXT)")



def deleteUser():
    pass

login()
