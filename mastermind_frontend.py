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

        # Create GUI elements
        self.color_buttons = []
        for color in ["R", "G", "B", "Y", "O", "P"]:
            button = tk.Button(master, text=color, width=5, height=2, command=lambda c=color: self.make_guess(c))
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
        self.board_text = tk.Text(self.board_frame, width=30, height=10)
        self.board_text.pack()

    def make_guess(self, color):
        current_guess = self.guess_entry.get()
        current_guess += color
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
            messagebox.showinfo("Congratulations!", f"You guessed the code in {self.game.attempts} attempts.")
            self.reset_game()
        else:
            # Append the guess and feedback to the board
            self.board_text.insert(tk.END, f"Guess: {guess} - Feedback: {feedback_str}\n")
            self.game.attempts += 1  # Increment attempts
            self.board_text.see(tk.END)  # Automatically scroll to the bottom

    def reset_game(self):
        self.game = MastermindGame()
        self.board_text.delete(1.0, tk.END)  # Clear the board


if __name__ == "__main__":
    root = tk.Tk()
    game = MastermindGUI(root)
    root.mainloop()
