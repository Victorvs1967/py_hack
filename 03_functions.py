import os


def check_symbols(restricted_symbols, s):

    for symb in restricted_symbols:
        if symb in s:
            return True
        return False


username = '$#ghj@'
email = '$g#hj%jhkjh'

if check_symbols(restricted_symbols=['@', '$#', '$'], s=username):
    print('username has restricted symbols')

if check_symbols(restricted_symbols=['#', '$', '%'], s=email):
    print('username has restricted symbols')


print(os.name)

# if '#$#' in username:
#     print('username has restricted symbols')
# if '$#' in username:
#     print('username has restricted symbols')
# if '@' in username:
#     print('username has restricted symbols')
#
# if '#' in email:
#     print('username has restricted symbols')
# if '$#' in email:
#     print('username has restricted symbols')
# if '%' in email:
#     print('username has restricted symbols')
#
