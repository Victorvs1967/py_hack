
hacked_user = {}
attems = 3

def hack():
    # TODO check time

    step = 0
    password = ''

    while password != None:

        login = ''
        while login != None:
            try:
                if request(url, login, password):
                    print('Success: ', login, password)
                    hacked_user[login] = password
                break
            except:
                print('Error: 'login, password)

            login = get_next_login()

            step += 1
            if step % 100 == 0:
                print(login, password)

        password = get_next_password()
