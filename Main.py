import time
from tkinter import*
import chatbot as cb
main=Tk()
hold_down=False

# def Ask():
#     # print("clicked")
#     activity.insert(END, "Listening.....")
    
def btn_hold(event):
    hold_down=True
    while hold_down== True: 
        activity.delete(0,END)
        activity.insert(END, "Listening.....")
        cb.respone()
        hold_down = btn.bind('<ButtonRelease-1>',stop_motor)

def stop_motor(event):
    hold_down= False
    activity.delete(0,END)
    activity.insert(END, "Recognizing.....")  
    
def turn_off():
    activity.delete(0,END)
    
main.title("Chit-Chat Bot")

main.geometry("500x550")


l = Label(main, text="Chit-Chat Bot", font=("Arial", 25))
l.pack(pady = 20)

frame= Frame(main)
# sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20)
# sc.pack(side= RIGHT)
msg.pack(side=LEFT ,fill= BOTH, pady=10)

frame.pack()

frame2 = Frame(main)


activity = Listbox(main, font=("Verdana", 20), width=29, height=1)
activity.pack( pady=10, padx=10)
# textField= Entry(main, font=("Verdana", 20))
# textField.pack(fill= X, pady=10)

btn = Button(main, text="Speak", font=("Verdana", 20))
btn.pack(side=LEFT)
btn.bind('<Button-1>',btn_hold)

btn1 = Button(main, text="Stop", font=("Verdana", 20), command=turn_off)
btn1.pack(side=RIGHT)

main.mainloop()