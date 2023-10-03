# %% 
import random 

word_list = ['apple','orange','tomato','grapes','dragon fruit']
print(word_list)
# %%

# Create random word using choice method 
word = random.choice(word_list)
print(word)

# %%
def guess():
    user_input = input('Select first letter')
    if len(user_input) == 1 and user_input.isalpha():
        print('Good guess!')
        return user_input
    else:
        print('Not valid input')
        return user_input

guess = guess()
print(guess)

# %%
