from random import choice

#Step 1

word_list = ['ketchup', 'chocolate', 'camel']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make
# guess lowercase.
guess = input('Guess a letter: ').lower()
while(len(guess) is not 1):
    guess = input('Should be only 1 letter, guess again: ').lower()

#TODO-3 - check if the letter the user guessed (guess) is on of the letters in the chosen_word.
if guess in chosen_word:
    print(f'{guess} was found')
else:
    print(f'{guess} was not found')
