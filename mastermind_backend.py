import random

class MastermindGame:
    """
    The MastermindGame class represents the back-end logic of the Mastermind game.
    It handles code generation, checking guesses, and providing feedback.
    """

    def __init__(self):
        self.secret_code = self.generate_secret_code()
        self.attempts = 0

    def generate_secret_code(self):
        """
        Generate a random secret code of 4 colors.
        """
        colors = ["R", "G", "B", "Y", "O", "P"]
        return [random.choice(colors) for _ in range(4)]

    def check_guess(self, guess):
        """
        Check the player's guess and provide feedback.

        Args:
            guess (str): The player's guess.

        Returns:
            list: A list of feedback (e.g., ["R", "W", "W", " "]) for the guess.
        """
        feedback = []
        for i in range(4):
            if guess[i] == self.secret_code[i]:
                feedback.append("R")  # Correct color and position
            elif guess[i] in self.secret_code:
                feedback.append("W")  # Correct color, wrong position
            else:
                feedback.append(" ")  # No match
        self.attempts += 1
        return feedback

    def is_game_over(self, guess):
        """
        Check if the game is over (i.e., the player guessed the code correctly).

        Args:
            guess (str): The player's guess.

        Returns:
            bool: True if the player guessed the code, False otherwise.
        """
        return guess == self.secret_code

    def get_secret_code(self):
        """
        Get the secret code (for testing or display).

        Returns:
            list: The secret code.
        """
        return self.secret_code
