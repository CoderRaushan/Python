from tkinter import *
root=Tk()
root.title("Guess the Number Game")
root.geometry('450x350')
root.configure(bg="blue") #for backgroud color
# manipulating functions
def new_game():
    global low, high, current_guess
    low = 1
    high = 100
    current_guess = (low + high) // 2
    guess_label.config(text=f"Computer's guess: {current_guess}")
    too_small_button.config(state=NORMAL)
    too_large_button.config(state=NORMAL)
    correct_button.config(state=NORMAL)
    new_game_button.config(state=DISABLED)

def too_small():
    global low, high, current_guess
    low = current_guess + 1
    current_guess = (low + high) // 2
    guess_label.config(text=f"Computer's guess: {current_guess}")

def too_large():
    global low, high, current_guess
    high = current_guess - 1
    current_guess = (low + high) // 2
    guess_label.config(text=f"Computer's guess: {current_guess}")

def correct():
    guess_label.config(text=f"Computer's guess: {current_guess} (Correct!)")
    too_small_button.config(state=DISABLED)
    too_large_button.config(state=DISABLED)
    correct_button.config(state=DISABLED)
    new_game_button.config(state=NORMAL)


low = 1
high = 100
current_guess = (low + high) // 2

# Create the GUI components
guess_label =Label(root, text=f"Computer's guess: {current_guess}")
guess_label.grid(row=0, column=0, columnspan=3, pady=10)

too_small_button = Button(root, text="Too small", command=too_small)
too_small_button.grid(row=1, column=0, padx=10, pady=10)

too_large_button = Button(root, text="Too large", command=too_large)
too_large_button.grid(row=1, column=1, padx=10, pady=10)

correct_button = Button(root, text="Correct", command=correct)
correct_button.grid(row=1, column=2, padx=10, pady=10)

new_game_button = Button(root, text="New game", command=new_game)
new_game_button.grid(row=2, column=0, columnspan=3, pady=10)
new_game_button.config(state=DISABLED)

root.mainloop()
