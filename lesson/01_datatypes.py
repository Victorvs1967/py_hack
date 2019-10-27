a = 1 / 3
a = a + 2

print(a)

print(type(a))

print(a + a + a)

a = a + a + a
b = a + a + a

print(b)

b_true = True
b_false = False

if a == 7:
    print('Ok')
else:
    print('Not Ok')

n = None

s = '1234567890'
print(s)
print(type(s))

s = f'Value of {a=} '
print(s[:5])

list_of_something = [1, 2, 3, 4, 'abc', ['1', True]]

print(list_of_something)
print(list_of_something[0])
print(list_of_something[5][0])
print(list_of_something[:3])

dictionary = {
    'key': 'value',
    'Moscow': 'Capital',
    'l': list_of_something
}

print(dictionary)
print(dictionary['Moscow'])
print(dictionary['l'])
print(dictionary['l'][5][0])
