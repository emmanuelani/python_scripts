from collections import Counter

# tuple unpacking
tuple = 'Emma', 21, 'UNEC', 'Lagos'
name, *age, school = tuple
print(age)
print(name)
print(school)


emma = 'abradacabra'
counter = Counter(emma)
print(counter.values())

def add10(x):
     return x + 10

print(add10(4))
add10 = lambda x: x + 10
print(add10(4))

c = [x*2 for x in range(1,6)]
print(c)

d = [x for x in range(1,9) if x%2==0]
e = filter(lambda x: x%2==0, range(1,9))
print(list(e))
print(d)
x= -6

class SoftwareEngineer:
    classattr = 'Programming'
    def __init__(self, name, age, level):
        self.name = name

def spell(txt):
    #your code goes here
    if len(txt) == 1:
        return txt
    else:
        return spell(txt[1:]) + txt[0]

txt = input()
txt2 = spell(txt)
print(txt2)

var = "nosrep doog a si leunammE"
print(var[::-1])

try:
    print(2/0)
    raise ZeroDivisionError('cannot divide bty zero')
except:
    print('Cannot be divided by zero')
finally:
    print('try another number greater than zero')


tuple1 = 1, 3, 4, 5, 7, 8, 3, 6
first_num, *other_nums, last_num = tuple1
print(first_num)
print(other_nums)
print(last_num)

def countdown():
    i = 10
    if i > 0:
        return i
        i -= 1
        for i in countdown():
            print(i)

countdown()

#python generators
y = map(lambda i: i**2, range(1,11))

print(next(y))
print(next(y))
print(next(y))
print(next(y))

print('for loop starts')
for i in y:
     print(i)

while True:
    try:
        value = y.__next__()
        print(value)
    except StopIteration:
        print('Done')
        break

print(next(iter(x)))
print('for loop starts')
for i in x:
    print(i)

# generator
def gen(a, b):
    for i in range(a, b):
        yield i

x = gen(1, 7)
print(next(x))
print(next(x))
print(next(x)) 


for i in gen(1,7):
    print(i)

def csv_reader(filename):
    for row in open(filename):
        yield row

print(next(csv_reader('titanic.csv')))
print(next(csv_reader('titanic.csv')))
print(next(csv_reader('titanic.csv')))
print(next(csv_reader('titanic.csv')))


# guess the password
import random as rd

r = rd.randrange(1,6)
print(r)

while True: # this means that the code following it should be repeated infinitely until explicitly quit
    Password = input('Enter password: ')
    if Password == 'emma':
        print('Password correct!')
        break
    else:
        print('Wrong password, try again')

        
    
# while true loops are infinite loops
x = 0
while True:
    print(x)
    x +=1
    if x == 1473:
        print('Done')
        break #break only executes when nested in a 'for' or 'While' loop

def glob():
    while True: 
        global x
        x = 4
        if x == 6:
            print('Got it')
            break
        else:
          x +=1
        

i = 0
while i < 5:
    print(i, end = " ")
    i += 1
    
   
    


