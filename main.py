from random_word import RandomWords

class Wordle:
    """
    Contains the necessary functions and variables for the game wordle.
    """

    word, guess = "", ""
    number_of_guesses = 0

    def __init__(self):
        rw = RandomWords()
        self.word = rw.get_random_word(maxLength=5)
        self.number_of_guesses = 5

    def check_guess(self, guess):
        """
        Checks the users input if it equals or a character
        in the word that the user has entered is in the word
        that's to be guessed.
        """

        result = ""
        
        if len(guess) > 5: return "The word does not exceed 5 letters"
        else:
            if guess == self.word: 
                print(f"Correct! The word is {self.word}.")
                quit()

            else:
                for i, c in enumerate(guess[:]):
                    if c == self.word[i]: result += "✅"
                    elif c in self.word: result += "🟨"
                    else: result += "🛑"
                
                return result

    def run(self):
        """Starts the game."""

        print("You have 5 chances to guess the word I am thinking.")
        print("------------------")
        print("✅ - The letter is in the correct spot.")
        print("🟨 - The letter is in the wrong spot.")
        print("🛑 - The letter is not in the word.")
        print("------------------")

        while self.number_of_guesses != 0:
            # Ask user to guess the word
            self.guess = input("Guess: ")

            print(self.check_guess(self.guess))
            self.number_of_guesses -= 1

        print(f"The word was {self.word}.")

    

if "__main__" == __name__:
    wordle = Wordle()
    wordle.run()
