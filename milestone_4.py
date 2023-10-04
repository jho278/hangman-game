
import random

class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(self.word_guessed)
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index,letter in enumerate(self.word): # C A T
                if guess in letter:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
            print(f'{self.word_guessed} and {self.num_letters}')
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        print(self.word)
        while True:
            guess = input('Guess a letter: ')
            if (not guess.isalpha()) or len(guess) != 1:
               print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
               print('You already tried that letter!') 
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            
word_list = ['doggo','elephant']
num_lives = 5
play_game = Hangman(word_list,num_lives)
print(play_game.ask_for_input())

