import prompt


def welcome_user():
    welcome_user.name = prompt.string('May I have your name?')
    print(f'Hello, {welcome_user.name}!')
