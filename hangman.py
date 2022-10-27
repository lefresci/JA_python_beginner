import random


def choosing_word():
    words_bank = ['python', 'java', 'swift', 'javascript']
    chosen_word = random.choice(words_bank)
    return chosen_word


def check_input(x):
    if len(x) != 1:
        return 'Please, input a single letter.'
    if x.isupper() or not x.isalpha():
        return 'Please, enter a lowercase letter from the English alphabet.'
    return 0


def win(x):
    print('You guessed the word', x + '!')
    print('You survived!')


def game():
    attempts = 8
    extra_letters = []
    answer = choosing_word()
    template = '-' * len(answer)

    while attempts > 0:

        print('\n' + template)
        letter = input('Input a letter: ')

        if check_input(letter):
            print(check_input(letter))
            continue

        if (letter in extra_letters) or (letter in template):
            print('You\'ve already guessed this letter.')
            continue

        if letter in answer:
            for letter_number in range(len(answer)):
                if answer[letter_number] == letter:
                    template = template[:letter_number] + letter + template[letter_number + 1:]
        else:
            print('That letter doesn\'t appear in the word.')
            attempts -= 1
            extra_letters += [letter]

        if answer == template:
            win(template)
            return 'victory'
    else:
        print('\nYou lost!')
        return 'lost'


def main():
    print('H A N G M A N')
    victories = 0
    losses = 0
    while True:
        user = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        user = user.lower()
        if user == 'play':
            if game() == 'victory':
                victories += 1
            else:
                losses += 1
        elif user == 'results':
            print('You won:', victories, 'times.')
            print('You lost:', losses, 'times.')
        elif user == 'exit':
            quit()
        else:
            continue


if __name__ == '__main__':
    main()
