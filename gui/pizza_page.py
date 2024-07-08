from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('550x250')
root.title(" Domino's Pizza Order")
root.configure(bg="blue") #for backgroud color

def place_order():
 size=size_var.get()
 crust_type=crust_var.get()
 if(size=='Small'):
   pizza_price=5 
 elif(size=='Medium'):
   pizza_price=10
 elif(size=='Large'):
   pizza_price=15

 toppings_arr=[]
 toppings_prize=0
 if(Peppernoi_var.get()):
   toppings_arr.append("Peppernoi")
   toppings_prize+=1

 if(Sausage_var.get()):
   toppings_arr.append("Sausage")
   toppings_prize+=1

 if(Mushrooms_var.get()):
   toppings_arr.append("Mushrooms")
   toppings_prize+=1 

 if(Olives_var.get()):
   toppings_arr.append("Olives")
   toppings_prize+=1

 if(Onions_var.get()):
   toppings_arr.append("Onions")
   toppings_prize+=1
 
 total_pizza_price=pizza_price+toppings_prize
 order_summary=(
   f"Pizza Order Summary:\n"
   f"Size:{size}\n"
   f"Crust:{crust_type}\n"
   f"Toppings:{ ', '.join(toppings_arr) if toppings_arr else 'None'}\n"
   f"Total Cost:${total_pizza_price}"
 )
 messagebox.showinfo("Order Summary",order_summary)

# select the size and toppings by default
size_var=StringVar(value="Medium")
crust_var=StringVar(value="Thin")
Peppernoi_var=BooleanVar()
Sausage_var=BooleanVar()
Mushrooms_var=BooleanVar()
Olives_var=BooleanVar()
Onions_var=BooleanVar()

size_label=Label(root,text="Select Pizza Size:")
size_label.grid(row=0,column=0,padx=10,pady=10)

small_radio=Radiobutton(root,text="Small",value="Small",variable=size_var)
small_radio.grid(row=0,column=1,padx=10,pady=10)

medium_radio=Radiobutton(root,text="Medium",value="Medium",variable=size_var)
medium_radio.grid(row=0,column=2,padx=10,pady=10)

large_radio=Radiobutton(root,text="Large",value="Large",variable=size_var)
large_radio.grid(row=0,column=3,padx=10,pady=10)

# crust type

crust_label=Label(root,text="Select Crust Type:")
crust_label.grid(row=1,column=0,padx=10,pady=10)

regular_radio=Radiobutton(root,text="Regular",value="Regular",variable=crust_var)
regular_radio.grid(row=1,column=1,padx=10,pady=10)

thin_radio=Radiobutton(root,text="Thin",value="Thin",variable=crust_var)
thin_radio.grid(row=1,column=2,padx=10,pady=10)

stuffed_radio=Radiobutton(root,text="Stuffed",value="Stuffed",variable=crust_var)
stuffed_radio.grid(row=1,column=3,padx=10,pady=10)

# toppings

toppings_label=Label(root,text="Select Toppings:")
toppings_label.grid(row=2,column=0,padx=10,pady=10)

pepperoni_check=Checkbutton(root,text="Peppernoi",variable=Peppernoi_var)
pepperoni_check.grid(row=2,column=1,padx=10,pady=10)

Sausage_check=Checkbutton(root,text="Sausage",variable=Sausage_var)
Sausage_check.grid(row=2,column=2,padx=10,pady=10)

Mushrooms_check=Checkbutton(root,text="Mushrooms",variable=Mushrooms_var)
Mushrooms_check.grid(row=2,column=3,padx=10,pady=10)

Olives_check=Checkbutton(root,text="Olives",variable=Olives_var)
Olives_check.grid(row=3,column=1,padx=10,pady=10)

Onions_check=Checkbutton(root,text="Onions",variable=Onions_var)
Onions_check.grid(row=3,column=2,padx=10,pady=10)

# button of placing order
place_order=Button(root,text="Place Order",command=place_order)
place_order.grid(row=4,column=2,padx=10,pady=10)
root.mainloop()