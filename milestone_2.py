# %% 
import random 

word_list = ['apple','orange','tomato','grapes','dragon fruit']
print(word_list)
# %%

# Create random word using choice method 
word = random.choice(word_list)
print(word)

# %%

user_input = input('Select first letter')
if len(user_input) == 1 and user_input.isalpha():
    print('Good guess!')
else:
    print('Not valid input')

print(user_input)

# %%
