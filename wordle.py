## I added a few "reacting sentences" to the attempts reponses.

import random

def display_word(word, correct_guesses):
    """Generate the current word display with guessed letters revealed."""
    display = ""
    for letter in word:
        if letter in correct_guesses:
            display += letter.upper()
        else:
            display += "_"  
    return display

def give_hint(word, guess):
    """Provide a hint based on the user's guess."""
    hint = ""
    for i, letter in enumerate(guess):  
        if letter in word:
            if i < len(word) and letter == word[i]:
                hint += letter.upper()  
            else:
                hint += letter.lower() 
        else:
            hint += "_"  
    return hint

def play_game():
    
    word_list = ["apple", "banana", "orange", "grape", "kiwi", "melon"]
    
    secret_word = random.choice(word_list)
    
    
    correct_guesses = []
    attempts = 0
    
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word.")
    
    while True:
        current_display = display_word(secret_word, correct_guesses)
        print(f"\nCurrent word: {current_display} | Attempts: {attempts}")
        
       
        guess = input("Enter your guess (letter or whole word): ").lower()
        
        if len(guess) == 1:  
            if guess in secret_word:
                print(f"Good guess! '{guess}' is in the word.")
                correct_guesses.append(guess)
            else:
                print(f"Sorry, '{guess}' is not in the word.")
        elif guess == secret_word:  
            print("Congratulations! You guessed the word correctly!")
            break
        else:
            print(f"Sorry, '{guess}' is not the correct word.")
        
        attempts += 1
        
        
        if all(letter in correct_guesses for letter in secret_word):
            print(f"Congratulations! You guessed the word: {secret_word.upper()}")
            break

    print(f"\nNumber of attempts: {attempts}")


play_game()
