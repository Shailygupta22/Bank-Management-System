
from datetime import datetime
from tkinter import *
from PIL import Image ,ImageTk
from tkinter import messagebox as ms
import re
## database entry
import sqlite3 as s
d=s.connect("Bank.db")
k=d.cursor()
password_visibility=False
def start():
    global w1,img
    try:
        w2.destroy()
    except:
        pass
    w1 = Tk()
    w1.title("Bank Management")
    w1.geometry("1000x1000")
    w1.config(bg='steel blue1')
    w1.attributes('-fullscreen',True)
    img=Image.open('2back-removebg-preview.png')
    img = img.resize((300, 250))
    photo=ImageTk.PhotoImage(image=img)
    l1=Label(w1,image=photo,bd=0,bg=w1['bg'])
    l1.place(x=600,y=70)
    w1.bind_all("<Escape>", lambda e: w1.attributes('-fullscreen',False))
    img1=Image.open('gesture.png')
    img1 = img1.resize((200, 200))
    photo1=ImageTk.PhotoImage(image=img1)
    l2=Label(w1,image=photo1,bd=0,bg=w1['bg'])
    l2.place(x=200,y=250)
    l1=Label(w1, text="Welcome to the Secure trust Bank of India",font=('arial',30,'bold','underline'),bg='steel blue1',fg='navy')
    l1.place(x=420,y=300)
    l2=Label(w1,text='Your Trust, Our Commitment',font=('arial',25,'bold'),bg='steel blue1',fg='snow')
    l2.place(x=570,y=360)
    img2 = Image.open('start.png')
    img2 = img2.resize((200, 200))
    photo2 = ImageTk.PhotoImage(image=img2)
    b1=Button(w1,image=photo2,bd=0,bg=w1['bg'],command=accountype,font=('arial',20,'bold'),fg='black',activebackground=w1['bg'])
    b1.place(x=660,y=450)
    w1.mainloop()
def accountype():
    global w2
    try:
        w1.destroy()
    except:
        pass
    try:
        w5.destroy()
    except:
        pass
    try:
        w6.destroy()
    except:
        pass
    try:
        w7.destroy()
    except:
        pass
    try:
        w3.destroy()
    except:
        pass
    w2=Tk()
    w2.title('account type')
    w2.geometry('1000x1000')
    w2.config(bg='steel blue1')
    w2.attributes('-fullscreen',True)
    w2.bind_all("<Escape>",lambda e:w2.attributes('-fullscreen',False))
    img1 = Image.open('bank logo2.png')
    img1 = img1.resize((80, 80))
    photo1 = ImageTk.PhotoImage(image=img1)
    l1=Label(w2,image=photo1,bd=0,bg='steel blue1')
    l1.place(x=450,y=100)
    l1=Label(w2,text='Secure Trust bank',font=('arial',40,'bold','underline'),bg='steelblue1',fg='navy')
    l1.place(x=550,y=100)
    l2=Label(w2,text='Choose your account type',font=('arial',30,'bold'),bg='steel blue1',fg='snow')
    l2.place(x=520,y=200)
    img2 = Image.open('new user.png')
    img2 = img2.resize((150, 150))
    photo2 = ImageTk.PhotoImage(image=img2)
    b1 = Button(w2, image=photo2, bd=0, bg=w2['bg'], command=Registration,  activebackground=w2['bg'])
    b1.place(x=250, y=400)
    l3 = Label(w2, text='New user registration', font=('arial', 15, 'bold'), bg='steel blue1', fg='navy')
    l3.place(x=230, y=550)
    img3 = Image.open('login (1).png')
    img3 = img3.resize((150, 150))
    photo3 = ImageTk.PhotoImage(image=img3)
    b2=Button(w2,image=photo3,bd=0,bg=w2['bg'],command=login,activebackground=w2['bg'])
    b2.place(x=540,y=400)
    l4 = Label(w2, text='Login', font=('arial', 15, 'bold'), bg='steel blue1', fg='navy')
    l4.place(x=580, y=550)
    img4 = Image.open('new-employee.png')
    img4 = img4.resize((150, 150))
    photo4 = ImageTk.PhotoImage(image=img4)
    b3 = Button(w2, image=photo4, command=employeelogin ,bd=0, bg=w2['bg'], activebackground=w2['bg'])
    b3.place(x=840, y=400)
    l4 = Label(w2, text='Employee login', font=('arial', 15, 'bold'), bg='steel blue1', fg='navy')
    l4.place(x=835, y=550)
    img5 = Image.open('admin.png')
    img5 = img5.resize((150, 150))
    photo5 = ImageTk.PhotoImage(image=img5)
    b4 = Button(w2, image=photo5, command=adminlogin, bd=0, bg=w2['bg'], activebackground=w2['bg'])
    b4.place(x=1150, y=400)
    l5=Label(w2,text='Admin login' ,font=('arial',15,'bold'),bg='steel blue1', fg='navy')
    l5.place(x=1180, y=550)
    w2.mainloop()
def Registration():
    global w3
    try:
        w2.destroy()
    except:
        pass
    try:
        w3.destroy()
    except:
        pass
    w3=Tk()
    w3.title('user login')
    w3.geometry('1000x1000')
    w3.config(bg='steel blue1')
    w3.attributes('-fullscreen',True)
    w3.bind_all("<Escape>",lambda e:w3.attributes('-fullscreen',False))
    img1 = Image.open('bank logo2.png')
    img1 = img1.resize((80, 80))
    photo1 = ImageTk.PhotoImage(image=img1)
    l1 = Label(w3, image=photo1, bd=0, bg='steel blue1')
    l1.place(x=450, y=70)
    l2 = Label(w3, text='Secure Trust bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=550, y=70)
    l2=Label(w3,text='Create Your Account',font=('arial',30,'bold'),bg='steel blue1',fg='snow')
    l2.place(x=600,y=150)
    l3=Label(w3,text='First Name:',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l3.place(x=230,y=250)
    l4=Label(w3,text='Last Name:',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l4.place(x=720,y=250)
    l5=Label(w3,text='DOB: ',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l5.place(x=230,y=350)
    l6=Label(w3,text='Email id:',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l6.place(x=230,y=450)
    l7=Label(w3,text='mobile no.:',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l7.place(x=720,y=350)
    l8=Label(w3,text='Create password:',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l8.place(x=720,y=450)
    e1=Entry(w3,font=('times new roman',20))
    e1.place(x=400,y=250)
    e2=Entry(w3,font=('times new roman',20))
    e2.place(x=980,y=250)
    e3=Entry(w3,font=('times new roman',20))
    e3.place(x=400,y=350)
    e4=Entry(w3,font=('times new roman',20))
    e4.place(x=400,y=450)
    e5=Entry(w3,font=('times new roman',20))
    e5.place(x=980,y=350)
    e6=Entry(w3,font=('times new roman',20),show='*')
    e6.place(x=980,y=450)
    try:
        k.execute("create table User_data1(First_name varchar(28),Last_name varchar(28),DOB varchar(10), Email_id varchar(30),mobile_no int,password int)")
        
    except:
        pass
    def validation():
        fn=e1.get()
        ln=e2.get()
        DOb=e3.get()
        em=e4.get()
        mob=e5.get()
        pw=e6.get()
        if fn=='':
            ms.showerror('Alert',"can't run without first name")
        elif ln=='':
            ms.showerror('Alert',"can't run without last name")
        elif DOb=='':
            ms.showerror('Alert',"cant't run without Dob")
        elif not re.search(r'^\w+@\w+\.[a-z]{2,3}$',e4.get()):
            ms.showerror('Alert',"cant't run without email")
        elif mob=='':
            ms.showerror('Alert',"cant't run without mobile no.")
        elif pw=='':
            ms.showerror('Alert',"cant't run without password")
        else:
            k.execute("insert into User_data1 (First_name,Last_name,DOB,Email_id,mobile_no,password) values(?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),int(e5.get()),int(e6.get())))
            d.commit()
            ms.showinfo("Success","Registration Successful")
            login()
    try:
        img2 = Image.open('back.png')
        img2 = img2.resize((250, 250))
        photo2 = ImageTk.PhotoImage(image=img2)
        b1 = Button(w3, image=photo2, bd=0, bg=w3['bg'], command=accountype, fg='black', activebackground=w3['bg'])
        b1.place(x=450, y=500)
        img3 = Image.open('submit.png')
        img3 = img3.resize((200, 200))
        photo3 = ImageTk.PhotoImage(image=img3)
        b2 = Button(w3, image=photo3, bd=0, bg=w3['bg'], command=validation, fg='black', activebackground=w3['bg'])
        b2.place(x=900, y=550)
    except:
        ms.showerror('Error','Button not working')
    w3.mainloop()
def page():
    global w4
    try:
        w3.destroy()
    except:
        pass
    
    w4=Tk()
    w4.title('page')
    w4.geometry('1000x1000')
    w4.config(bg='steel blue1')
    w4.attributes('-fullscreen',True)
    w4.bind_all("<Escape>",lambda e:w4.attributes('-fullscreen',False))
    l1=Label(w4,text='Congratulation your Account has been Successfully Created',font=('arial',30,'bold',),bg='steel blue1',fg='navy')
    l1.place(x=200,y=200)
    l2=Label(w4,text='Please click on continue to login into your account',font=('arial',25,'bold',),bg='steel blue1',fg='snow')
    l2.place(x=350,y=260)
    b1=Button(w4,text='Previous',command=accountype,font=('arial',20,'bold'),width=10,bg='sea green1',fg='black',activebackground='dark green',activeforeground='snow')
    b1.place(x=450,y=600)
    b2=Button(w4,text='Continue',command=login,font=('arial',20,'bold'),width=10,bg='sea green1',fg='black',activebackground='dark green',activeforeground='snow')
    b2.place(x=900,y=600)
    w4.mainloop()
def login():
    global w5, e1,e2
    try:
        w2.destroy()
    except:
        pass
    try:
        w4.destroy()
    except:
        pass
    try:
        w3.destroy()
    except:
        pass
    w5 = Tk()
    w5.title('login')
    w5.geometry('1000x1000')
    w5.config(bg='steel blue1')
    w5.attributes('-fullscreen',True)
    w5.bind_all("<Escape>",lambda e:w5.attributes('-fullscreen',False))
    img = Image.open('bank logo2.png')
    img = img.resize((80, 80))
    photo = ImageTk.PhotoImage(image=img)
    l1 = Label(w5, image=photo, bd=0, bg='steel blue1')
    l1.place(x=450, y=70)
    l2 = Label(w5, text='Secure Trust bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=550, y=70)
    l1=Label(w5,text='Login',font=('arial',34,'bold','underline'),bg='steel blue1',fg='navy')
    l1.place(x=670,y=150)
    l1=Label(w5,text='Email_id:',font=('arial',20,'bold',),bg='steel blue1',fg='blue')
    l1.place(x=500,y=300)
    l2=Label(w5,text='Password:',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l2.place(x=500,y=350)
    e1=Entry(w5,font=('arial',18))
    e1.place(x=700,y=300)
    e2=Entry(w5,font=('arial',18),show='*')
    e2.place(x=700,y=350)
    img1 = Image.open('back.png')
    img1 = img1.resize((250, 250))
    photo1 = ImageTk.PhotoImage(image=img1)
    b1 = Button(w5, image=photo1, bd=0, bg=w5['bg'], command=accountype, fg='black', activebackground=w5['bg'])
    b1.place(x=450, y=470)
    img2 = Image.open('submit.png')
    img2 = img2.resize((200, 200))
    photo2 = ImageTk.PhotoImage(image=img2)
    b2 = Button(w5, image=photo2, bd=0, bg=w5['bg'], command=validation, fg='black', activebackground=w5['bg'])
    b2.place(x=900, y=500)
    show_img = ImageTk.PhotoImage(Image.open('eye.png').resize((50, 50)))
    hide_img = ImageTk.PhotoImage(Image.open('hidden.png').resize((50, 50)))
    def hide_show():
        global password_visibility
        if password_visibility:
            e2.config(show='*')
            pass_show.config(image=show_img)
            password_visibility = False
        else:
            e2.config(show='')
            pass_show.config(image=hide_img)
            password_visibility = True
    pass_show=Button(w5, image=show_img,command=hide_show,bd=0,bg=w5['bg'], activebackground=w5['bg'])
    pass_show.place(x=980, y=340)
    w5.mainloop()
def validation():
    em=e1.get()
    pw=e2.get()
    k.execute("SELECT First_name,Last_name,ID from user_data1 where Email_id=? and Password=?",(em,pw))
    n=k.fetchone()
    if n:
        Full_name=n[0]+' '+n[1]
        ids=n[2]
        ms.showinfo("Success",f'You have successfully logged in ,{Full_name}')
        w5.destroy()
        loginwork(Full_name,ids)
    else:
        ms.showerror('alert',"invalid id or password")
def employeelogin():
    global w6
    try:
        w2.destroy()
    except:
        pass
    
    w6 = Tk()
    w6.title('employee logins')
    w6.geometry('1000x1000')
    w6.config(bg='steel blue1')
    w6.attributes('-fullscreen',True)
    w6.bind_all("<Escape>",lambda e:w6.attributes('-fullscreen',False))
    img = Image.open('bank logo2.png')
    img = img.resize((80, 80))
    photo = ImageTk.PhotoImage(image=img)
    l1 = Label(w6, image=photo, bd=0, bg='steel blue1')
    l1.place(x=450, y=70)
    l2 = Label(w6, text='Secure Trust bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=550, y=70)
    l1 = Label(w6, text='Employee Login', font=('arial', 34, 'bold', 'underline'), bg='steel blue1', fg='navy')
    l1.place(x=600, y=150)
    l1=Label(w6,text='Employee id:',font=('arial',20,'bold',),bg='steel blue1',fg='blue')
    l1.place(x=500,y=300)
    l2=Label(w6,text='Password:',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l2.place(x=500,y=350)
    e1=Entry(w6,font=('arial',18))
    e1.place(x=700,y=300)
    e2=Entry(w6,font=('arial',18),show='*')
    e2.place(x=700,y=350)
    img1 = Image.open('back.png')
    img1 = img1.resize((250, 250))
    photo1 = ImageTk.PhotoImage(image=img1)
    b1 = Button(w6, image=photo1, bd=0, bg=w6['bg'], command=accountype, fg='black', activebackground=w6['bg'])
    b1.place(x=450, y=470)

    def emp_validation():
        em = e1.get()
        pw = e2.get()
        if em == '':
            ms.showerror('Error', 'Please enter your email_id')
        elif pw == '':
            ms.showerror('Error', 'Please enter your password')
        else:
            pw1 = int(pw)
            k.execute("SELECT FULL_name,ID from Employee where Email_Id=? and Password=?", (em, pw))
            n = k.fetchone()
            if n:
                FULL_name = n[0]
                ids = n[1]
                ms.showinfo("Success", f'You have successfully logged in ,{FULL_name}')
                employee_work(FULL_name,ids)
            else:
                ms.showerror('alert', "invalid id or password")

    img2 = Image.open('submit.png')
    img2 = img2.resize((200, 200))
    photo2 = ImageTk.PhotoImage(image=img2)
    b2 = Button(w6, image=photo2, command=emp_validation, bd=0, bg=w6['bg'], fg='black', activebackground=w6['bg'])
    b2.place(x=900, y=500)
    show_img = ImageTk.PhotoImage(Image.open('eye.png').resize((50, 50)))
    hide_img = ImageTk.PhotoImage(Image.open('hidden.png').resize((50, 50)))

    def hide_show():
        global password_visibility
        if password_visibility:
            e2.config(show='*')
            pass_show.config(image=show_img)
            password_visibility = False
        else:
            e2.config(show='')
            pass_show.config(image=hide_img)
            password_visibility = True

    pass_show = Button(w6, image=show_img, command=hide_show, bd=0, bg=w6['bg'], activebackground=w6['bg'])
    pass_show.place(x=980, y=340)

    w6.mainloop()
def adminlogin():
    global w7
    try:
        w2.destroy()
    except:
        pass
    w7 = Tk()
    w7.title('admin logins')
    w7.geometry('1000x1000')
    w7.config(bg='steel blue1')
    w7.attributes('-fullscreen',True)
    w7.bind_all("<Escape>",lambda e:w7.attributes('-fullscreen',False))
    img = Image.open('bank logo2.png')
    img = img.resize((80, 80))
    photo = ImageTk.PhotoImage(image=img)
    l1 = Label(w7, image=photo, bd=0, bg='steel blue1')
    l1.place(x=450, y=70)
    l2 = Label(w7, text='Secure Trust bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=550, y=70)
    l1 = Label(w7, text='Admin Login', font=('arial', 34, 'bold', 'underline'), bg='steel blue1', fg='navy')
    l1.place(x=600, y=150)
    l1=Label(w7,text='Admin_id:',font=('arial',20,'bold',),bg='steel blue1',fg='blue')
    l1.place(x=500,y=300)
    l2=Label(w7,text='Password:',font=('arial',20,'bold'),bg='steel blue1',fg='blue')
    l2.place(x=500,y=350)
    e1=Entry(w7,font=('arial',18))
    e1.place(x=700,y=300)
    e2=Entry(w7,font=('arial',18),show='*')
    e2.place(x=700,y=350)
    img1 = Image.open('back.png')
    img1 = img1.resize((250, 250))
    photo1 = ImageTk.PhotoImage(image=img1)
    b1 = Button(w7, image=photo1, bd=0, bg=w7['bg'], command=accountype, fg='black', activebackground=w7['bg'])
    b1.place(x=450, y=470)
    img2 = Image.open('submit.png')
    img2 = img2.resize((200, 200))
    photo2 = ImageTk.PhotoImage(image=img2)

    def admin_validation():
        em = e1.get()
        pw = e2.get()
        if em == '':
            ms.showerror('Error', 'Please enter your email_id')
        elif pw == '':
            ms.showerror('Error', 'Please enter your password')
        else:
            pw1 = int(pw)
            k.execute("SELECT FULL_name,ID from Admin where Email_Id=? and Password=?", (em, pw))
            n = k.fetchone()
            if n:
                FULL_name = n[0]
                ids = n[1]
                ms.showinfo("Success", f'You have successfully logged in ,{FULL_name}')
                adminwork(FULL_name, ids)
               # w7.destroy()
            else:
                ms.showerror('alert', "invalid id or password")
    b2 = Button(w7, image=photo2, command=admin_validation ,bd=0, bg=w7['bg'], fg='black', activebackground=w7['bg'])
    b2.place(x=900, y=500)
    show_img = ImageTk.PhotoImage(Image.open('eye.png').resize((50, 50)))
    hide_img = ImageTk.PhotoImage(Image.open('hidden.png').resize((50, 50)))

    def hide_show():
        global password_visibility
        if password_visibility:
            e2.config(show='*')
            pass_show.config(image=show_img)
            password_visibility = False
        else:
            e2.config(show='')
            pass_show.config(image=hide_img)
            password_visibility = True

    pass_show = Button(w7, image=show_img, command=hide_show, bd=0, bg=w7['bg'], activebackground=w7['bg'])
    pass_show.place(x=980, y=340)
    w7.mainloop()
def loginwork(full,ids):
    global w8
    try:
        w3.destroy()
    except:
        pass
    try:
        w5.destroy()
    except:
        pass
    try:
        w6.destroy()
    except:
        pass
    try:
        w7.destroy()
    except:
        pass
    w8 = Tk()
    w8.title('login page')
    w8.geometry('1000x1000')
    w8.config(bg='steel blue1')
    w8.attributes('-fullscreen',True)
    w8.bind_all("<Escape>",lambda e:w8.attributes('-fullscreen',False))
    img = Image.open('bank_logo.png')
    img = img.resize((550, 100))
    photo = ImageTk.PhotoImage(img)
    l1 = Label(w8, image=photo, bd=0, bg='steelblue1')
    l1.image = photo
    l1.pack()
    sur_name=Label(w8, text=f'Welcome, {full} \n Account Number: {ids}', font=('arial', 30, 'bold'), bg='steelblue1', fg='snow')
    sur_name.pack()
    balan=Label(w8,text='Balance',font=('arial', 33, 'underline'), bg='steelblue1', fg='navy')
    balan.pack()
    k.execute("select Balance from user_data1 where ID=?",(ids,))
    balance=list(k.fetchone())
    amount=Label(w8,text=f'{balance[0]}',font=('arial', 45, 'bold'), bg='steelblue1', fg='navy')
    amount.pack()
    img = Image.open('deposit.png')
    img = img.resize((150, 150))
    photo = ImageTk.PhotoImage(image=img)
    b1 = Button(w8, image=photo, bd=0, bg=w8['bg'], command= lambda :deposit(ids), font=('arial', 20, 'bold'), fg='black',activebackground=w8['bg'])
    b1.place(x=230, y=450)
    img2 = Image.open('money-transfer.png')
    img2 = img2.resize((150, 150))
    photo2 = ImageTk.PhotoImage(image=img2)
    b3 = Button(w8, image=photo2, bd=0,command= lambda :transaction(ids), bg=w8['bg'],activebackground=w8['bg'])
    b3.place(x=550, y=450)
    img3 = Image.open('transaction-history.png')
    img3 = img3.resize((150, 150))
    photo3 = ImageTk.PhotoImage(image=img3)
    b4 = Button(w8, image=photo3, bd=0, bg=w8['bg'], command= lambda: transaction_history(ids), font=('arial', 20, 'bold'), fg='black', activebackground=w8['bg'])
    b4.place(x=880, y=450)
    img4 = Image.open('user.png')
    img4 = img4.resize((150, 150))
    photo4 = ImageTk.PhotoImage(image=img4)
    b5 = Button(w8, image=photo4, bd=0, bg=w8['bg'], command=lambda: profile_window(ids), font=('arial', 20, 'bold'), fg='black', activebackground=w8['bg'])
    b5.place(x=1200, y=450)
    img5 = Image.open('logout.png')
    img5 = img5.resize((150, 150))
    photo5 = ImageTk.PhotoImage(image=img5)
    b6 = Button(w8, image=photo5, bd=0, bg=w8['bg'], command=lambda: logout(), font=('arial', 20, 'bold'), fg='black',
                activebackground=w8['bg'])
    b6.place(x=700,y=700)
    l3=Label(w8,text='Deposit Money',font=('arial',15,'bold'),bg='steelblue1',fg='navy')
    l3.place(x=230,y=620)
    l5 = Label(w8, text='Money Transfer', font=('arial', 15, 'bold'), bg='steelblue1', fg='navy')
    l5.place(x=550, y=620)
    l6 = Label(w8, text='Transaction History', font=('arial', 15, 'bold'), bg='steelblue1', fg='navy')
    l6.place(x=880, y=620)
    l7 = Label(w8, text='Profile Update', font=('arial', 15, 'bold'), bg='steelblue1', fg='navy')
    l7.place(x=1200, y=620)
    w8.mainloop()
def employee_work(FULL_name,ids):
    global w9
    try:
        w5.destroy()
    except:
        pass
    try:
        w6.destroy()
    except:
        pass
    w9 = Tk()
    w9.title('admin logins')
    w9.geometry('1000x1000')
    w9.config(bg='steelblue1')
    w9.attributes('-fullscreen', True)
    w9.bind_all("<Escape>", lambda e: w9.attributes('-fullscreen', False))
    img = Image.open('bank_logo.png')
    img = img.resize((550, 100))
    photo = ImageTk.PhotoImage(img)
    l1 = Label(w9, image=photo, bd=0, bg='steelblue1')
    l1.image = photo
    l1.pack()
    l3 = Label(w9, text='Employee Panel', font=('arial', 30, 'bold'), bg='steelblue1', fg='snow')
    l3.pack()
    l4 = Label(w9, text=f'Welcome {FULL_name}\nUser ID: {ids}', font=('arial', 30, 'bold'), bg='steelblue1', fg='navy')
    l4.pack()
    l5 = Label(w9,text='Add New Customer                          Modify Customer detail                            Delete Account                             search Account',font=('arial', 15, 'bold'), bg='steelblue1', fg='navy')
    l5.place(x=150, y=450)
    img1 = Image.open('add new customer.png')
    img1 = img1.resize((150, 150))
    photo1 = ImageTk.PhotoImage(image=img1)
    b1 = Button(w9, image=photo1, command=add_new_customer,bd=0, bg=w9['bg'], fg='black', activebackground=w9['bg'], padx=20)
    b1.place(x=170, y=300)
    b1.image = photo1
    img2 = Image.open('modify customer.png')
    img2 = img2.resize((150, 150))
    photo2 = ImageTk.PhotoImage(image=img2)
    b2 = Button(w9, image=photo2, command=lambda: modify_customer_details(), bd=0, bg=w9['bg'], fg='black', activebackground=w9['bg'], padx=20)
    b2.place(x=520, y=300)
    b2.image = photo2
    img3 = Image.open('delete customer.png')
    img3 = img3.resize((150, 150))
    photo3 = ImageTk.PhotoImage(image=img3)
    b3 = Button(w9, image=photo3,command=lambda:delete_customer_account(), bd=0, bg=w9['bg'], fg='black', activebackground=w9['bg'], padx=20)
    b3.place(x=870, y=300)
    b3.image = photo3
    l6 = Label(w9, text='View all Customers                                        Loan Initiate                                               Logout',font=('arial', 15, 'bold'), bg='steelblue1', fg='navy')
    l6.place(x=300, y=700)
    img4 = Image.open('search customer.png')
    img4 = img4.resize((150, 150))
    photo4 = ImageTk.PhotoImage(image=img4)
    b4 = Button(w9, image=photo4,command=lambda:search_customer_account(), bd=0, bg=w9['bg'], fg='black', activebackground=w9['bg'], padx=20)
    b4.place(x=1210, y=300)
    img5 = Image.open('view all account.png')
    img5 = img5.resize((150, 150))
    photo5 = ImageTk.PhotoImage(image=img5)
    b5 = Button(w9, image=photo5,command=lambda:show_all_accounts(), bd=0, bg=w9['bg'], fg='black', activebackground=w9['bg'], padx=20)
    b5.place(x=320, y=550)
    b5.image = photo5
    img6 = Image.open('loan.png')
    img6 = img6.resize((150, 150))
    photo6 = ImageTk.PhotoImage(image=img6)
    b6 = Button(w9, image=photo6, command=lambda:initiate_loan(),bd=0, bg=w9['bg'], fg='black', activebackground=w9['bg'], padx=20)
    b6.place(x=700, y=550)
    b6.image = photo6
    img7 = Image.open('logout.png')
    img7 = img7.resize((150, 150))
    photo7 = ImageTk.PhotoImage(image=img7)
    b7 = Button(w9, image=photo7, bd=0, bg=w9['bg'], command=lambda: logout(), font=('arial', 20, 'bold'), fg='black',activebackground=w9['bg'])
    b7.place(x=1080, y=550)

    def logout():
        ask = ms.askyesno("Logout", "Are you sure you want to logout?", parent=w9)

        if ask:
            try:
                w9.destroy()
            except:
                pass
    w9.mainloop()
def transaction(IDs):
    global w10
    w10= Toplevel()
    w10.title('transaction')
    w10.geometry('1000x1000')
    w10.config(bg='steel blue1')
    w10.resizable(False,False)
    w10.attributes("-topmost",True)
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    pho = ImageTk.PhotoImage(image=logo)
    l1 = Label(w10, image=pho, bd=0, bg='steel blue1')
    l1.place(x=210, y=30)
    l2 = Label(w10, text='Secure Trust bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=300,y=50)
    l3 = Label(w10, text=f'Account Number: {IDs}', font=('arial', 30, 'bold'), bg='steel blue1', fg='snow')
    l3.place(x=330, y=150)
    l4 = Label(w10, text='Receivers Account number:', font=('arial', 20, 'bold'), bg='steel blue1', fg='blue')
    l4.place(x=200, y=300)
    l5 = Label(w10, text="Amount:", font=('arial', 20, 'bold'), bg='steel blue1', fg='blue')
    l5.place(x=200, y=400)
    e1 = Entry(w10, font=('arial', 20, 'bold'), fg='black')
    e1.place(x=600, y=300)
    e2 = Entry(w10, font=('arial', 20, 'bold'), fg='black')
    e2.place(x=600, y=400)

    def trans():
        try:
            k.execute("select Balance from User_data1 where ID=?", (IDs,))
            Q = list(k.fetchone())
            ab1 = int(e1.get())
            amou = int(e2.get())
            print(IDs, amou, ab1)
            if ab1 == IDs:
                ms.showerror("Error", "You can't send money in your own Account!", parent=w10)
                return

                # ✅ Receiver account fetch karo
            k.execute("select ID,Balance from User_data1 where ID=?", (ab1,))
            receiver_data = k.fetchone()

            if not receiver_data:
                ms.showerror("Error", "Receiver account exist nahi karta!", parent=w10)
                return
            # try:
            k.execute("select ID,Balance from User_data1 where ID=?", (ab1,))
            tu = list(k.fetchone())
            if amou <= Q[0]:
                new_amo = tu[1] + amou
                k.execute("update User_data1 set Balance=? where ID=?", (new_amo, tu[0]))
                d.commit()
                tg = Q[0] - amou
                k.execute("update User_data1 set Balance=? where ID=?", (tg, IDs))
                d.commit()
                if k.rowcount > 0:
                    k.execute("select First_name, Last_name from User_data1 where ID=?", (ab1,))
                    jj = k.fetchone()
                    full_n = jj[0] + " " + jj[1]
                    k.execute("INSERT INTO Transactions (User_ID, Type, Amount, To_Account,Name) VALUES (?,?,?, ?,?)",
                              (IDs, 'Transfer', amou, ab1, full_n))
                    d.commit()
                    # w10.attributes("-topmost",False)
                    m = ms.askyesno('Transferred', "DO you want to transfer more money", parent=w10)
                    if not m:
                        try:
                            w10.destroy()
                        except:
                            pass
                    else:
                        e1.delete(0, END)
                        e2.delete(0, END)
                else:
                    ms.showerror("Error", "Technical Problem\nTry after sometime", parent=w10)
                    w10.destroy()
            else:
                ms.showerror('Insufficient Balance', "Sorry You don't have account account", parent=w10)
        except Exception as e:
            ms.showerror("Error", str(e), parent=w10)

    img2 = Image.open('transfer.png')
    img2 = img2.resize((150, 150))
    photo2 = ImageTk.PhotoImage(image=img2)
    b2 = Button(w10, image=photo2,command=trans, bd=0, bg=w10['bg'], fg='black', activebackground=w10['bg'])
    b2.place(x=400, y=500)
    w10.mainloop()
def deposit(IDs):
    global w11
    w11 = Toplevel()
    w11.title("Money Deposit")
    w11.geometry("1000x1000")
    w11.config(bg="steel blue1")
    w11.resizable(False, False)
    w11.attributes("-topmost", True)
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    photo = ImageTk.PhotoImage(image=logo)
    l1 = Label(w11, image=photo, bd=0, bg='steel blue1')
    l1.photo = photo  # prevent garbage collection
    l1.place(x=210, y=50)
    l2 = Label(w11, text='Secure Trust Bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=300, y=50)
    l3 = Label(w11, text=f'Account Number: {IDs}', font=('arial', 30, 'bold'),  bg='steel blue1', fg='snow')
    l3.place(x=330, y=150)
    balan = Label(w11, text='Available Balance', font=('arial', 35, 'underline'), bg='steelblue1', fg='navy')
    balan.place(x=350, y=220)
    k.execute("SELECT Balance FROM user_data1 WHERE ID=?", (IDs,))
    balance_data = k.fetchone()
    current_balance = balance_data[0] if balance_data else 0
    amount_lbl = Label(w11, text=f'{current_balance}',  font=('arial', 40, 'bold'),  bg='steelblue1', fg='navy')
    amount_lbl.place(x=440, y=300)
    l4 = Label(w11, text="Enter the Amount:", font=('arial', 20, 'bold'), bg='steel blue1', fg='blue')
    l4.place(x=180, y=400)
    e1 = Entry(w11, font=('arial', 20, 'bold'), fg='black')
    e1.place(x=500, y=400)
    def do_deposit():
        try:
            depo_amount = int(e1.get())
            if depo_amount <= 0:
                ms.showerror("Invalid Amount", "Deposit amount must be greater than 0", parent=w11)
                return
            k.execute("SELECT Balance FROM user_data1 WHERE ID=?", (IDs,))
            bal = k.fetchone()
            if not bal:
                ms.showerror("Error", "Account not found!", parent=w11)
                return
            new_balance = bal[0] + depo_amount
            k.execute("UPDATE user_data1 SET Balance=? WHERE ID=?", (new_balance, IDs))
            d.commit()
            k.execute("INSERT INTO Transactions (User_ID, Type, Amount, To_Account, Name) VALUES (?,?,?,?,?)",(IDs, 'Deposit', depo_amount, IDs, 'Self Deposit'))
            d.commit()
            amount_lbl.config(text=f"{new_balance}")
            ms.showinfo("Success",f"₹{depo_amount} deposited successfully!\nNew Balance: ₹{new_balance}",parent=w11)
            more = ms.askyesno("Deposit More?", "Do you want to deposit more money?", parent=w11)
            if more:
                e1.delete(0, END)
            else:
                w11.destroy()
        except ValueError:
            ms.showerror("Error", "Please enter a valid numeric amount", parent=w11)
        except Exception as e:
            ms.showerror("Error", str(e), parent=w11)
    img1 = Image.open('deposit (1).png')
    img1 = img1.resize((150, 150))
    photo1 = ImageTk.PhotoImage(image=img1)
    b1 = Button(w11, image=photo1, bd=0, bg=w11['bg'], command=do_deposit, activebackground=w11['bg'])
    b1.photo = photo1
    b1.place(x=420, y=600)
    w11.mainloop()
def transaction_history(IDs):
    global w14
    try:
        w7.destroy()
    except:
        pass
    w12 = Toplevel()
    w12.title("Transaction History")
    w12.geometry("1200x800")
    w12.config(bg="steel blue1")
    w12.resizable(False, False)
    w12.attributes("-topmost", True)
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    photo = ImageTk.PhotoImage(image=logo)
    l1 = Label(w12, image=photo, bd=0, bg='steel blue1')
    l1.photo = photo
    l1.place(x=230, y=30)
    l2 = Label(w12, text='Secure Trust Bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=330, y=30)
    l3 = Label(w12, text=f'Account Number: {IDs}', font=('arial', 30, 'bold'), bg='steel blue1', fg='snow')
    l3.place(x=340, y=100)
    l4 = Label(w12, text="Your Transactions History", font=('arial', 25, 'bold', 'underline'), bg='steel blue1', fg='navy')
    l4.place(x=360, y=150)
    l5 = Label(w12, text="T_ID             Amount              Acc no.                    Date & Time                        Name",font=('arial', 20, 'bold'), bg='steel blue1')
    l5.place(x=70, y=250)
    k.execute("select T_ID,Amount,To_Account,Timestamp,Name from Transactions where User_ID=? and Type=? order by Timestamp desc limit 5",(IDs,"Transfer"))
    data = list(k.fetchall())
    ee = 300
    for row in data:
        ff = 50
        for idx, col in enumerate(row):
            det = Label(w12,text=str(col),font=('arial', 20), bg=w12['bg'],  bd=0,
                justify='left'
            )
            det.place(x=ff, y=ee)
            if idx == 3 or idx == 4:
                ff += 310
            else:
                ff += 200
        ee += 40
    w12.mainloop()
def profile_window(IDs):
    global w13
    w13 = Toplevel()
    w13.title('Profile')
    w13.geometry('1000x850')
    w13.config(bg='steel blue1')
    w13.resizable(False, False)
    w13.attributes("-topmost", True)
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    pho = ImageTk.PhotoImage(image=logo)
    lbl_logo = Label(w13, image=pho, bd=0, bg='steel blue1')
    lbl_logo.image = pho
    lbl_logo.place(x=160, y=50)
    Label(w13, text='Secure Trust Bank', font=('arial', 40, 'bold', 'underline'), bg='steel blue1', fg='navy').place(x=250, y=50)
    Label(w13, text=f"Account Number: {IDs}", font=('arial', 30, 'bold'), bg='steel blue1', fg='snow').place(x=300, y=150)
    frame_profile = Frame(w13, bg='lightblue')
    frame_profile.place(x=200, y=450)
    def clear_frame():
        for widget in frame_profile.winfo_children():
            widget.destroy()
    def show_profile():
        clear_frame()
        try:
            k.execute("SELECT First_name, Last_name,DOB,mobile_no,Email_id FROM User_data1 WHERE ID=?", (IDs,))
            user_data = k.fetchone()
            if not user_data:
                ms.showerror("Error", "User not found!", parent=w13)
                return
        except Exception as e:
            ms.showerror("Error", str(e), parent=w13)
            return

        Label(frame_profile, text="First Name:", font=('arial', 20, 'bold'),bg='lightblue', fg='blue').grid(row=0, column=0, sticky="w", pady=10)
        Label(frame_profile, text=user_data[0], font=('arial', 20), bg='lightblue', fg='black').grid(row=0, column=1, sticky="w")

        Label(frame_profile, text="Last Name:", font=('arial', 20, 'bold'),bg='lightblue', fg='blue').grid(row=1, column=0, sticky="w", pady=10)
        Label(frame_profile, text=user_data[1], font=('arial', 20),bg='lightblue', fg='black').grid(row=1, column=1, sticky="w")

        Label(frame_profile, text="DOB:", font=('arial', 20, 'bold'), bg='lightblue', fg='blue').grid(row=2, column=0, sticky="w", pady=10)
        Label(frame_profile, text=user_data[2], font=('arial', 20),bg='lightblue', fg='black').grid(row=2, column=1, sticky="w")

        Label(frame_profile, text="Mobile_No.:", font=('arial', 20, 'bold'),bg='lightblue', fg='blue').grid(row=3, column=0, sticky="w", pady=10)
        Label(frame_profile, text=user_data[3], font=('arial', 20), bg='lightblue', fg='black').grid(row=3, column=1, sticky="w")

        Label(frame_profile, text="Email_id:", font=('arial', 20, 'bold'), bg='lightblue', fg='blue').grid(row=4, column=0, sticky="w",pady=10)
        Label(frame_profile, text=user_data[4], font=('arial', 20), bg='lightblue', fg='black').grid(row=4, column=1,  sticky="w")

    # ✅ UPDATE PROFILE MODE
    def update_profile_mode():
        clear_frame()
        try:
            k.execute("SELECT First_name, Last_name, DOB,mobile_no,Email_id  FROM User_data1 WHERE ID=?", (IDs,))
            user_data = k.fetchone()
            if not user_data:
                ms.showerror("Error", "User not found!", parent=w13)
                return
        except Exception as e:
            ms.showerror("Error", str(e), parent=w13)
            return

        Label(frame_profile, text="First Name:", font=('arial', 20, 'bold'),bg='lightblue', fg='blue').grid(row=0, column=0, sticky="w", pady=10)
        e_fname = Entry(frame_profile, font=('arial', 20, 'bold'), fg='black')
        e_fname.grid(row=0, column=1)
        e_fname.insert(0, user_data[0])

        Label(frame_profile, text="Last Name:", font=('arial', 20, 'bold'), bg='lightblue', fg='blue').grid(row=1, column=0, sticky="w", pady=10)
        e_lname = Entry(frame_profile, font=('arial', 20, 'bold'), fg='black')
        e_lname.grid(row=1, column=1)
        e_lname.insert(0, user_data[1])

        Label(frame_profile, text="DOb:", font=('arial', 20, 'bold'),bg='lightblue', fg='blue').grid(row=2, column=0, sticky="w", pady=10)
        e_DOB = Entry(frame_profile, font=('arial', 20, 'bold'), fg='black')
        e_DOB.grid(row=2, column=1)
        e_DOB.insert(0, user_data[2])

        Label(frame_profile, text="Mobile_No.:", font=('arial', 20, 'bold'), bg='lightblue', fg='blue').grid(row=3, column=0, sticky="w", pady=10)
        e_mobile_no = Entry(frame_profile, font=('arial', 20, 'bold'), fg='black')
        e_mobile_no.grid(row=3, column=1)
        e_mobile_no.insert(0, user_data[3])

        def save_changes():
            fname = e_fname.get().strip()
            lname = e_lname.get().strip()
            DOB = e_DOB.get().strip()
            mobile_no = e_mobile_no.get().strip()

            if not fname or not lname or not DOB or not mobile_no:
                ms.showerror("Error", "All fields are required!", parent=w13)
                return

            try:
                k.execute("UPDATE User_data1 SET First_name=?, Last_name=?, DOB=?, mobile_no=? WHERE ID=?",
                          (fname, lname, DOB, mobile_no, IDs))
                d.commit()
                if k.rowcount > 0:
                    ms.showinfo("Success", "Profile updated successfully!", parent=w13)
                    show_profile()
                else:
                    ms.showwarning("Warning", "No changes were made!", parent=w13)
            except Exception as e:
                ms.showerror("Error", str(e), parent=w13)

        Button(frame_profile, text="Save Changes", command=save_changes, font=('arial', 18, 'bold'), bg='green', fg='white', padx=20).grid(row=4, column=0, columnspan=2, pady=20)
    def change_password_mode():
        clear_frame()

        Label(frame_profile, text="Old Password:", font=('arial', 20, 'bold'),
              bg='lightblue', fg='blue').grid(row=0, column=0, sticky="w", pady=10)
        e_old = Entry(frame_profile, font=('arial', 20, 'bold'), fg='black', show='*')
        e_old.grid(row=0, column=1)

        Label(frame_profile, text="New Password:", font=('arial', 20, 'bold'),
              bg='lightblue', fg='blue').grid(row=1, column=0, sticky="w", pady=10)
        e_new = Entry(frame_profile, font=('arial', 20, 'bold'), fg='black', show='*')
        e_new.grid(row=1, column=1)

        Label(frame_profile, text="Confirm New Password:", font=('arial', 20, 'bold'),
              bg='lightblue', fg='blue').grid(row=2, column=0, sticky="w", pady=10)
        e_confirm = Entry(frame_profile, font=('arial', 20, 'bold'), fg='black', show='*')
        e_confirm.grid(row=2, column=1)

        def save_password():
            old_pass = e_old.get().strip()
            new_pass = e_new.get().strip()
            confirm_pass = e_confirm.get().strip()

            if not old_pass or not new_pass or not confirm_pass:
                ms.showerror("Error", "All fields are required!", parent=w13)
                return

            if new_pass != confirm_pass:
                ms.showerror("Error", "New password and confirm password do not match!", parent=w13)
                return

            try:
                k.execute("SELECT Password FROM User_data1 WHERE ID=?", (IDs,))
                db_pass = k.fetchone()
                if int(db_pass[0]) != int(old_pass):
                    ms.showerror("Error", "Old password is incorrect!", parent=w13)
                    return

                k.execute("UPDATE User_data1 SET Password=? WHERE ID=?", (new_pass, IDs))
                d.commit()
                if k.rowcount > 0:
                    ms.showinfo("Success", "Password changed successfully!", parent=w13)
                    clear_frame()
                else:
                    ms.showwarning("Warning", "Password not updated!", parent=w13)

            except Exception as e:
                ms.showerror("Error", str(e), parent=w13)

        Button(frame_profile, text="Save Password", command=save_password,font=('arial', 18, 'bold'), bg='red', fg='white', padx=20).grid(row=3, column=0, columnspan=2, pady=20)

    img1 = Image.open('show profile.png')
    img1= img1.resize((140, 140))
    photo1 = ImageTk.PhotoImage(image=img1)
    b1 = Button(w13, image=photo1, bd=0, bg=w13['bg'], command=show_profile, fg='black', activebackground=w13['bg'], padx=20)
    b1.place(x=200, y=230)
    b1.image=photo1

    img2 = Image.open('update profile.png')
    img2 = img2.resize((180, 180))
    photo2 = ImageTk.PhotoImage(image=img2)
    b2 = Button(w13, image=photo2, bd=0, bg=w13['bg'], command=update_profile_mode, fg='black', activebackground=w13['bg'],  padx=20)
    b2.place(x=450, y=230)
    b2.image = photo2
    img3 = Image.open('reset-password.png')
    img3 = img3.resize((140, 140))
    photo3 = ImageTk.PhotoImage(image=img3)
    b3 = Button(w13, image=photo3, bd=0, bg=w13['bg'], command=change_password_mode, fg='black', activebackground=w13['bg'], padx=20)
    b3.place(x=700, y=230)
    b3.image = photo3
def logout():
    ask = ms.askyesno("Logout", "Are you sure you want to logout?", parent=w8)

    if ask:
     try:
        w8.destroy()
       # accountype()
     except:
          pass
def adminwork(ad_n,ad_i):
    global w14
    try:
        w7.destroy()
    except:
        pass
    w14 = Tk()
    w14.title('admin logins')
    w14.geometry('1000x1000')
    w14.config(bg='steelblue1')
    w14.attributes('-fullscreen', True)
    w14.bind_all("<Escape>", lambda e: w14.attributes('-fullscreen', False))
    img = Image.open('bank_logo.png')
    img = img.resize((550, 100))
    photo = ImageTk.PhotoImage(img)
    l1 = Label(w14, image=photo, bd=0, bg='steelblue1')
    l1.image = photo
    l1.pack()
    l3=Label(w14,text='Admin Panel',font=('arial', 30, 'bold'),bg='steelblue1', fg='snow')
    l3.pack()
    l4=Label(w14,text=f'Welcome {ad_n}\nUser ID: {ad_i}',font=('arial', 30, 'bold'),bg='steelblue1', fg='navy')
    l4.pack()
    l5=Label(w14,text='Add New Employee                               Modify Employee                              Delete Employee                                view all Employee',font=('arial', 15, 'bold'),bg='steelblue1', fg='navy')
    l5.place(x=150,y=450)
    img1 = Image.open('new employee in admin.png')
    img1 = img1.resize((150, 150))
    photo1 = ImageTk.PhotoImage(image=img1)
    b1 = Button(w14, image=photo1,command=lambda: add_new_employee(), bd=0, bg=w14['bg'], fg='black',activebackground=w14['bg'], padx=20)
    b1.place(x=170, y=300)
    b1.image = photo1
    img2 = Image.open('modify employee detail.png')
    img2 = img2.resize((150, 150))
    photo2 = ImageTk.PhotoImage(image=img2)
    b2 = Button(w14, image=photo2,command=lambda:modify_employee_details(), bd=0, bg=w14['bg'], fg='black', activebackground=w14['bg'], padx=20)
    b2.place(x=520, y=300)
    b2.image = photo2
    img3 = Image.open('delete employee.png')
    img3 = img3.resize((150, 150))
    photo3 = ImageTk.PhotoImage(image=img3)
    b3 = Button(w14, image=photo3,command=lambda:delete_employee_account(), bd=0, bg=w14['bg'], fg='black', activebackground=w14['bg'], padx=20)
    b3.place(x=870, y=300)
    b3.image = photo3
    l6 = Label(w14, text='View all Customers                                      Admin Profile                                               Logout', font=('arial', 15, 'bold'), bg='steelblue1', fg='navy')
    l6.place(x=300, y=700)
    img4 = Image.open('view all employee.png')
    img4 = img4.resize((150, 150))
    photo4 = ImageTk.PhotoImage(image=img4)
    b4 = Button(w14, image=photo4,command=lambda:show_all_employees(), bd=0, bg=w14['bg'], fg='black', activebackground=w14['bg'], padx=20)
    b4.place(x=1210, y=300)
    img5 = Image.open('all customers account.png')
    img5 = img5.resize((150, 150))
    photo5 = ImageTk.PhotoImage(image=img5)
    b5 = Button(w14, image=photo5,command=lambda:show_all_accounts(), bd=0, bg=w14['bg'], fg='black', activebackground=w14['bg'], padx=20)
    b5.place(x=320, y=550)
    b5.image = photo5
    img6 = Image.open('admin-panel.png')
    img6 = img6.resize((150, 150))
    photo6 = ImageTk.PhotoImage(image=img6)
    b6 = Button(w14, image=photo6,command=lambda:show_admin_profile(ad_i),bd=0, bg=w14['bg'], fg='black', activebackground=w14['bg'], padx=20)
    b6.place(x=700, y=550)
    b6.image = photo6
    img7 = Image.open('logout.png')
    img7 = img7.resize((150, 150))
    photo7 = ImageTk.PhotoImage(image=img7)
    b7 = Button(w14, image=photo7, bd=0, bg=w14['bg'], command=lambda: logout(), font=('arial', 20, 'bold'), fg='black',activebackground=w14['bg'])
    b7.place(x=1080, y=550)
    def logout():
        ask = ms.askyesno("Logout", "Are you sure you want to logout?", parent=w14)

        if ask:
            try:
                w14.destroy()
            except:
                pass
    w14.mainloop()
def add_new_employee():
        w15 = Toplevel(w14)
        w15.title("Add New Employee")
        w15.geometry("1000x800")
        w15.attributes("-topmost", True)
        w15.config(bg="steel blue1")
        logo = Image.open('bank logo2.png')
        logo = logo.resize((80, 80))
        photo = ImageTk.PhotoImage(image=logo)
        l1 = Label(w15, image=photo, bd=0, bg='steel blue1')
        l1.photo = photo  # prevent garbage collection
        l1.place(x=210, y=50)
        l2 = Label(w15, text='Secure Trust Bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
        l2.place(x=300, y=50)
        l3=Label(w15, text="Add New Employee", font=("Arial", 22, "bold"), bg="steel blue1", fg="navy")
        l3.place(x=400,y=150)
        l4=Label(w15, text="Full Name:", font=("Arial", 20,'bold'),bg='steel blue1',fg='blue')
        l4.place(x=200,y=250)
        e1 = Entry(w15, font=('arial', 20, 'bold'), fg='black')
        e1.place(x=500, y=250)
        l5 = Label(w15, text="DOB:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
        l5.place(x=200, y=300)
        e2 = Entry(w15, font=('arial', 20, 'bold'), fg='black')
        e2.place(x=500, y=300)
        l6 = Label(w15, text="Mobile No.:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
        l6.place(x=200, y=350)
        e3 = Entry(w15, font=('arial', 20, 'bold'), fg='black')
        e3.place(x=500, y=350)
        l7 = Label(w15, text="Email id.:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
        l7.place(x=200, y=400)
        e4 = Entry(w15, font=('arial', 20, 'bold'), fg='black')
        e4.place(x=500, y=400)
        l8 = Label(w15, text="Position:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
        l8.place(x=200, y=450)
        e5  = Entry(w15, font=('arial', 20, 'bold'), fg='black')
        e5.place(x=500, y=450)
        l9 = Label(w15, text="Salary:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
        l9.place(x=200, y=500)
        e6 = Entry(w15, font=('arial', 20, 'bold'), fg='black')
        e6.place(x=500, y=500)
        l10 = Label(w15, text="Password:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
        l10.place(x=200, y=550)
        e7 = Entry(w15, font=('arial', 20, 'bold'), fg='black')
        e7.place(x=500, y=550)
        def save_employee():
            name = e1.get()
            dob = e2.get()
            mobile=  e3.get()
            email=e4.get()
            position=e5.get()
            salary = e6.get()
            password = e7.get()
            if name == '':
                ms.showerror('Alert', "can't run without full name",parent=w15)
            elif dob == '':
                ms.showerror('Alert', "can't run without dob name",parent=w15)
            elif mobile == '':
                ms.showerror('Alert', "cant't run without mobile number",parent=w15)
            elif not re.search(r'^\w+@\w+\.[a-z]{2,3}$', e4.get()):
                ms.showerror('Alert', "cant't run without email",parent=w15)
            elif email == '':
                ms.showerror('Alert', "cant't run without email_id",parent=w15)
            elif position == '':
                ms.showerror('Alert', "cant't run without position",parent=w15)
            elif salary == '':
                ms.showerror('Alert', "cant't run without salary",parent=w15)
            elif password == '':
                ms.showerror('Alert', "cant't run without password",parent=w15)
            else:
                k.execute("insert into Employee (FULL_name ,DOB , mobile_no , Email_id ,password ,Position ,Salary) values (?,?,?,?,?,?,?)", (name,dob,mobile,email,password,position,salary))
                d.commit()
                if k.rowcount>0:
                    ms.showinfo("Success", f"Employee {name} added successfully!",parent=w15)
                    w15.destroy()
                else:
                    pass
        b1=Button(w15, text="Save Employee", font=("Arial", 20), bg="green", fg="white",command=save_employee)
        b1.place(x=400,y=700)
        w15.mainloop()
def add_new_customer():
    w16 = Toplevel()
    w16.title("Add New Employee")
    w16.geometry("1000x800")
    w16.attributes("-topmost", True)
    w16.config(bg="steel blue1")
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    photo = ImageTk.PhotoImage(image=logo)
    l1 = Label(w16, image=photo, bd=0, bg='steel blue1')
    l1.photo = photo  # prevent garbage collection
    l1.place(x=210, y=50)
    l2 = Label(w16, text='Secure Trust Bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=300, y=50)
    l3 = Label(w16, text="Add New Customer", font=("Arial", 22, "bold"), bg="steel blue1", fg="navy")
    l3.place(x=400, y=150)
    l4 = Label(w16, text="First Name:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l4.place(x=200, y=250)
    e1 = Entry(w16, font=('arial', 20, 'bold'), fg='black')
    e1.place(x=500, y=250)
    l5 = Label(w16, text="Last Name:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l5.place(x=200, y=300)
    e2 = Entry(w16, font=('arial', 20, 'bold'), fg='black')
    e2.place(x=500, y=300)
    l6 = Label(w16, text="DOB:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l6.place(x=200, y=350)
    e3 = Entry(w16, font=('arial', 20, 'bold'), fg='black')
    e3.place(x=500, y=350)
    l7 = Label(w16, text="Email id.:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l7.place(x=200, y=400)
    e4 = Entry(w16, font=('arial', 20, 'bold'), fg='black')
    e4.place(x=500, y=400)
    l8 = Label(w16, text="Mobile_no.:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l8.place(x=200, y=450)
    e5 = Entry(w16, font=('arial', 20, 'bold'), fg='black')
    e5.place(x=500, y=450)
    l9 = Label(w16, text="Password:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l9.place(x=200, y=500)
    e6 = Entry(w16, font=('arial', 20, 'bold'), fg='black')
    e6.place(x=500, y=500)
    l10 = Label(w16, text="Account Type:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l10.place(x=200, y=550)
    e7 = Entry(w16, font=('arial', 20, 'bold'), fg='black')
    e7.place(x=500, y=550)
    def save_customer():
        fn = e1.get()
        ln = e2.get()
        DOb = e3.get()
        em = e4.get()
        mob = e5.get()
        pw = e6.get()
        ac= e7.get()
        if fn == '':
            ms.showerror('Alert', "can't run without first name")
        elif ln == '':
            ms.showerror('Alert', "can't run without last name")
        elif DOb == '':
            ms.showerror('Alert', "cant't run without Dob")
        elif not re.search(r'^\w+@\w+\.[a-z]{2,3}$', e4.get()):
            ms.showerror('Alert', "cant't run without email")
        elif mob == '':
            ms.showerror('Alert', "cant't run without mobile no.")
        elif pw == '':
            ms.showerror('Alert', "cant't run without password")
        elif ac == '':
            ms.showerror('Alert', "cant't run without account type")
        else:
            try:
                k.execute(
                    "INSERT INTO User_data1 (First_name, Last_name, DOB, Email_id, mobile_no, password,Type) VALUES (?, ?, ?, ?, ?, ?,?)", (fn, ln, DOb, em, mob, pw,ac) )
                d.commit()
                ms.showinfo("Success", "Customer added successfully!", parent=w16)
                w16.destroy()
            except Exception as ex:
                ms.showerror("DB Error", f"Customer not added!\n{ex}")
    b1 = Button(w16, text="Save Detail", font=("Arial", 20), bg="green", fg="white", command=save_customer)
    b1.place(x=400, y=700)
def modify_customer_details():
    w17 = Toplevel()
    w17.title("Modify Customer Details")
    w17.geometry("1000x1200")
    w17.attributes("-topmost", True)
    w17.config(bg="steel blue1")
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    photo = ImageTk.PhotoImage(image=logo)
    l1 = Label(w17, image=photo, bd=0, bg='steel blue1')
    l1.photo = photo
    l1.place(x=210, y=50)
    l2 = Label(w17, text='Secure Trust Bank', font=('arial', 40, 'bold', 'underline'),bg='steelblue1', fg='navy')
    l2.place(x=300, y=50)
    l3 = Label(w17, text="Modify Customer Details", font=("Arial", 25, "bold"),bg="steel blue1", fg="snow")
    l3.place(x=350, y=150)
    l4 = Label(w17, text="Enter Customer Email ID:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l4.place(x=150, y=200)
    e1 = Entry(w17, font=('arial', 18, 'bold'), fg='black')
    e1.place(x=500, y=200)
    l5 = Label(w17, text="Enter Password:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    l5.place(x=150, y=250)
    e2 = Entry(w17, font=('arial', 20, 'bold'), fg='black', show="*")
    e2.place(x=500, y=250)
    # Editable fields (hidden initially)
    fn_label = Label(w17, text="First Name:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    fn_entry = Entry(w17, font=('arial', 20, 'bold'), fg='black')
    ln_label = Label(w17, text="Last Name:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    ln_entry = Entry(w17, font=('arial', 20, 'bold'), fg='black')
    dob_label = Label(w17, text="DOB:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    dob_entry = Entry(w17, font=('arial', 20, 'bold'), fg='black')
    mob_label = Label(w17, text="Mobile No.:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    mob_entry = Entry(w17, font=('arial', 20, 'bold'), fg='black')
    pw_label = Label(w17, text="New Password:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    pw_entry = Entry(w17, font=('arial', 20, 'bold'), fg='black')
    def load_customer():
        email = e1.get()
        password = e2.get()
        if email == '' or password == '':
            ms.showerror("Error", "Enter both Email and Password", parent=w17)
            return
        k.execute("SELECT First_name, Last_name, DOB, Email_id, mobile_no, password FROM User_data1 WHERE Email_id=? AND password=?", (email, password))
        cust = k.fetchone()
        if cust:
            # Show editable fields with existing data
            fn_label.place(x=150, y=400)
            fn_entry.place(x=500, y=400)
            fn_entry.delete(0, END)
            fn_entry.insert(0, cust[0])

            ln_label.place(x=150, y=450)
            ln_entry.place(x=500, y=450)
            ln_entry.delete(0, END)
            ln_entry.insert(0, cust[1])

            dob_label.place(x=150, y=500)
            dob_entry.place(x=500, y=500)
            dob_entry.delete(0, END)
            dob_entry.insert(0, cust[2])

            mob_label.place(x=150, y=550)
            mob_entry.place(x=500, y=550)
            mob_entry.delete(0, END)
            mob_entry.insert(0, cust[4])

            pw_label.place(x=150, y=600)
            pw_entry.place(x=500, y=600)
            pw_entry.delete(0, END)
            pw_entry.insert(0, cust[5])
        else:
            ms.showerror("Error", "Customer not found or wrong password!", parent=w17)
    def save_changes():
        fn = fn_entry.get()
        ln = ln_entry.get()
        dob = dob_entry.get()
        mob = mob_entry.get()
        new_pw = pw_entry.get()
        email = e1.get()
        if fn == '' or ln == '' or dob == '' or mob == '' or new_pw == '':
            ms.showerror("Error", "All fields are required!", parent=w17)
            return
        try:
            k.execute("""UPDATE User_data1 SET First_name=?, Last_name=?, DOB=?, mobile_no=?, password=? WHERE Email_id=?""", (fn, ln, dob, mob, new_pw, email))
            d.commit()
            ms.showinfo("Success", "Customer details updated successfully!", parent=w17)
            w17.destroy()
        except Exception as ex:
            ms.showerror("DB Error", f"Update failed!\n{ex}", parent=w17)
    b1 = Button(w17, text="Load Customer", font=("Arial", 20), bg="sea green1", fg="black", command=load_customer)
    b1.place(x=400, y=330)
    b2 = Button(w17, text="Save Changes", font=("Arial", 20), bg="green", fg="black", command=save_changes)
    b2.place(x=400, y=680)
    w17.mainloop()
def delete_customer_account():
    w19 = Toplevel()
    w19.title("Delete Customer Account")
    w19.geometry("800x500")
    w19.attributes("-topmost", True)
    w19.config(bg="steel blue1")
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    photo = ImageTk.PhotoImage(image=logo)
    l1 = Label(w19, image=photo, bd=0, bg='steel blue1')
    l1.photo = photo
    l1.place(x=100, y=30)
    l2 = Label(w19, text='Secure Trust Bank', font=('arial', 35, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=200, y=40)
    l3 = Label(w19, text="Delete Customer Account", font=("Arial", 22, "bold"),bg="steel blue1", fg="red")
    l3.place(x=200, y=150)
    l4 = Label(w19, text="Enter Email ID:", font=("Arial", 20, 'bold'),bg='steel blue1', fg='blue')
    l4.place(x=150, y=230)
    e1 = Entry(w19, font=('arial', 20, 'bold'), fg='black')
    e1.place(x=400, y=230)
    l5 = Label(w19, text="Enter Password:", font=("Arial", 20, 'bold'),bg='steel blue1', fg='blue')
    l5.place(x=150, y=280)
    e2 = Entry(w19, font=('arial', 20, 'bold'), fg='black', show="*")
    e2.place(x=400, y=280)

    def delete_customer():
        email = e1.get()
        password = e2.get()
        if email == '' or password == '':
            ms.showerror("Error", "Please enter Email and Password!", parent=w19)
            return
        k.execute("SELECT First_name, Last_name FROM User_data1 WHERE Email_id=? AND password=?",(email, password))
        cust = k.fetchone()
        if cust:
            confirm = ms.askyesno("Confirm Deletion",f"Are you sure you want to delete account for {cust[0]} {cust[1]}?", parent=w19)
            if confirm:
                try:
                    k.execute("DELETE FROM User_data1 WHERE Email_id=? AND password=?", (email, password))
                    d.commit()
                    if k.rowcount > 0:
                        ms.showinfo("Deleted", f"Customer {cust[0]} {cust[1]} deleted successfully!", parent=w19)
                        w19.destroy()
                    else:
                        ms.showerror("Error", "Failed to delete account!", parent=w19)
                except Exception as ex:
                    ms.showerror("DB Error", f"Deletion failed!\n{ex}", parent=w19)
        else:
            ms.showerror("Error", "No matching customer found or wrong password!", parent=w19)

    b1 = Button(w19, text="Delete Account", font=("Arial", 20),bg="red", fg="white", command=delete_customer)
    b1.place(x=300, y=350)
    w19.mainloop()
def search_customer_account():
    w20 = Toplevel()
    w20.title("Search Customer Account")
    w20.geometry("1000x700")
    w20.config(bg="steel blue1")
    w20.attributes("-topmost", True)
    l1=Label(w20, text="Search Customer Account", font=("Arial", 25, "bold"),bg="steel blue1", fg="navy").pack(pady=30)
    l2=Label(w20, text="Enter Email or Mobile No.:", font=("Arial", 20, "bold"), bg="steel blue1", fg="blue").pack(pady=10)
    e1= Entry(w20, font=("Arial", 20), width=30)
    e1.pack(pady=10)
    l3 = Label(w20, text="", font=("Arial", 16), bg="steel blue1", fg="white", justify="left")
    l3.pack(pady=30)
    b1 = Button(w20, text="Close", font=("Arial", 18), bg="red", fg="white", command=w20.destroy)
    def search_customer():
        query = e1.get().strip()
        if query == "":
            l3.config(text="⚠ Please enter Email or Mobile Number!", fg="yellow")
            return
        k.execute("SELECT First_name, Last_name, DOB, Email_id, mobile_no FROM User_data1 WHERE Email_id=? OR mobile_no=?",(query, query))
        data = k.fetchone()
        if data:
            fn, ln, dob, email, mob = data
            l3.config(
                text=f"✅ Customer Found:\n\n"
                     f"Name   : {fn} {ln}\n"
                     f"DOB    : {dob}\n"
                     f"Email  : {email}\n"
                     f"Mobile : {mob}",
                fg="white"
            )
        else:
            l3.config(text="❌ No matching customer found!", fg="red")
        b1.pack(pady=10)
    b2=Button(w20, text="Search", font=("Arial", 18), bg="green", fg="white", command=search_customer).pack(pady=10)
    w20.mainloop()
def initiate_loan():
    w22 = Toplevel()
    w22.title("Initiate Loan")
    w22.geometry("1000x700")
    w22.config(bg="steel blue1")
    w22.attributes("-topmost", True)

    l1 = Label(w22, text="Loan Initiation Form", font=("Arial", 26, "bold"), bg="steel blue1", fg="navy")
    l1.place(x=350, y=50)
    l2 = Label(w22, text="Customer Email:", font=("Arial", 20, "bold"),bg="steel blue1", fg="blue")
    l2.place(x=200, y=150)
    e1 = Entry(w22, font=('Arial', 20, 'bold'), fg='black')
    e1.place(x=500, y=150)
    l3 = Label(w22, text="Loan Amount:", font=("Arial", 20, "bold"),bg="steel blue1", fg="blue")
    l3.place(x=200, y=220)
    e2 = Entry(w22, font=('Arial', 20, 'bold'), fg='black')
    e2.place(x=500, y=220)
    l4 = Label(w22, text="Loan Type:", font=("Arial", 20, "bold"),bg="steel blue1", fg="blue")
    l4.place(x=200, y=290)
    e3 = Entry(w22, font=('Arial', 20, 'bold'), fg='black')
    e3.place(x=500, y=290)
    l5 = Label(w22, text="Duration (Months):", font=("Arial", 20, "bold"),bg="steel blue1", fg="blue")
    l5.place(x=200, y=360)
    e4 = Entry(w22, font=('Arial', 20, 'bold'), fg='black')
    e4.place(x=500, y=360)
    l6 = Label(w22, text="Interest Rate (%):", font=("Arial", 20, "bold"), bg="steel blue1", fg="blue")
    l6.place(x=200, y=430)
    e5 = Entry(w22, font=('Arial', 20, 'bold'), fg='black')
    e5.place(x=500, y=430)
    def save_loan():
        email = e1.get()
        amount = e2.get()
        loan_type = e3.get()
        duration = e4.get()
        interest = e5.get()
        if email == '' or amount == '' or loan_type == '' or duration == '' or interest == '':
            ms.showerror("Alert", "All fields are required!", parent=w22)
        else:
            try:
                k.execute("""CREATE TABLE IF NOT EXISTS Loan (id INTEGER PRIMARY KEY AUTOINCREMENT,customer_email TEXT,loan_amount REAL,loan_type TEXT,duration_months INTEGER,interest_rate REAL)""")
                k.execute("INSERT INTO Loan (customer_email, loan_amount, loan_type, duration_months, interest_rate) VALUES (?, ?, ?, ?, ?)",(email, amount, loan_type, duration, interest))
                d.commit()
                ms.showinfo("Success", f"Loan initiated for {email}", parent=w22)
                w22.destroy()
            except Exception as ex:
                ms.showerror("DB Error", f"Loan not initiated!\n{ex}", parent=w22)
    b1 = Button(w22, text="Initiate Loan", font=("Arial", 18), bg="green", fg="white", command=save_loan)
    b1.place(x=350, y=550)
    b2 = Button(w22, text="Close", font=("Arial", 18), bg="red", fg="white", command=w22.destroy)
    b2.place(x=550, y=550)

    w22.mainloop()
def delete_employee_account():
    w23 = Toplevel()
    w23.title("Delete Employee Account")
    w23.geometry("800x600")
    w23.attributes("-topmost", True)
    w23.config(bg="steel blue1")
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    photo = ImageTk.PhotoImage(image=logo)
    l1 = Label(w23, image=photo, bd=0, bg='steel blue1')
    l1.photo = photo
    l1.place(x=150, y=30)
    l2 = Label(w23, text='Secure Trust Bank', font=('arial', 35, 'bold', 'underline'),bg='steelblue1', fg='navy')
    l2.place(x=250, y=40)
    l3 = Label(w23, text="Delete Employee Account", font=("Arial", 22, "bold"),bg="steel blue1", fg="navy")
    l3.place(x=250, y=150)
    l4 = Label(w23, text="Employee Email ID:", font=("Arial", 20, 'bold'),bg='steel blue1', fg='blue')
    l4.place(x=100, y=250)
    e1 = Entry(w23, font=('arial', 20, 'bold'), fg='black')
    e1.place(x=400, y=250)
    l5 = Label(w23, text="Password:", font=("Arial", 20, 'bold'),bg='steel blue1', fg='blue')
    l5.place(x=100, y=320)
    e2 = Entry(w23, font=('arial', 20, 'bold'), fg='black', show="*")
    e2.place(x=400, y=320)
    def confirm_delete():
        email = e1.get().strip()
        password = e2.get().strip()
        if email == '':
            ms.showerror("Alert", "Please enter Employee Email ID", parent=w23)
            return
        elif not re.search(r'^\w+@\w+\.[a-z]{2,3}$', email):
            ms.showerror("Alert", "Invalid Email format", parent=w23)
            return
        elif password == '':
            ms.showerror("Alert", "Please enter password", parent=w23)
            return
        k.execute("SELECT FULL_name FROM Employee WHERE Email_id = ? AND password = ?", (email, password))
        emp = k.fetchone()
        if emp:
            ask = ms.askyesno("Confirm Delete",f"Are you sure you want to delete Employee '{emp[0]}'?",parent=w23)
            if ask:
                k.execute("DELETE FROM Employee WHERE Email_id = ? AND password = ?", (email, password))
                d.commit()
                ms.showinfo("Success", f"Employee '{emp[0]}' deleted successfully!", parent=w23)
                w23.destroy()
        else:
            ms.showerror("Error", "Employee not found or password incorrect!", parent=w23)
    b1 = Button(w23, text="Delete Employee", font=("Arial", 20), bg="red", fg="white", command=confirm_delete)
    b1.place(x=300, y=420)
    w23.mainloop()
def modify_employee_details():
    w24 = Toplevel()
    w24.title("Modify Employee Details")
    w24.geometry("1000x1200")
    w24.attributes("-topmost", True)
    w24.config(bg="steel blue1")
    logo = Image.open('bank logo2.png')
    logo = logo.resize((80, 80))
    photo = ImageTk.PhotoImage(image=logo)
    l1 = Label(w24, image=photo, bd=0, bg='steel blue1')
    l1.photo = photo
    l1.place(x=210, y=50)
    l2 = Label(w24, text='Secure Trust Bank', font=('arial', 40, 'bold', 'underline'), bg='steelblue1', fg='navy')
    l2.place(x=300, y=50)
    l3 = Label(w24, text="Modify Employee Details", font=("Arial", 22, "bold"),bg="steel blue1", fg="snow")
    l3.place(x=350, y=150)
    l4 = Label(w24, text="Enter Employee Email ID:", font=("Arial", 20, 'bold'),bg='steel blue1', fg='blue')
    l4.place(x=150, y=200)
    e1 = Entry(w24, font=('arial', 20, 'bold'), fg='black')
    e1.place(x=500, y=200)
    l5 = Label(w24, text="Enter Current Password:", font=("Arial", 20, 'bold'),bg='steel blue1', fg='blue')
    l5.place(x=150, y=250)
    e2 = Entry(w24, font=('arial', 20, 'bold'), fg='black', show="*")
    e2.place(x=500, y=250)
    # Editable fields (hidden initially)
    l6 = Label(w24, text="Full Name:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    e3 = Entry(w24, font=('arial', 20, 'bold'), fg='black')
    l7 = Label(w24, text="DOB:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    e4 = Entry(w24, font=('arial', 20, 'bold'), fg='black')
    l8 = Label(w24, text="Mobile No.:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    e5 = Entry(w24, font=('arial', 20, 'bold'), fg='black')
    l9 = Label(w24, text="Position:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    e6 = Entry(w24, font=('arial', 20, 'bold'), fg='black')
    l10 = Label(w24, text="Salary:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    e7 = Entry(w24, font=('arial', 20, 'bold'), fg='black')
    l11 = Label(w24, text="New Password (optional):", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    e8 = Entry(w24, font=('arial', 20, 'bold'), fg='black', show="*")
    l12 = Label(w24, text="Confirm New Password:", font=("Arial", 20, 'bold'), bg='steel blue1', fg='blue')
    e9 = Entry(w24, font=('arial', 20, 'bold'), fg='black', show="*")
    old_password_cache = {"password": None}
    # --- Load Employee Details ---
    def load_employee():
        email = e1.get().strip()
        password = e2.get().strip()
        if email == '' or password == '':
            ms.showerror("Error", "Enter both Email and Password", parent=w24)
            return
        k.execute("SELECT FULL_name, DOB, mobile_no, Position, Salary, password FROM Employee WHERE Email_id=? AND password=?",(email, password))
        emp = k.fetchone()
        if emp:
            old_password_cache["password"] = emp[5]

            # Show editable fields
            l6.place(x=150, y=400)
            e3.place(x=500, y=400)
            e3.delete(0, END)
            e3.insert(0, emp[0])
            l7.place(x=150, y=450)
            e4.place(x=500, y=450)
            e4.delete(0, END)
            e4.insert(0, emp[1])
            l8.place(x=150, y=500)
            e5.place(x=500, y=500)
            e5.delete(0, END)
            e5.insert(0, emp[2])
            l9.place(x=150, y=550)
            e6.place(x=500, y=550)
            e6.delete(0, END)
            e6.insert(0, emp[3])
            l10.place(x=150, y=600)
            e7.place(x=500, y=600)
            e7.delete(0, END)
            e7.insert(0, emp[4])
            # Password change fields
            l11.place(x=150, y=650)
            e8.place(x=500, y=650)
            l12.place(x=150, y=700)
            e9.place(x=500, y=700)

            save_btn.place(x=400, y=780)
        else:
            ms.showerror("Error", "Employee not found or wrong password!", parent=w24)
    def save_changes():
        full_name = e3.get().strip()
        dob = e4.get().strip()
        mob = e5.get().strip()
        position = e6.get().strip()
        salary = e7.get().strip()
        email = e1.get().strip()
        new_pw = e8.get().strip()
        confirm_pw = e9.get().strip()
        if new_pw == '' and confirm_pw == '':
            final_password = old_password_cache["password"]
        else:
            if new_pw != confirm_pw:
                ms.showerror("Error", "New password & confirm password must match!", parent=w24)
                return
            final_password = new_pw
        if full_name == '' or dob == '' or mob == '' or position == '' or salary == '':
            ms.showerror("Error", "All fields except password must be filled!", parent=w24)
            return
        try:
            k.execute(""" UPDATE Employee SET FULL_name=?, DOB=?, mobile_no=?, Position=?, Salary=?, password=?WHERE Email_id=?""", (full_name, dob, mob, position, salary, final_password, email))
            d.commit()
            ms.showinfo("Success", "Employee details updated successfully!", parent=w24)
            w24.destroy()
        except Exception as ex:
            ms.showerror("DB Error", f"Update failed!\n{ex}", parent=w24)

    b1 = Button(w24, text="Load Employee", font=("Arial", 20), bg="orange", fg="white", command=load_employee)
    b1.place(x=400, y=330)
    save_btn = Button(w24, text="Save Changes", font=("Arial", 20), bg="green", fg="white", command=save_changes)

    w24.mainloop()
def show_all_accounts():
    import tkinter as tk
    w25 = Toplevel()
    w25.title("All Accounts")
    w25.geometry("1500x500")
    w25.config(bg="steelblue1")
    w25.resizable(False, False)
    l1 = Label(w25, text="Secure Trust Bank", font=("arial", 30, 'bold', 'underline'), bg='steel blue1', fg='navy')
    l1.pack()
    l4 = Label(w25, text="All Customers Account", font=("Arial", 25, "bold"), bg="steel blue1", fg="navy")
    l4.pack()
    canvas = Canvas(w25, bg="steelblue1")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    v_scroll = Scrollbar(w25, orient=tk.VERTICAL, command=canvas.yview)
    v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=v_scroll.set)
    table_frame = tk.Frame(canvas, bg="steelblue1")
    window = canvas.create_window((0, 0), window=table_frame, anchor='nw')
    k.execute("SELECT * FROM User_Data1")
    rows = k.fetchall()
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(window, width=max(canvas.winfo_width(), table_frame.winfo_reqwidth()))
    table_frame.bind("<Configure>", on_frame_configure)
    headers = ["First Name", "Last Name", "DOB", "Email ID", "Mobile_no.", "Password", "ID", "Balance", "Type"]
    for i, header in enumerate(headers):
        Label(table_frame, text=header, font=("Arial", 12, 'bold'), bg='lightgrey',padx=5, pady=5, borderwidth=1, relief="solid", width=15).grid(row=0, column=i)
    for row_num, row in enumerate(rows):
        for col_num, value in enumerate(row):
            Label(table_frame, text=value, font=("Arial", 11), bg='white',padx=5, pady=5, borderwidth=1, relief="solid", width=15).grid(row=row_num + 1, column=col_num)
    w25.mainloop()
def show_all_employees():
    import tkinter as tk
    from tkinter import Toplevel, Label, Canvas, Scrollbar
    w26 = Toplevel()
    w26.title("All Employees")
    w26.geometry("1500x500")
    w26.config(bg="#e6f0ff")
    w26.resizable(False, False)
    l1 = Label(w26, text="Secure Trust Bank", font=("times new roman", 30, 'bold', 'underline'), bg='#e6f0ff', fg='#003366')
    l1.pack()
    l4 = Label(w26, text="All Employees", font=("times new roman", 30, 'bold', 'underline'), bg='#e6f0ff', fg="#4169E1")
    l4.pack()

    canvas = Canvas(w26, bg="#e6f0ff")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    v_scroll = Scrollbar(w26, orient=tk.VERTICAL, command=canvas.yview)
    v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=v_scroll.set)
    table_frame = tk.Frame(canvas, bg="#e6f0ff")
    window = canvas.create_window((0, 0), window=table_frame, anchor='nw')
    k.execute("SELECT * FROM Employee")
    emp_rows = k.fetchall()
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(window, width=max(canvas.winfo_width(), table_frame.winfo_reqwidth()))
    table_frame.bind("<Configure>", on_frame_configure)
    headers = ["Full Name", "DOB", "Mobile No", "Email ID", "Password", "Position", "Salary", "Employee ID"]
    for i, header in enumerate(headers):
        Label(
            table_frame, text=header, font=("Arial", 12, 'bold'),
            bg='lightgrey', padx=5, pady=5, borderwidth=1, relief="solid", width=18 ).grid(row=0, column=i)
    for row_num, row in enumerate(emp_rows):
        for col_num, value in enumerate(row):
            Label(
                table_frame, text=value, font=("Arial", 11),
                bg='white', padx=5, pady=5, borderwidth=1, relief="solid", width=18
            ).grid(row=row_num + 1, column=col_num)

    w26.mainloop()
def show_admin_profile(admin_id):
    w25 = Toplevel()
    w25.title("Admin Profile")
    w25.geometry("650x400")
    w25.config(bg="steelblue1")
    w25.resizable(False, False)
    k.execute("SELECT ID,FULL_name,DOB, mobile_no, Email_id, Password FROM Admin WHERE ID=?", (admin_id,))
    data = k.fetchone()
    if not data:
        ms.showerror("Error", "Admin ID not found")
        return
    Label(w25, text="Admin Profile", font=("Arial", 25, "bold", "underline"), bg=w25["bg"], fg="#003366").pack(pady=20)
    labels = ["ID","Name","Date of Birth", "Mobile Number","Email ID", "Password"]
    for i, field in enumerate(data):
        Label(w25, text=f"{labels[i]}: {field}", font=("Arial", 16), bg=w25["bg"], anchor='w').pack(pady=5, anchor='w', padx=30)
    w25.mainloop()
start()


