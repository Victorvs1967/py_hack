import requests


def request(url):

    r = requests.get(url)
    return r.text

def main():

    url = 'https://www.apple.com'
    for _ in range(1, 100):
        print(request(url))

if __name__ == '__main__':
    main()