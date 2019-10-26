states = {
    # states_key: 0
}


with open('passwords.txt') as users_file:
    s = users_file.read()
    password = s.split('\n')


def get_next_str(state_key):

    if state_key not in states:
        states[state_key] = 0

    if states[state_key] >= len(password):
        return None

    login = password[states[state_key]]
    states[state_key] += 1

    return ''.join(login)


if __name__ == '__main__':

    for step in range(1000000):
        print(get_next_str('1'))
