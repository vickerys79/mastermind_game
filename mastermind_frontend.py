import tkinter as tk
from tkinter import messagebox
from mastermind_backend import MastermindGame

class MastermindGUI:
    """
    The MastermindGUI class represents the front-end of the Mastermind game.
    It provides a graphical user interface (GUI) for playing the game.
    """

    def __init__(self, master):
        self.master = master
        self.master.title("Mastermind")
        self.game = MastermindGame()
        self.max_attempts = 10
        self.current_attempt = 1

        # Create GUI elements
        self.master.geometry("1400x450")  # Set the initial window size

        # Create color buttons
        self.color_buttons = []
        for color in ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]:
            button = tk.Button(master, text=color, width=8, height=2, command=lambda c=color: self.make_guess(c))
            self.color_buttons.append(button)
            button.pack(side=tk.LEFT)

        self.guess_label = tk.Label(master, text="Make a guess:")
        self.guess_label.pack()
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()
        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        # Create a board to display previous guesses and feedback
        self.board_frame = tk.Frame(master)
        self.board_frame.pack()
        self.board_label = tk.Label(self.board_frame, text="Previous Guesses:")
        self.board_label.pack()
        self.board_text = tk.Text(self.board_frame, width=40, height=10)
        self.board_text.pack()

        # Create a key for feedback responses
        self.key_frame = tk.Frame(master)
        self.key_frame.pack()
        self.key_label = tk.Label(self.key_frame, text="Key:")
        self.key_label.pack()
        self.key_text = tk.Text(self.key_frame, width=40, height=4)
        self.key_text.insert(tk.END, "R: Correct color and position\nW: Correct color, wrong position\nSpace: No match")
        self.key_text.config(state=tk.DISABLED)  # Disable editing
        self.key_text.pack()

        # Create a counter label for the current guess
        self.counter_label = tk.Label(master, text=f"Guess {self.current_attempt}/{self.max_attempts}")
        self.counter_label.pack()

        # Create a "Play Again" button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.play_again_button.pack()
        self.play_again_button.config(state=tk.NORMAL)  # Enable the "Play Again" button

    def make_guess(self, color):
        current_guess = self.guess_entry.get()
        current_guess += color[0]  # Use the first letter of the color
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.insert(0, current_guess)

    def check_guess(self):
        guess = self.guess_entry.get().upper()
        if len(guess) != 4 or not all(color in "RGBYOP" for color in guess):
            messagebox.showerror("Invalid Input", "Please enter a valid 4-color code.")
            return

        feedback = self.game.check_guess(guess)
        feedback_str = " ".join(feedback)

        if self.game.is_game_over(guess):
            messagebox.showinfo("Congratulations!", f"You guessed the code in {self.current_attempt} attempts.")
            self.reset_game()
        else:
            # Append the guess and feedback to the board
            self.board_text.insert(tk.END, f"Guess: {guess} - Feedback: {feedback_str}\n")
            self.guess_entry.delete(0, tk.END)  # Clear the guess entry field
            self.game.attempts += 1  # Increment attempts
            self.current_attempt += 1
            self.counter_label.config(text=f"Guess {self.current_attempt}/{self.max_attempts}")
            self.board_text.see(tk.END)  # Automatically scroll to the bottom

            # Remove the previous guess if the number of attempts exceeds the limit
            if self.current_attempt > self.max_attempts:
                messagebox.showinfo("Game Over", "You've run out of guesses. You lost.")
                self.play_again_button.config(state=tk.NORMAL)  # Enable the "Play Again" button
                self.submit_button.config(state=tk.DISABLED)  # Disable the "Submit" button

    def reset_game(self):
        self.game = MastermindGame()
        self.current_attempt = 1
        self.counter_label.config(text=f"Guess {self.current_attempt}/{self.max_attempts}")
        self.board_text.delete(1.0, tk.END)  # Clear the board
        self.play_again_button.config(state=tk.NORMAL)  # Enable the "Play Again" button
        self.submit_button.config(state=tk.NORMAL)  # Enable the "Submit" button
        self.guess_entry.delete(0, tk.END)  # Clear the guess entry field

if __name__ == "__main__":
    root = tk.Tk()
    game = MastermindGUI(root)
    root.mainloop()
