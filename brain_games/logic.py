import prompt
from random import randint


ATTEMPTS = 3


def get_user_name():
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    return name


def get_user_answer():
    return str(prompt.string('Your answer: '))


def get_random_number():
    return randint(0, 100)


def logic(user_answer, correct_answer, user_name):
    attempts = ATTEMPTS
    if correct_answer == user_answer:
        print('Correct!\n')
        attempts -= 1
    else:
        print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let`s try again {user_name}!\n''')
    if attempts == 0:
        print(f'Congratulations, {user_name}!')
