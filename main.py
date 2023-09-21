import tkinter as tk
from tkinter import ttk


def new_game():
    global secret_number, remaining_guesses
    secret_number = None
    remaining_guesses = 10
    entry_secret_number.config(state="normal")
    entry_player_guess.config(state="normal")
    entry_secret_number.delete(0, tk.END)
    entry_player_guess.delete(0, tk.END)
    label_result.config(text="")
    label_turn.config(
        text="Player 1, save your secret number:", foreground="black")
    label_title.config(foreground="blue")
    label_title.after(1000, lambda: label_title.config(foreground="blue"))


def save_secret_number():
    global secret_number
    try:
        secret_number = int(entry_secret_number.get())
        entry_secret_number.config(state="disabled")
        label_turn.config(
            text="Player 2's Turn (10 guesses remaining)", foreground="black")
    except ValueError:
        label_turn.config(
            text="Please enter a valid number as your secret number", foreground="red")


def check_guess():
    global remaining_guesses
    if secret_number is None:
        label_turn.config(
            text="Player 1, please save your secret number first.", foreground="red")
        return

    guess = int(entry_player_guess.get())
    remaining_guesses -= 1

    if guess == secret_number:
        label_result.config(
            text=f"Player 2 wins! The number was {secret_number}", foreground="green")
        entry_player_guess.config(state="disabled")
        label_turn.config(foreground="green")
    elif remaining_guesses == 0:
        label_result.config(
            text=f"Player 2 ran out of guesses. The number was {secret_number}", foreground="red")
        entry_player_guess.config(state="disabled")
        label_turn.config(foreground="red")
    elif guess < secret_number:
        label_result.config(
            text=f"Player 2's guess is too low ({remaining_guesses} guesses remaining)", foreground="red")
        entry_player_guess.delete(0, tk.END)
    else:
        label_result.config(
            text=f"Player 2's guess is too high ({remaining_guesses} guesses remaining)", foreground="red")


window = tk.Tk()
window.title("Guess the Number Game")

title_font = ("Helvetica", 24, "bold")
label_font = ("Arial", 16)
button_font = ("Arial", 14)
bg_color = "#F5F5F5"  
button_color = "#4CAF50"  
text_color = "#333333"  

window.configure(bg=bg_color)

frame_title = ttk.Frame(window)
label_title = ttk.Label(
    frame_title, text="Guess the Number Game", font=title_font, foreground="blue")
label_title.grid(row=0, column=0, padx=10, pady=10)
frame_title.grid(row=0, column=0, columnspan=2)

label_instruction1 = ttk.Label(
    window, text="Player 1, enter your secret number (1-100):", font=label_font, foreground=text_color)
entry_secret_number = ttk.Entry(window, font=label_font)
button_save = ttk.Button(
    window, text="Save", command=save_secret_number, style='TButton')
label_instruction2 = ttk.Label(
    window, text="Player 2, guess the secret number (10 guesses):", font=label_font, foreground=text_color)
entry_player_guess = ttk.Entry(window, font=label_font)
button_guess = ttk.Button(window, text="Guess",
                          command=check_guess, style='TButton')
label_result = ttk.Label(window, text="", font=label_font)
label_turn = ttk.Label(window, text="", font=label_font)
button_new_game = ttk.Button(
    window, text="New Game", command=new_game, style='TButton')

label_instruction1.grid(row=1, column=0, columnspan=2)
entry_secret_number.grid(row=2, column=0, padx=10, pady=5)
button_save.grid(row=2, column=1, padx=10, pady=5)
label_instruction2.grid(row=3, column=0, columnspan=2)
entry_player_guess.grid(row=4, column=0, padx=10, pady=5)
button_guess.grid(row=4, column=1, padx=10, pady=5)
label_result.grid(row=5, column=0, columnspan=2, pady=10)
label_turn.grid(row=6, column=0, columnspan=2)
button_new_game.grid(row=7, column=0, columnspan=2, pady=10)

new_game()

window.mainloop()
