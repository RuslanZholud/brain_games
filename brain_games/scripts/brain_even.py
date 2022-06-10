#!/usr/bin/env python3
import prompt
from random import randint


def welcome():
    print('''Welcome to the Brain Games!
Game: Is even number?''')


def welcome_user():
    welcome_user.name = prompt.string('May I have your name?\n')
    print(f'Hello, {welcome_user.name}!')


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while n < 3:
        random_num = randint(1, 100)
        print('Question: ', random_num)
        answer = input('Your answer: ')
        if random_num % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif random_num % 2 != 0 and answer == 'no':
            print('Correct!')
        elif random_num % 2 == 0 and answer != 'yes':
            print('"', answer, '"', ' is wrong answer ;(. Correct answer was "yes"')
            quit()
        elif random_num % 2 != 0 and answer != 'no':
            print('"', answer, '"', ' is wrong answer ;(. Correct answer was "no"')
            quit()
        n += 1
    print(f'Congratulations, {welcome_user.name}!')


def main():
    welcome()
    welcome_user()
    brain_even()


if __name__ == '__main__':
    main()
