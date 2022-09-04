'''CALCULATOR'''


# importTkinter
from tkinter import *
from tkinter import ttk

#colors
color_1 = "#5A5673"  #grey
color_2 = "#323040"

#create window
root = Tk()
root.title("Calculadora")

# def window size
root.geometry("435x518")
root.minsize(435, 518)
root.maxsize(435, 518)

# Frames
frame_screen = Frame(root, width=435, height=135, background=color_1)
frame_screen.grid(row=0, column=0)

frame_body = Frame(root, width=435, height=418, background=color_2)
frame_body.grid(row=1, column=0)



all_value = ''



#Label
value_text = StringVar()

#Function
def value_entry(event):
    global all_value  #variable global
    all_value =  all_value + str(event)     
   
    #passing value to the screen
    value_text.set(all_value)
   


# function calculate
def calculate():
    global all_value
    resolucion= eval(all_value)   
    value_text.set(str(resolucion))

# function delete
def clear():
    global all_value
    all_value = ""
    value_text.set("")




app_label = Label(frame_screen, textvariable=value_text, width=18, height=5, padx=10, relief=FLAT, anchor="e", justify=RIGHT, font="Times 34 ", bg=color_1, fg="white")
app_label.place(x=0,y=0)


# Buttom

# first row
bot1 = Button(frame_body, text="C",width=20, height=3, bg="grey", fg ="black", font="Times 15 bold",relief=RAISED, overrelief=RIDGE, command= clear)
bot1.place(x=0, y=0)
bot2 = Button(frame_body,text="%",width=9, height=3, bg="grey", fg="black", font="Times 15 bold", command = lambda: value_entry('%'))
bot2.place(x=220,y=0)
bot3 = Button(frame_body,text="/",width=9, height=3, bg="orange", fg="purple", font="times 15 bold", command = lambda: value_entry('/'))
bot3.place(x=330,y=0)

#second row
bot4 = Button(frame_body,text="7",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('7'))
bot4.place(x=0,y=77)
bot5 = Button(frame_body,text="8",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('8'))
bot5.place(x=108,y=77)
bot6 = Button(frame_body,text="9",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('9'))
bot6.place(x=220,y=77)
bot7 = Button(frame_body,text="*",width=9, height=3, bg="orange", fg="purple", font="times 15 bold", command = lambda: value_entry('*'))
bot7.place(x=330,y=77)


#third row
bot8 = Button(frame_body,text="4",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('4'))
bot8.place(x=0,y=154)
bot9 = Button(frame_body,text="5",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('5'))
bot9.place(x=108,y=153)
bot10 = Button(frame_body,text="6",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('6'))
bot10.place(x=220,y=153)
bot11 = Button(frame_body,text="-",width=9, height=3, bg="orange", fg="purple", font="times 15 bold", command = lambda: value_entry('-'))
bot11.place(x=330,y=153)

#fourth row
bot12 = Button(frame_body,text="1",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('1'))
bot12.place(x=0,y=229)
bot13 = Button(frame_body,text="2",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('2'))
bot13.place(x=108,y=229)
bot14 = Button(frame_body,text="3",width=9, height=3, bg="grey", fg="black", font="times 15 italic", command = lambda: value_entry('3'))
bot14.place(x=220,y=229)
bot15 = Button(frame_body,text="+",width=9, height=3, bg="orange", fg="purple", font="times 15 bold", command = lambda: value_entry('+'))
bot15.place(x=330,y=229)

# final row
bot16 = Button(frame_body, text="0",width=20, height=3, bg="grey", fg ="black", font="Times 15 bold",relief=RAISED, overrelief=RIDGE, command = lambda: value_entry('0'))
bot16.place(x=0, y=305)
bot17 = Button(frame_body,text=".",width=9, height=3, bg="grey", fg="black", font="Times 15 bold", command = lambda: value_entry('.'))
bot17.place(x=220,y=305)
bot18 = Button(frame_body,text="=",width=9, height=3, bg="orange", fg="purple", font="times 15 bold", command = calculate)
bot18.place(x=330,y=305)


root.mainloop()
