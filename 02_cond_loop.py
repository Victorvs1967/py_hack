if (8 / 3) == 2:
    print('Ok 1')
elif 8 / 3 == 2.6666:
    print('Ok 2')
elif 8 / 3 == 2.66666666:
    print('Ok 3')
elif 8 / 3 == 2.66666666666666666666:
    print('Ok 4')
else:
    print('Not okey')

password = ''  # not known

if not password:
    true_password = '12345'
else:
    true_password = password

true_password = password if password else '12345'
print(true_password)

for i in range(1, 11):
    print(i * i)

lc = [i * i for i in range(1, 101) if i % 2 == 0]
print(lc)

i = 0
while len(str(i)) < 3:
    print(i)
    i += 1
