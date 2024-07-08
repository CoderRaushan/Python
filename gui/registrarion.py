from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Reg Form")
root.geometry('450x350')
root.configure(bg="blue") #for backgroud color
def submit_form():
    name=name_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    gender=gender_var.get()

    form_arr=[]
    if(hobbies_cricket_var.get()):
      form_arr.append("Cricket")

    if(hobbies_football_var.get()):
      form_arr.append("Football")

    if(hobbies_music_var.get()):
      form_arr.append("Music")

    if(hobbies_walking_var.get()):
      form_arr.append("Walking")

    if(hobbies_movie_var.get()):
      form_arr.append("Movie")
    
    if(hobbies_game_var.get()):
      form_arr.append("Game")

    form_summary=(
      f"Name:{name}\n"
      f"Email:{email}\n"
      f"Password:{password}\n"
      f"Gender:{gender}\n"
      f"Hobbies: {', '.join(form_arr) if form_arr else 'none'}\n"
    )
    messagebox.showinfo("Form submission summary",form_summary)

# Variables
gender_var=StringVar(value='Male')
hobbies_cricket_var=BooleanVar()
hobbies_football_var=BooleanVar()
hobbies_music_var=BooleanVar()
hobbies_walking_var=BooleanVar()
hobbies_movie_var=BooleanVar()
hobbies_game_var=BooleanVar()
# name 
name_label=Label(root,text="Name")
name_label.grid(row=0,column=0,padx=10,pady=10)
# name Entry 
name_entry=Entry(root)
name_entry.grid(row=0,column=1,padx=10,pady=10)
# email 
email_label=Label(root,text="Email")
email_label.grid(row=1,column=0,padx=10,pady=10)
# entry 
email_entry=Entry(root)
email_entry.grid(row=1,column=1,padx=10,pady=10)
# password 
password_label=Label(root,text="Password")
password_label.grid(row=2,column=0,padx=10,pady=10)
# entry 
password_entry=Entry(root)
password_entry.grid(row=2,column=1,padx=10,pady=10)
# gender 
gender_label=Label(root,text="Gender")
gender_label.grid(row=3,column=0,padx=10,pady=10)
# radio button 
male_radio=Radiobutton(root,text="Male",value="Male",variable=gender_var)
male_radio.grid(row=3,column=1,padx=10,pady=10)
female_radio=Radiobutton(root,text="Female",value="Female",variable=gender_var)
female_radio.grid(row=3,column=2,padx=10,pady=10)
other_radio=Radiobutton(root,text="Other",value="Other",variable=gender_var)
other_radio.grid(row=3,column=3,padx=10,pady=10)
# hobbies 
hobbies_label=Label(root,text="Hobbies")
hobbies_label.grid(row=4,column=0,padx=10,pady=10)
# hobbies Checkbutton 
hobbies_cricket=Checkbutton(root,text="Cricket",variable=hobbies_cricket_var)
hobbies_cricket.grid(row=4,column=1,padx=10,pady=10)

hobbies_football=Checkbutton(root,text="Football",variable=hobbies_football_var)
hobbies_football.grid(row=4,column=2,padx=10,pady=10)

hobbies_music=Checkbutton(root,text="Music",variable=hobbies_music_var)
hobbies_music.grid(row=4,column=3,padx=10,pady=10)

hobbies_walking=Checkbutton(root,text="Walking",variable=hobbies_walking_var)
hobbies_walking.grid(row=5,column=1,padx=10,pady=10)

hobbies_movie=Checkbutton(root,text="Movie",variable=hobbies_movie_var)
hobbies_movie.grid(row=5,column=2,padx=10,pady=10)

hobbies_game=Checkbutton(root,text="Game",variable=hobbies_game_var)
hobbies_game.grid(row=5,column=3,padx=10,pady=10)

# submit_button 
submit_button=Button(root,text="Submit",command=submit_form)
submit_button.grid(row=6,column=2,padx=10,pady=10)
root.mainloop()