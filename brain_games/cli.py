import prompt


def get_user_name():
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    return name
