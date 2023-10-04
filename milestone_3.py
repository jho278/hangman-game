
import random 

word_list = ['apple','orange','tomato','grapes','dragon fruit']
print(word_list)

# Create random word using choice method 
hidden_word = random.choice(word_list)
print(hidden_word)

def check_guess(guess):
    guess = guess.lower()
    if guess in hidden_word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    while True:
        guess = input('Guess a letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()