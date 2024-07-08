from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('400x200')
root.title("tax calculator")
root.config(bg="blue")

# maniputting functions

def income_tax():
    gross_income=float(grossientry.get())
    dependents=float(dependent_Entry.get())
    taxable_income = gross_income - (dependents * 1000)
    
    if taxable_income <= 18200:
        tax = 0
    elif taxable_income <= 45000:
        tax = (taxable_income - 18200) * 0.19
    elif taxable_income <= 120000:
        tax = 5092 + (taxable_income - 45000) * 0.32
    else:
        tax = 29467 + (taxable_income - 120000) * 0.37
    
    totaltax_label.config(text=f"Total tax:{tax:.2f}")
    
    tax_summary=(
        f"Total Tax:{tax:.2f}"
    )
    messagebox.showinfo("Tax calculator summary",tax_summary)
    # totaltax_entry.delete(0,END)
    # totaltax_entry.insert(0,tax)

#end of the functionh
gross_incomeleb=Label(root,text="Enter Gross income")
gross_incomeleb.grid(row=0,column=0,padx=10,pady=10)

grossientry=Entry(root)
grossientry.grid(row=0,column=1,padx=10,pady=10)

dependent_label=Label(root,text="Enter dependents")
dependent_label.grid(row=1,column=0,padx=10,pady=10)

dependent_Entry=Entry(root)
dependent_Entry.grid(row=1,column=1,padx=10,pady=10)

totaltax_label=Label(root,text="Total tax:")
totaltax_label.grid(row=2,column=0,padx=10,pady=10)

# totaltax_entry=Entry(root)
# totaltax_entry.grid(row=2,column=1,padx=10,pady=10)
# totaltax_entry.insert(0,"00")

calculate_button=Button(root,text="Calculat Tax",command=income_tax)
calculate_button.grid(row=3,column=1,padx=10,pady=10)

root.mainloop()