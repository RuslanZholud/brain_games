from brain_games import logic
import random


def get_correct_answer(num1, expr, num2):
    if expr == '+':
        return str(num1 + num2)
    elif expr == '-':
        return str(num1 - num2)
    elif expr == '*':
        return str(num1 * num2)


def brain_calc():
    logic.welcome()
    user_name = logic.get_user_name()
    print('What is the result of the expression?\n')
    attempts = logic.ATTEMPTS
    while attempts > 0:
        expr_list = ['+', '-', '*']
        expr = random.choice(expr_list)
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)
        correct_answer = get_correct_answer(num1, expr, num2)
        print(f'Question: {num1} {expr} {num2}')
        user_answer = logic.get_user_answer()
        logic.run(user_answer, correct_answer, user_name)
        attempts -= 1
    logic.win_message(user_name)


brain_calc()
