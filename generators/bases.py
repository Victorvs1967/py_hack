from string import digits, ascii_letters


states = {
    # states_key: 0
}
symbols = digits + ascii_letters


def get_next_str(state_key):

    if state_key not in states:
        states[state_key] = 0

    password_index = states[state_key]
    password = ''

    index = password_index
    while index > 0:
        rest = index % len(symbols)
        index = index // len(symbols)
        password += symbols[rest]

    states[state_key] += 1
    return password


if __name__ == '__main__':

    for step in range(len(symbols)):
        print(get_next_str('1'))
        print(get_next_str('2'))
