from tkinter import *
import random
root=Tk()
root.title("random no game")
root.geometry('250x150')

computer_guess=random.randint(1,100)
def randomfun():
 user_guess=int(input_entry.get())
 if(computer_guess==user_guess):
    input_label.config(text="You won!")
   
 elif(computer_guess>user_guess):
    input_label.config(text="Too low try again!")
    
 else:
    input_label.config(text="Too high try again!")

# input label 
input_label=Label(root,text="Enter a random no b/w 1 to 100")
input_label.grid(row=0,column=0,padx=10,pady=10)
# input Entry 
input_entry=Entry(root)
input_entry.grid(row=1,column=0,padx=10,pady=10)
# submit btn 
submit_btn=Button(root,text="Submit",command=randomfun)
submit_btn.grid(row=2,column=0,padx=10,pady=10)
root.mainloop()