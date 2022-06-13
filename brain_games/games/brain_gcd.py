from brain_games import logic
from math import gcd


def get_correct_answer(num1, num2):
    return str(gcd(num1, num2))


def brain_gcd():
    logic.welcome()
    user_name = logic.get_user_name()
    print('Find the greatest common divisor of given numbers.\n')
    attempts = logic.ATTEMPTS
    while attempts > 0:
        num1 = logic.get_random_number()
        num2 = logic.get_random_number()
        correct_answer = get_correct_answer(num1, num2)
        print(f'Question: {num1} {num2}')
        user_answer = logic.get_user_answer()
        logic.run(user_answer, correct_answer, user_name)
        attempts -= 1
    logic.welcome(user_name)
