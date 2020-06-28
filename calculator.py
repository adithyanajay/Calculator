from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("320x480")
root.minsize(320,480)

# vaiables
operator = ""
text_Input = StringVar()
num=""
# Function for button on click.
def btnClick(number):
    global operator,text_Input,num
    operator=operator + str(number)
    text_Input.set(operator)
# Function for Equal btn.
def btnEquals():
    global operator
    maths=str(eval(operator))
    text_Input.set(maths)
    operator=""
# Function for clear btn.
def btnClear():
    global operator
    operator=""
    text_Input.set("")
# Function for deleting the last number or operator.
def btndel():
    global text_Input,operator
    temp = text_Input.get()
    temp = temp[0:-1]
    operator=temp
    text_Input.set(temp)

# Button function
def button(frame,text_i,font=("Copper Black",21),number=num):
    global num
    button_Def = Button(frame,
                        text=text_i,
                        font=font,
                        fg="white",
                        bg="black",
                        border=0,
                        command=lambda:btnClick(number)
                        
)
    button_Def.pack(fill="both",expand=True,padx=1,pady=1,side="left")


#Frames
frame_label = Frame(root,
                bg="#333029",
                height="157",
                width="322",
                )

frame_label.pack(expand=True,fill="both")
frame_1 = Frame(root,
                bg="#333029")
frame_1.pack(expand=True, fill="both")

frame_2 = Frame(root,
                bg="#333029")
frame_2.pack(expand=True,fill="both")

frame_3 = Frame(root,
                bg="#333029")
frame_3.pack(expand=True,fill="both")

frame_4 = Frame(root,
                bg="#333029")
frame_4.pack(expand=True,fill="both")

frame_5 = Frame(root,
                bg="#333029")
frame_5.pack(expand=True, fill="both")


# Label or the screen
screen = Label(frame_label,
             font=("Arial",35),
             bg="#333029",
             border=0,
             fg="white",
             textvariable=text_Input,
             anchor="e"
             )

screen.pack(fill="both",expand=True)


# buttons
btn_per = button(frame_1,"%",number="%")
btn_c = Button(frame_1,
                text="C",
                font=("Copper Black",21),
                fg="white",
                bg="black",
                border=0,
                command=btnClear
                        
)
btn_c.pack(fill="both",expand=True,padx=1,pady=1,side="left")
btn_del =Button(frame_1,
                        text=("⌫"),
                        font=("Copper Black",16),
                        fg="white",
                        bg="black",
                        border=0,
                        command=btndel
                        
)
btn_del.pack(fill="both",expand=True,padx=1,pady=1,side="left")
btn_div = button(frame_1,"÷",font=("Copper Black",22),number="/")
btn_7 = button(frame_2,"7",number=7)
btn_8 = button(frame_2,"8",number=8)
btn_9 = button(frame_2,"9",number=9)
btn_multi = button(frame_2,"X", font=("Copper Black",17),number="*")
btn_4 = button(frame_3,"4",number=4)
btn_5 = button(frame_3,"5",number=5)
btn_6 = button(frame_3,"6",number=6)
btn_sub = button(frame_3,"-", font=("Copper Black",22),number="-")
btn_1 = button(frame_4,"1",number=1)
btn_2 = button(frame_4,"2",number=2)
btn_3 = button(frame_4,"3",number=3)
btn_add = button(frame_4,"+",font=("Copper Black",18),number="+")
btn_0 = button(frame_5,"0",number=0)
btn_dot = button(frame_5,".",number=".")
btn_equal = Button(frame_5,
                    text="       =        ",
                    bg="orange",
                    font=("Copper Black",20),
                    border=0,
                    command=btnEquals)
#btn_equal.config( height = 10,width = 50)
btn_equal.pack(fill="both", expand=True,padx=2,pady=2)
root.mainloop()