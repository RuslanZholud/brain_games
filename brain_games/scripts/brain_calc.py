#!/usr/bin/env python3
import prompt
from random import randint, choice


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}!')
    return name


def brain_calc(name):
    print('What is the result of the expression?')
    n = 0
    while n < 3:
        random_num1 = randint(1, 100)
        random_num2 = randint(1, 10)
        expr = ['+', '-', '*']
        random_expr = choice(expr)
        if random_expr == '+':
            solution = random_num1 + random_num2
        elif random_expr == '-':
            solution = random_num1 - random_num2
        elif random_expr == '*':
            solution = random_num1 * random_num2
        print('Question: ', random_num1, random_expr, random_num2)
        answer = input('Your answer: ')
        if solution == int(answer):
            print('Correct!')
        else:
            print('"', answer, '"', ' is wrong answer ;(. Correct answer was', '"', solution, '"')
            print(f'Let`s try again, {name}!')
            quit()
        n += 1
    print(f'Congratulations, {name}!')


def main():
    welcome()
    brain_calc(welcome_user())


if __name__ == '__main__':
    main()
