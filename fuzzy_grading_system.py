
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from fuzzySystem import fuzzy_logics
from tkinter import messagebox

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
        basewindow()
    else:
        #Label(img, text = "Enter again",fg="black").place(y=350, x=100)
        messagebox.showinfo("Wrong Credentials", "Wrong User Id or Password")


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
    regt.geometry("600x400")
    
    newname = StringVar()
    newpass = StringVar()
    regno = StringVar()
    
    lbl_title = Label(imgreg, text = " Login Application", font=('arial', 15)).place(y=50, x=50)

    lbl_username = Label(imgreg, text = "Username:", font=('arial', 14), padx=10, pady=10).place(y=90,x=40)
    user1 = Entry(imgreg, textvariable=newname, font=('arial', 14)).place(y=90,x=200)

    lbl_regno = Label(imgreg, text = "Reg No:", font=('arial', 14), padx=10, pady=10).place(y=180,x=40)
    regno1 = Entry(imgreg, textvariable=regno, font=('arial', 14)).place(y=180,x=200)
 
    lbl_password = Label(imgreg, text = "Password:", font=('arial', 14), padx=10, pady=10).place(y=270,x=40)
    passw1 = Entry(imgreg, textvariable=newpass, show="*", font=('arial', 14)).place(y=270,x=200)

    Button(imgreg, text="Back", width=10, command=Back, padx=5, pady=5).place(y=340,x=120)
    Button(imgreg, text="Register", width=10, command=regback, padx=5, pady=5).place(y=340,x=280)
    

    lbl_text = Label(imgreg).place(y=300, x=150)

    regt.mainloop()


def database():
    global conn, cursor
    conn = sqlite3.connect("studentDetails.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'studentInfo' (student_id TEXT NOT NULL PRIMARY KEY, username TEXT, password TEXT)")


def basewindow():
    
    home = Tk()

    database()
    cursor.execute("SELECT * FROM studentInfo WHERE student_id=?", (str(regnologin.get()),))
    det = cursor.fetchone()

    bg_home = Image.open("GPA11.png")
    image = ImageTk.PhotoImage(bg_home)
    imghome = Label(home, image = image)
    imghome.image = image
    imghome.pack(fill='both', expand=True)

    home.title("Grading System")
    home.geometry("600x400")
    
    Label(imghome, text = f"Hello, {det[1]}",fg="black", font=('arial', 14), fill=None).place(y=50, x=50)
    Label(imghome, text = "Fill subject marks to find CGPA",fg="black", font=('arial', 14), fill=None).place(y=100, x=50)

    Button(imghome, text="Maths",command=lambda: inputmarks("Maths"), width=10, height=1, padx=5, pady=5).place(y=150,x=100)
    Button(imghome, text="English",command=lambda: inputmarks("English"), width=10, height=1, padx=5, pady=5).place(y=150,x=240)
    Button(imghome, text="Chemistry",command=lambda: inputmarks("Chemistry"), width=10, height=1, padx=5, pady=5).place(y=200,x=100)
    Button(imghome, text="Physics",command=lambda: inputmarks("Physics"), width=10, height=1, padx=5, pady=5).place(y=200,x=240)
    Button(imghome, text="Optional",command=lambda: inputmarks("Optional"), width=10, height=1, padx=5, pady=5).place(y=250,x=100)

    Button(imghome, text="Find CGPA",command=result, width=20, height=2).place(y=280,x=350)

    home.mainloop()


def marksdatabase():
    global conn1, cursor1
    conn1 = sqlite3.connect("studentMarks.db")
    cursor1 = conn1.cursor()
    cursor1.execute("CREATE TABLE IF NOT EXISTS 'studentMark' (student_id TEXT NOT NULL PRIMARY KEY, ca TEXT, attendance TEXT, halfTerm TEXT, finalTerm TEXT)")


def result():

    marksdatabase()
    param = (str(regnologin.get()), str((mat[0]+eng[0]+che[0]+phy[0]+opt[0])//5), str((mat[1]+eng[1]+che[1]+phy[1]+opt[1])//5), str((mat[2]+eng[2]+che[2]+phy[2]+opt[2])//5), str((mat[3]+eng[3]+che[3]+phy[3]+opt[3])//5))
    cursor1.execute("INSERT INTO 'studentMark' (student_id, ca, attendance, halfTerm, finalTerm) VALUES(?,?,?,?,?)", param)
    conn1.commit()
    conn1.close()

    res = Tk()
    res.title("Result CGPA")
    res.geometry("600x400")
    #print(param)

    Label(res, text = "CGPA : " + str(fuzzy_logics(int(param[1]), int(param[2]), int(param[3]), int(param[4]))),fg="black", font=('arial', 30), fill=None).place(y=100, x=170)

    res.mainloop()

def collect(subjct):
    
    global mat
    global eng
    global che
    global phy
    global opt
    

    if(subjct=="Maths"):
        
        mat = [int(clas.get()), int(att.get()), int(half.get()), int(fin.get())]
        #print(mat)

    elif(subjct=="English"):
        
        eng = [int(clas.get()), int(att.get()), int(half.get()), int(fin.get())]
        #print(eng)

    elif(subjct=="Chemistry"):
        
        che = [int(clas.get()), int(att.get()), int(half.get()), int(fin.get())]
        #print(che)

    elif(subjct=="Physics"):
        
        phy = [int(clas.get()), int(att.get()), int(half.get()), int(fin.get())]
        #print(phy)

    elif(subjct=="Optional"):
        
        opt = [int(clas.get()), int(att.get()), int(half.get()), int(fin.get())]
        #print(opt)

    inpt.destroy()

def inputmarks(subjects):

    global att
    global fin
    global half
    global clas

    att = IntVar()
    fin = IntVar()
    half = IntVar()
    clas = IntVar()
    global inpt

    inpt = Tk()

    inpt.title(subjects)
    inpt.geometry("600x400")

    Label(inpt, text = "Enter Marks",fg="black", font=('arial', 14), fill=None).place(y=30, x=50)

    Label(inpt, text = "Class Test ",bg="light pink", font=('arial', 14)).place(y=80,x=40)
    clas=Entry(inpt, font=('arial', 14))
    clas.place(y=80,x=180)
    Label(inpt, text = "/30 ", font=('arial', 14)).place(y=80,x=410)

    Label(inpt, text = "Attendance ",bg="light pink", font=('arial', 14)).place(y=140,x=40)
    att=Entry(inpt, font=('arial', 14))
    att.place(y=140,x=180)
    Label(inpt, text = "/100 ", font=('arial', 14)).place(y=140,x=410)

    Label(inpt, text = "Half Term ",bg="light pink", font=('arial', 14)).place(y=200,x=40)
    half=Entry(inpt, font=('arial', 14))
    half.place(y=200,x=180)
    Label(inpt, text = "/50 ", font=('arial', 14)).place(y=200,x=410)

    Label(inpt, text = "Final Term ",bg="light pink", font=('arial', 14)).place(y=260,x=40)
    fin=Entry(inpt, font=('arial', 14))
    fin.place(y=260,x=180)
    Label(inpt, text = "/100 ", font=('arial', 14)).place(y=260,x=410)
    
    Button(inpt, text="Submit",command=lambda: collect(subjects), width=20, height=2).place(y=320,x=300)
    
    inpt.mainloop()

login()
