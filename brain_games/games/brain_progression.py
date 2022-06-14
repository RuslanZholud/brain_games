from brain_games import logic
from random import randint


def make_progression():
    progression_len = 10
    step = randint(1, 10)
    progression_first_num = randint(1, 10)
    hidden_element_index = randint(0, progression_len - 1)
    progression = ''
    correct_answer = ''
    counter = 0
    while counter < progression_len:
        next_in_progression = progression_first_num + counter * step
        if counter == hidden_element_index:
            correct_answer = str(next_in_progression)
            progression = f'{progression} ..'
            counter += 1
        else:
            progression = str(f'{progression} {next_in_progression}')
            counter += 1
    return progression, correct_answer


def brain_progression():
    logic.welcome()
    user_name = logic.get_user_name()
    print('What number is missing in the progression?\n')
    attempts = logic.ATTEMPTS
    while attempts > 0:
        progression, correct_answer = make_progression()
        print(f'Question:{progression}')
        user_answer = logic.get_user_answer()
        logic.run(user_answer, correct_answer, user_name)
        attempts -= 1
    logic.win_message(user_name)
