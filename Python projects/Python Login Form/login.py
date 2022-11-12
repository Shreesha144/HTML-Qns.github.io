from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error



def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
    

def on_enterpass(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
    passwordEntry.config(show='*')

def hide():
    openEye.config(file=r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\closeye.png')
    passwordEntry.config(show='*')
    EyeBtn.config(command=show)

def show():
    openEye.config(file=r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\openeye.png')
    passwordEntry.config(show='')
    EyeBtn.config(command=hide)

def signup_page():
    login_window.destroy()
    import signup




def forget_pass():

    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Erorr!!', 'Please enter all the fields', parent=window)

        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Erorr!!', 'password and Confirm password not mathching', parent=window)

        else:
            con = mysql.connector.connect(host='127.0.0.1', user='root', port='3306',
            password='Keyboard@2017', database = 'userdata' )
            mycursor = con.cursor()

            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get(), ))

            row = mycursor.fetchone()

            if row==None:
                messagebox.showerror('Erorr!!', 'Wrong Username', parent=window)
            else:

                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password reset successful', parent = window)
                window.destroy()

        







        




    window = Toplevel()
    window.title('Change Password')
    bgPic = ImageTk.PhotoImage(file = r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\background.jpg')
    bgLabell = Label(window , image = bgPic)
    bgLabell.grid()

    heading_label = Label(window, text='Reset Password', font=('arial', '18', 'bold'), 
    bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('arial', '12', 'bold'),
    bg='white', fg='orchid' )
    userLabel.place(x=470, y=130)

    user_entry = Entry(window, width=25, fg='magenta2', font=('arial', '11', 'bold'),
    bd=0)
    user_entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    passwordLabel = Label(window, text='New Password', font=('arial', '12', 'bold'),
    bg='white', fg='orchid' )
    passwordLabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', '11', 'bold'),
    bd=0)
    newpass_entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmpassLabel = Label(window, text='Confirm Password', font=('arial', '12', 'bold'),
    bg='white', fg='orchid' )
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', '11', 'bold'),
    bd=0)
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submitButton = Button(window, text='Submit', bd=0, bg='magenta2', 
    fg='white', font=('Open Sans', '16', 'bold'), width=19, cursor='hand2',
    activebackground='magenta2', activeforeground='white',
    command = change_password )
    submitButton.place(x=470, y=390)

    






    






    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Erorr!!', 'All fields are required')
    else:
        try :
            con = mysql.connector.connect(host='127.0.0.1', user='root', port='3306',
            password='Keyboard@2017', )
            mycursor = con.cursor()
        except:
            messagebox.showerror('Erorr!!', 'Database connectivity issue') 
            return
        
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()

        if row == None :
            messagebox.showerror('Erorr!!', 'Invalid Username or Password ')
        else:
            messagebox.showinfo('Welcome', 'Login is successful')
        

            









login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file=r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\bg.jpg')

bgLabel = Label(login_window, image=bgImage)

bgLabel.grid(row=0, column=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'),
 bg='white', fg='firebrick1')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
bd=0, fg='firebrick1' )
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', on_enter)

Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
bd=0, fg='firebrick1' )
passwordEntry.place(x=580, y=280)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', on_enterpass)

Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=302)

openEye =  PhotoImage(file=r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\closeye.png')
EyeBtn = Button(login_window, image=openEye, bd=0, bg='white', 
activebackground='white', cursor='hand2', command=show)
EyeBtn.place(x=800, y=275)


forgetBtn = Button(login_window, text='forgot password?', bd=0, bg='white', 
activebackground='white', cursor='hand2', 
font=('Microsoft Yahei UI Light', 9, 'bold'), fg='firebrick1', 
activeforeground='firebrick1', command = forget_pass)
forgetBtn.place(x=715, y=310)


loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'),
bg='firebrick1', fg='white', activebackground='firebrick1',
 activeforeground='white', cursor='hand2',bd=0, width=8, command = login_user )
loginButton.place(x=650, y=360)

orLabel = Label(login_window, text='----------OR---------', font=('Open Sans', 16), 
fg='firebrick1', bg='white')
orLabel.place(x=620, y=410)

facebook_logo = PhotoImage(file=r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white' )
fbLabel.place(x=630, y=440)

google_logo = PhotoImage(file=r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\google.png')
googleLabel = Label(login_window, image=google_logo, bg='white' )
googleLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file=r'D:\Youtube Coding Projects\Python projects\Python Login Form\login_images\twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white' )
twitterLabel.place(x=750, y=440)

signupLabel = Label(login_window, text="Don't have an account? ", font=('Open Sans', 9, 'bold'), 
fg='firebrick1', bg='white')
signupLabel.place(x=580, y=500)

newaccountButton = Button(login_window, text='Create New One', font=('Open Sans', 9, 'bold'),
bg='white', fg='blue', activebackground='white',
 activeforeground='blue', cursor='hand2',bd=0, command=signup_page  )
newaccountButton.place(x=718, y=500)




login_window.mainloop()