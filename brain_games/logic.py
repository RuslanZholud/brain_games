import prompt
from random import randint


ATTEMPTS = 3


def welcome():
    print('Welcome to the Brain Games!')


def get_user_name():
    name = prompt.string('May I have your name?\n')
    print(f'\nHello, {name}!')
    return name


def get_user_answer():
    return str(prompt.string('Your answer: '))


def get_random_number():
    return randint(0, 100)


def win_message(user_name):
    print(f'Congratulations, {user_name}!')


def run(user_answer, correct_answer, user_name):
    attempts = ATTEMPTS
    if correct_answer == user_answer:
        print('Correct!\n')
        attempts -= 1
    else:
        print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let`s try again {user_name}!\n''')
        quit()
