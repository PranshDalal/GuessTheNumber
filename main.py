import tkinter as tk
from tkinter import ttk
import random


def new_game():
    global secret_number, remaining_guesses, is_single_player
    secret_number = None
    remaining_guesses = 10
    is_single_player = False
    entry_secret_number.config(state="normal")
    entry_secret_number.delete(0, tk.END)
    entry_player_guess.delete(0, tk.END)
    label_result.config(text="")
    label_turn.config(
        text="Player 1, enter your secret number (1-100):", foreground="black")
    label_instruction1.config(
        text="Player 1, enter your secret number (1-100):")
    button_save.config(text="Save")
    label_instruction2.grid(row=3, column=0, columnspan=2)
    entry_secret_number.delete(0, tk.END)
    entry_player_guess.delete(0, tk.END)
    entry_secret_number.config(state="normal")
    entry_secret_number.delete(0, tk.END)
    entry_player_guess.config(state="normal")
    button_save.config(state="normal")
    button_guess.config(state="normal")
    label_instruction2.grid(row=3, column=0, columnspan=2)


def save_secret_number():
    global secret_number, is_single_player
    if is_single_player:
        num_digits = int(entry_secret_number.get())
        secret_number = random.randint(
            10 ** (num_digits - 1), 10 ** num_digits - 1)
        is_single_player = False  # Automatically switch to player 2's turn
        entry_secret_number.config(state="disabled")
        label_turn.config(
            text="Try to guess the secret number", foreground="black")
    else:
        try:
            secret_number = int(entry_secret_number.get())
            entry_secret_number.config(state="disabled")
            label_turn.config(
                text="Player 2's Turn (10 guesses remaining)", foreground="black")
        except ValueError:
            label_turn.config(
                text="Please enter a valid number as your secret number", foreground="red")


def switch_to_single_player_mode():
    global is_single_player
    is_single_player = True
    label_instruction1.config(
        text="Enter the number of digits for the secret number:")
    button_save.config(text="Generate Secret Number")
    label_instruction2.grid_remove()
    label_turn.config(text="You have 10 guesses remaining", foreground="black")


def switch_to_two_player_mode():
    global is_single_player
    is_single_player = False
    label_instruction1.config(
        text="Player 1, enter your secret number (1-100):")
    button_save.config(text="Save")
    label_instruction2.grid(row=3, column=0, columnspan=2)
    label_turn.config(
        text="Player 1's Turn (Enter your secret number)", foreground="black")


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
            text=f"The number was {secret_number}", foreground="green")
        entry_player_guess.config(state="disabled")
        label_turn.config(foreground="green")
    elif remaining_guesses == 0:
        label_result.config(
            text=f"Ran out of guesses. The number was {secret_number}", foreground="red")
        entry_player_guess.config(state="disabled")
        label_turn.config(foreground="red")
    elif guess < secret_number:
        label_result.config(
            text=f"Guess is too low ({remaining_guesses} guesses remaining)", foreground="red")
        entry_player_guess.delete(0, tk.END)
    else:
        label_result.config(
            text=f"Guess is too high ({remaining_guesses} guesses remaining)", foreground="red")


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

menu = tk.Menu(window)
window.config(menu=menu)
game_menu = tk.Menu(menu)
menu.add_cascade(label="Menu", menu=game_menu)
game_menu.add_command(label="1 Player Mode",
                      command=switch_to_single_player_mode)
game_menu.add_command(label="2 Player Mode", command=switch_to_two_player_mode)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=window.quit)

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
