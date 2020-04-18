from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from login_signUp import *
from login_signUp import regnologin
from fuzzySystem import fuzzy_logics

global mat
mat = [0,0,0,0]
global eng
eng = [0,0,0,0]
global che
che = [0,0,0,0]
global phy
phy = [0,0,0,0]
global opt
opt = [0,0,0,0]


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
    print(param)

    Label(res, text = str(fuzzy_logics(int(param[1]), int(param[2]), int(param[3]), int(param[4]))),fg="black", font=('arial', 14), fill=None).place(y=30, x=50)

    res.mainloop()

def collect(subjct):
    
    
    print(str(att.get())+"   "+str(clas.get())+"   "+str(half.get())+"   "+str(fin.get()))

    if(subjct=="Maths"):
        
        mat = [clas.get(), att.get(), half.get(), fin.get()]
        print(mat)

    elif(subjct=="English"):
        
        eng = [clas.get(), att.get(), half.get(), fin.get()]
        print(eng)

    elif(subjct=="Chemistry"):
        
        che = [clas.get(), att.get(), half.get(), fin.get()]
        print(che)

    elif(subjct=="Physics"):
        
        phy = [clas.get(), att.get(), half.get(), fin.get()]
        print(phy)

    elif(subjct=="Optional"):
        
        opt = [clas.get(), att.get(), half.get(), fin.get()]
        print(opt)

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

    Label(inpt, text = "Attendance ",bg="light pink", font=('arial', 14)).place(y=140,x=40)
    att=Entry(inpt, font=('arial', 14))
    att.place(y=140,x=180)

    Label(inpt, text = "Half Term ",bg="light pink", font=('arial', 14)).place(y=200,x=40)
    half=Entry(inpt, font=('arial', 14))
    half.place(y=200,x=180)

    Label(inpt, text = "Final Term ",bg="light pink", font=('arial', 14)).place(y=260,x=40)
    fin=Entry(inpt, font=('arial', 14))
    fin.place(y=260,x=180)
    
    Button(inpt, text="Submit",command=lambda: collect(subjects), width=20, height=2).place(y=320,x=300)
    
    inpt.mainloop()

basewindow()