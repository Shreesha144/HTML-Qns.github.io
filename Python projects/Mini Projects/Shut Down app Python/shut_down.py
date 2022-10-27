from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def log_out():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="blue")

r_button = Button(st, text="Restart", font=("Time New Roman", 20, "bold"), 
relief=RAISED, cursor="plus", command=restart)

r_button.place(x=150, y=60, height=50, width=200)


log_button = Button(st, text="Log Out", font=("Time New Roman", 20, "bold"), 
relief=RAISED, cursor="plus", command=log_out)

log_button.place(x=150, y=160, height=50, width=200)

st_button = Button(st, text="Shut Down", font=("Time New Roman", 20, "bold"), 
relief=RAISED, cursor="plus", command=shutdown)

st_button.place(x=150, y=260, height=50, width=200)














st.mainloop()