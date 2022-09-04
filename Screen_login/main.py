from tkinter import *
from tkinter import Tk
from tkinter import messagebox


#colors
green = "#3fb5a3"
letra = "#403d3d"

# creating the window
window = Tk()
window.title("Login")
window.geometry("340x450")
window.config(background='white')
window.resizable(width=FALSE, height=FALSE)

# defining the frames
frame_up = Frame(window, width=450, height=80, bg='white', relief=FLAT)
frame_up.grid(row=0, column=0, pady=1, padx=0, sticky= NSEW)

frame_down = Frame(window, width=450, height=400, bg='white', relief=FLAT)
frame_down.grid(row=1, column=0, pady=1, padx=0, sticky= NSEW)

# config frame_up
l_log = Label(frame_up, text='LOGIN', anchor=NE, font='Ive 28', bg='white', fg=letra)
l_log.place(x=5, y=10)

l_row = Label(frame_up, text='',width=310,anchor=NW, font='Ive 1', bg=green, fg=letra)
l_row.place(x=10, y=60)

# user
user = ['Aelin', '5678']

#check user
def check_password():
    name = e_name.get()
    password = e_password.get()

    if name =='admin' and password =='admin':
        messagebox.showinfo('Login success', 'Welcome Admin!')
    elif user[0] == name and user[1] == password:

        #clear frame
        for widget in frame_down.winfo_children():
            widget.destroy()
            
            for widget in frame_up.winfo_children():
                widget.destroy()

                new_window()

    else:
        messagebox.showwarning('Error!','check your username and password')


# show user
def new_window():
    l_log = Label(frame_up, text='WELCOME', justify='center', font='Ive 30', bg='white', fg=letra)
    l_log.place(x=70, y=10)
    l_row = Label(frame_up, text='',width=310,anchor=NW, font='Ive 1', bg=green, fg=letra)
    l_row.place(x=10, y=60)

    l_log = Label(frame_down, text=user[0] +' Online ✅', anchor=NE, font='Ive 15', bg='white', fg=letra)
    l_log.place(x=5, y=0)

# config frame_down
l_name = Label(frame_down, text='Name *', anchor=NW, font='Ive 12 bold', bg='white')
l_name.place(x=10, y=30)
e_name = Entry(frame_down, width=25, justify='left', font=("times new roman", 18), highlightthickness=2, relief=SOLID)
e_name.place(x=14, y=60)


l_password = Label(frame_down, text='Password *', anchor=NW, font='Ive 12 bold', bg='white')
l_password.place(x=10, y=150)
e_password = Entry(frame_down, width=25, justify='left',show='*', font=("times new roman", 18), highlightthickness=2, relief=SOLID)
e_password.place(x=14, y=180)

bot = Button(frame_down, command=check_password, text='Enter', width=39, height=2, bg=green, anchor=CENTER, fg='black', font='ive 8 bold', relief=RAISED )
bot.place(x=15, y=290)


window.mainloop()