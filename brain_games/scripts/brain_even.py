#!/usr/bin/env python3
import prompt
from random import randint


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}!')
    return name


def brain_even(name):
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
    print(f'Congratulations, {name}!')


def main():
    welcome()
    brain_even(welcome_user())


if __name__ == '__main__':
    main()
