from brain_games import logic


def check_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def brain_prime():
    logic.welcome()
    user_name = logic.get_user_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')
    attempts = logic.ATTEMPTS
    while attempts > 0:
        num = logic.get_random_number()
        if check_prime_number(num) is False:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
        print(f'Question: {num}')
        user_answer = logic.get_user_answer()
        logic.run(user_answer, correct_answer, user_name)
        attempts -= 1
    logic.win_message(user_name)
