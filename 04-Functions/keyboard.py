def input_string(message):
    user_input = input(message)
    return user_input(message)

def input_integer(message):
    user_input = int(input(message))
    return user_input

def input_real(message):
    user_input = float(input(message))
    return user_input

def input_boolean(message):
    user_input = input(message).capitalize
    if user_input == 'Y':
        return True
    elif user_input == 'N':
        return False