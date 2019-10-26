import random
from string import digits, ascii_letters

s = digits + ascii_letters

r = random.choice(s)

print(s)
print(r)