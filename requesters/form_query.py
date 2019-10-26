import requests


def request(url, login, password):

    r = requests.post(url, data={'login': login, 'password': password})

    return r.status_code == 200





