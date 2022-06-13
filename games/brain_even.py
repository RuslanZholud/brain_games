from brain_games import logic


def get_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def brain_even():
    logic.welcome()
    user_name = logic.get_user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".\n')
    attempts = logic.ATTEMPTS
    while attempts > 0:
        question = logic.get_random_number()
        correct_answer = get_correct_answer(question)
        print(f'Question: {question}')
        user_answer = logic.get_user_answer()
        logic.run(user_answer, correct_answer, user_name)
        attempts -= 1
    logic.win_message(user_name)
