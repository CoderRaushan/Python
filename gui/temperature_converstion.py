# final 
from tkinter import *
root=Tk()
root.geometry('350x150')
root.title("Temperature Converter")
root.configure(bg="blue") #for backgroud color
# manipulation function
def fahrenhiet_to_celcius():
    fahrenhiet=float(fahrenhiet_entry.get())
    celcius_res=(fahrenhiet-32)*5/9
    celcus_entry.delete(0,END)
    celcus_entry.insert(0,f"{celcius_res:.2f}")

def celcius_to_fahrenhiet():
    celcus=float(celcus_entry.get())
    fahrenhiet_res=(9/5)*celcus+32
    fahrenhiet_entry.delete(0,END)
    fahrenhiet_entry.insert(0,f"{fahrenhiet_res:.2f}")

# pages
# celcus input label 
celcus=Label(root,text="Enter celcus:",bg="red",fg="white")
celcus.grid(row=0,column=0, padx=20, pady=10)
# celcus input 
celcus_entry=Entry(root)
celcus_entry.grid(row=1,column=0, padx=20, pady=10)
celcus_entry.insert(0,"00")
# fahrenhiet input label 
fahrenhiet=Label(root,text="Enter fahrenhiet:",bg="red",fg="white")
fahrenhiet.grid(row=0,column=1,padx=20, pady=10)
# fahrenhiet input 
fahrenhiet_entry=Entry(root)
fahrenhiet_entry.grid(row=1,column=1,padx=10, pady=10)
fahrenhiet_entry.insert(0,"32")
# button for  celcius
celcus_button=Button(root,text=">>>>",command=celcius_to_fahrenhiet)
celcus_button.grid(row=2,column=0,padx=20,pady=10)
# button for fahrenhiet
fahrenhiet_button=Button(root,text="<<<<",command=fahrenhiet_to_celcius)
fahrenhiet_button.grid(row=2,column=1,padx=20,pady=10)
# for image 
# image = PhotoImage(file="/download.jpeg")  # Change "image.png" to your image file path
# image_label = Label(root,image) 
# image_label.grid(row=3, column=2)
root.mainloop() 
