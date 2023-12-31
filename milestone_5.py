
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
        """
        This function checks if the user-defined guess (a letter) is in the word then responds accordingly

        If the letter is in the word, then it will print the location of the letter that appears in the word and 
        reduces number of letters to be guessed remaining accordingly. 
        However, if the letter is incorrectly guessed then the number of lives is reduced for every incorrect guess.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index,letter in enumerate(self.word): # C A T
                if guess == letter:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
            print(f'{self.word_guessed} and {self.num_letters} more letters to guess!')
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        """
        This function asks the user to guess a letter of the hidden word

        The purpose of this function is to ensure the user chooses appropriate characters. It uses if statements
        to check that their inputs is from the alphabet and is singular. It also ensures the user doesn't select 
        a previously chosen letter and lose a life for it.
        """
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input('Guess a letter: ')
            if (not guess.isalpha()) or len(guess) != 1:
               print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
               print('You already tried that letter!') 
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
           
    
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost')
            break
        elif  game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


word_list = ['doggo','elephant']
play = play_game(word_list)

