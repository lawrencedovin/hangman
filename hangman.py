from random import choice

word_list = ['ketchup', 'chocolate', 'camel']
counter = 7
chosen_word = choice(word_list)
print(chosen_word)

display = ['_' for letter in chosen_word]
print(display)

while ''.join(display) != chosen_word:
    guess = input('Guess a letter: ').lower()
    while(len(guess) is not 1):
        guess = input('Should be only 1 letter, guess again: ').lower()

    if guess not in chosen_word:
        print(f'{guess} was not found')
        counter -= 1
        print(counter)
        if counter == 0:
            print('game over')
            break

    for index in range(0, len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
        else:
            display[index] = display[index]
    print(display)
    print(''.join(display))
    
