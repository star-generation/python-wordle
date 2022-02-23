word, guess = "crane", ""

print(word)

print("You have 5 chances to guess the word I am thinking.")
print("-------")

def check_guess(guess):
    result = ""

    if len(guess) > 5: return "The word does not exceed 5 letters"
    else:
        if guess == word: 
            print(f"Correct! The word is {word}.")
            quit()

        else:
            for i, c in enumerate(guess[:]):
                if i < len(word):
                    if c == word[i]: result += "X"
                    else: result += "O"
            
            return result
                

def main():
    number_of_guesses = 5

    while number_of_guesses != 0:
        guess = input("Guess: ")
        print(check_guess(guess))
        number_of_guesses -= 1

    print(f"The word was {word}.")


if "__main__" == __name__:
    main()
