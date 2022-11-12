from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
from mysql.connector import Error

def login_page():
    signup_window.destroy()
    import login

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    ConfirmPasswordEntry.delete(0, END)
    check.set(0)



def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or ConfirmPasswordEntry.get()=='':
        messagebox.showerror('Erorr!!', 'All fields are required')
    elif passwordEntry.get() != ConfirmPasswordEntry.get():
        messagebox.showerror('Erorr!!', 'Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Erorr!!', 'Please accept terms & conditions') 
    else:
        try :
            con = mysql.connector.connect(host='127.0.0.1', user='root', port='3306',
            password='Keyboard@2017', )
            mycursor = con.cursor()
        except:
            messagebox.showerror('Erorr!!', 'Database connectivity issue') 
            return
        
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100) , password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        
        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get(), ))

        row = mycursor.fetchone()

        if row != None:
            messagebox.showerror('Erorr!!', 'Username already exist')
        else:
            query = 'insert into data(email, username, password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import login


        

        
    
    


signup_window = Tk()

signup_window.title('SignUp Page')
signup_window.resizable(False,False)


background = ImageTk.PhotoImage(file=r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\bg.jpg')
bgLabel = Label(signup_window, image=background)
bgLabel.grid()



frame = Frame(signup_window, bg='white' )
frame.place(x=554, y=100)

heading = Label(frame, text='Create an Account', font=('Microsoft Yahei UI Light', 18, 'bold'),
 bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=30, pady=(10,5))

emailLabel = Label(frame, text='Email', 
font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white', fg= 'firebrick1')
emailLabel.grid(row=1, column=0,sticky='w', padx=25, pady=(10,2) )

emailEntry = Entry(frame, width=30, 
font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1' )
emailEntry.grid(row=2, column=0, sticky='W', padx=25 )

usernameLabel = Label(frame, text='Username', 
font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white', fg= 'firebrick1')
usernameLabel.grid(row=3, column=0,sticky='w', padx=25, pady=(10,2) )

usernameEntry = Entry(frame, width=30, 
font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1' )
usernameEntry.grid(row=4, column=0, sticky='W', padx=25 )

passwordLabel = Label(frame, text='Password', 
font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white', fg= 'firebrick1')
passwordLabel.grid(row=5, column=0,sticky='w', padx=25, pady=(10,2) )

passwordEntry = Entry(frame, width=30, 
font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1' )
passwordEntry.grid(row=6, column=0, sticky='W', padx=25 )

ConfirmPasswordLabel = Label(frame, text='Confirm Password', 
font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white', fg= 'firebrick1')
ConfirmPasswordLabel.grid(row=7, column=0,sticky='w', padx=25, pady=(10,2) )

ConfirmPasswordEntry = Entry(frame, width=30, 
font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1' )
ConfirmPasswordEntry.grid(row=8, column=0, sticky='W', padx=25 )

check = IntVar()

termsandconditions = Checkbutton(frame, 
text='I agree to terms and conditions', 
font=('Microsoft Yahei UI Light', 10, 'bold'), fg='blue', bg='white',
activebackground='white', activeforeground='blue', cursor='hand2', variable=check )
termsandconditions.grid(row=9, column=0, pady=10, padx=15)

signupButton = Button(frame, text='SIGN UP', 
font=('Open Sans', 15, 'bold'), fg='white', bg='firebrick1',
activebackground='firebrick1', activeforeground='white', cursor='hand2',
width=15, command=connect_database )
signupButton.grid(row=10, column=0, padx=15, pady=(2,10))

alreadyAccountLabel = Label(frame, text="Don't have an account?", 
font=('Open Sans', 9, 'bold'), fg='blue', bg='white', )
alreadyAccountLabel.grid(row=11, column=0, sticky='w' ,padx=10, pady=(5,5))

loginButton = Button(frame, text='LogIn', 
font=('Open Sans', 9, 'bold'), fg='firebrick1', bg='white',
activebackground='firebrick1', activeforeground='white', 
cursor='hand2', bd=0, command=login_page )
loginButton.place(x=155, y=408)



signup_window.mainloop()