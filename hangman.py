from random import choice
from art import stages, logo

word_list = ['ketchup', 'chocolate', 'camel']
counter = 6
chosen_word = choice(word_list)
print(logo)
display = ['_' for letter in chosen_word]

while ''.join(display) != chosen_word:
    output = ''.join(str(char) + ' ' for char in display)
    print(stages[counter])
    print(output)

    guess = input('\nGuess a letter: ').lower()
    while(len(guess) is not 1):
        guess = input('Should be only 1 letter, guess again: ').lower()
    
    while(guess in display):
        guess = input(f'You already guessed {guess}, guess again: ').lower()

    if guess not in chosen_word:
        print(f'{guess} was not found')
        counter -= 1
        print(counter)
        if counter == 0:
            print(stages[counter])
            print('Game over, you lose')
            break
    else: 
        print(f'{guess} was found')

    for index in range(0, len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
        else:
            display[index] = display[index]
    output = ''.join(str(char) + ' ' for char in display)
    

if ''.join(display) == chosen_word:
    print(f'Congrats you guessed {chosen_word} correctly and won the game!')
    
