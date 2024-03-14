import random

def choose_word():
    words = ["hangman", "python", "programming", "challenge", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    max_attempts = 6
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_attempts = 0

    print("Welcome to Hangman!")
    
    while incorrect_attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nWord: " + current_display)
        
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                incorrect_attempts += 1
                print("Incorrect guess. Attempts left: {}".format(max_attempts - incorrect_attempts))
        else:
            print("Invalid input. Please enter a single letter.")

        if set(guessed_letters) == set(word_to_guess):
            print("\nCongratulations! You guessed the word: '{}'".format(word_to_guess))
            break

    if incorrect_attempts == max_attempts:
        print("\nSorry, you ran out of attempts. The word was: '{}'".format(word_to_guess))

if __name__ == "__main__":
    hangman()