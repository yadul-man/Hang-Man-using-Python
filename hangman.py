import random
import string
# The set of words are stored in file words.py. This is imported for random selection
from words import words

# Choose a random word without a space or '-' in it
def choose_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

# A random word is chosen by the program
# User enters a letter and it is searched for occurence in the word
# If found, the user continues guessing until the complete word is guessed
# Else the total no. of lives is decreased
def play():
    total_lives = 6

    # Choose a random word and create another string with the same length but with '-' as its characters
    word = choose_word()
    guess_word = '-' * len(word)
    temp = ""
    print(word)

    print("\nWord: " + f"{guess_word}")
    letter = input("Guess a letter (press - to exit): ")
    index = word.find(letter)

    # Correct guess
    if index != -1:
        print("\nCorrect guess.")
        # Update guessed word
        for i in range(len(word)):
            if word[i] == letter:
                temp += letter
            elif guess_word[i] != '-':
                temp += guess_word[i]
            else:
                temp += '-'
        guess_word = temp
    # Incorrect guess
    else:
        print("Incorrect guess.")
        total_lives -= 1
    
    print(f"Remaining lives: {total_lives}")

    print("\nWord: " + f"{guess_word}")
    letter = input("Guess a letter (press - to exit): ")
    # Loop guessing again until the complete word is guessed or all lives are lost
    while letter != '-':
        temp = ""

        if letter == '-':
            break
        else:
            index = word.find(letter)

            if index != -1:
                print("\nCorrect guess.")
                for i in range(len(word)):
                    if word[i] == letter:
                        temp += letter
                    elif guess_word[i] != '-':
                        temp += guess_word[i]
                    else:
                        temp += '-'
                guess_word = temp
            else:
                print("Incorrect guess.")
                total_lives -= 1
            
            if total_lives == 0:
                print("Game over.")
                break

            if word == guess_word:
                print("Word successfully guessed.")
                break

            if letter in guess_word:
                print("Letter already guessed. Try again.")
        
        print(f"Remaining lives: {total_lives}")

        print("\nWord: " + f"{guess_word}")
        letter = input("Guess a letter (press - to exit): ")

# Program starts here   
play()
