from tkinter import *
from random import randint

# Initialize the main window
root = Tk()
root.title("Number Guessing Game")
root.geometry("300x300")

# Generate a random number between 1 and 100
random_number = randint(1, 100)

# Function to check the user's guess
def check_guess():
    try:
        guess = int(guess_entry.get())
        if guess < random_number:
            result_label.config(text="Too low! Try again.")
        elif guess > random_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text="Correct! You guessed it!")
            guess_button.config(state=DISABLED)  # Disable button after correct guess
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Function to reset the game
def reset_game():
    global random_number
    random_number = randint(1, 100)
    result_label.config(text="Game reset! Guess again.")
    guess_entry.delete(0, END)
    guess_button.config(state=NORMAL)

# GUI Components
Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 14)).pack(pady=10)

guess_entry = Entry(root, font=("Helvetica", 12))
guess_entry.pack(pady=5)

guess_button = Button(root, text="Submit Guess", font=("Helvetica", 12), command=check_guess)
guess_button.pack(pady=10)

result_label = Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

reset_button = Button(root, text="Reset Game", font=("Helvetica", 12), command=reset_game)
reset_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
