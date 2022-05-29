import random as rd

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
numbers = "1234567890"
symbols = "!@#$%^&*\|?<>"

concat = lower + upper + numbers + symbols

length = 20

password = ''.join(rd.sample(concat, length))
print('your auto-generated password is: {}'.format(password))
with open() as g:
    file = readlines(g)
