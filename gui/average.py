# final
from tkinter import *
from tkinter import messagebox
# Main window
root=Tk()
root.title("Average Calculator")
root.geometry('300x250')
root.configure(bg="blue") #for backgroud color
numbers = []
def add_number():
    try:
        num = float(entry.get())
        numbers.append(num)
        entry.delete(0, END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def calculate_average():
    if numbers:
        # 1,2,3,4,5,6,7,8,9,10
        # 1,3,5,7,9=25
        numbers1=numbers[::2]
        average = sum(numbers1) / len(numbers1)
        messagebox.showinfo("Average", f"The average is: {average:.3f}")
    else:
        messagebox.showerror("Error", "No numbers entered.")

# Widgets
label =Label(root, text="Enter a number:")
label.grid(row=0, column=1,padx=10,pady=10)

entry=Entry(root)
entry.grid(row=1, column=1,padx=10,pady=10)

add_button=Button(root, text="Add Number", command=add_number)
add_button.grid(row=2, column=1,padx=5, pady=5)

calculate_button=Button(root, text="Calculate Average", command=calculate_average)
calculate_button.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
