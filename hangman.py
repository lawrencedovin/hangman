from random import choice
from art import stages, logo
from words import word_list

lives = len(stages) - 1
chosen_word = choice(word_list)
print(logo)
display = ['_' for letter in chosen_word]

while ''.join(display) != chosen_word:
    output = ''.join(str(char) + ' ' for char in display)
    print(stages[lives])
    print(output)

    guess = input('\nGuess a letter: ').lower()
    while(len(guess) is not 1):
        guess = input('Should be only 1 letter, guess again: ').lower()
    
    while(guess in display):
        guess = input(f'You already guessed {guess}, guess again: ').lower()

    if guess not in chosen_word:
        print(f'{guess} was not found')
        lives -= 1
        if lives == 0:
            print(stages[lives])
            break
    else: 
        print(f'{guess} was found')

    for index in range(0, len(chosen_word)):
        display[index] = guess if guess == chosen_word[index] else display[index]
    
if ''.join(display) == chosen_word:
    print(f'Congrats you guessed {chosen_word} correctly and won the game!')
else:
    print(f'Game over, you lose. the word was {chosen_word}')

    
