from tkinter import *
root=Tk()
# window size
root.geometry("440x200")
root.minsize(350,180)
root.maxsize(690,370)
# title
root.title("Temperature converter")
root.configure(bg='black')


# celcius_to_fahrenhiet 
def celcius_to_fahrenhiet():
    celcius=float(celcius_entry.get())
    fahrenhiet_res=(9/5)*celcius+32
    fahrenhiet_entry.delete(0,END)
    fahrenhiet_entry.insert(0,f"{fahrenhiet_res:.2f}")

# celcius_to_fahrenhiet
def fahrenhiet_to_celsius():
    fahrenheit = float(fahrenhiet_entry.get())
    celsius_res=(5/9)*(fahrenheit-32)
    celcius_entry.delete(0, END)
    celcius_entry.insert(0, f"{celsius_res:.2f}")






# title icon
# image="2.webp"
# root.iconbitmap(image)

# for celcius 
celcius_lable=Label(root,text="Enter celcius",fg="white",bg="black")
celcius_lable.grid(row=0,column=0,padx=20,pady=10)
celcius_entry=Entry(root)
celcius_entry.grid(row=1,column=0,padx=20,pady=10)
celcius_entry.insert(0,"00")
# for fahrenhiet 

fahrenhiet_lable=Label(root,text="Enter fahrenhiet",fg="white",bg="black")
fahrenhiet_lable.grid(row=0,column=1,padx=20,pady=10)

fahrenhiet_entry=Entry(root)
fahrenhiet_entry.grid(row=1,column=1,padx=20,pady=10)
fahrenhiet_entry.insert(0,"32")

# for celcius button
celcius_btn=Button(root,text=">>>>",bg="yellow",command=celcius_to_fahrenhiet)
celcius_btn.grid(row=2,column=0,padx=20,pady=10)

# for fahrenhiet button 
fahrenhiet_btn=Button(root,text=">>>>",bg="yellow",command=fahrenhiet_to_celsius)
fahrenhiet_btn.grid(row=2,column=1,padx=20,pady=10)

root.mainloop()
