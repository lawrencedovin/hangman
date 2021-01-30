from random import choice

#Step 1

word_list = ['ketchup', 'chocolate', 'camel']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make
# guess lowercase.
display = ['_' for letter in chosen_word]
print(display)
# guess = input('Guess a letter: ').lower()
# while(len(guess) is not 1):
#     guess = input('Should be only 1 letter, guess again: ').lower()

#TODO-3 - check if the letter the user guessed (guess) is on of the letters in the chosen_word.
while ''.join(display) != chosen_word:
    guess = input('Guess a letter: ').lower()
    while(len(guess) is not 1):
        guess = input('Should be only 1 letter, guess again: ').lower()

    for index in range(0, len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
        else:
            display[index] = display[index]
    print(display)
    print(''.join(display))
    
