import numpy as np
a = np.array([[[2, 5, 6, 4],
             [3, 5, 6, 8]],
             [[5, 6, 7, 3],
             [8, 10, 11, 17]]])

b = np.array([[[4, 6, 9]]])

#arrays can't multiply each other unless they are of the shape, even if they are the same dimension
print(a.shape)
print(b.shape)
try:
    c = a*b
except:
    pass


a[0,0, 2] = 4
a[:, 0, :2] = 0
print(a[:, 0, :2])
print(a)

print(np.random.rand(2, 5))
print(np.random.randint(2, 67, size= (2, 3, 5)))

#identity matrix i.e the argument (usaully integer) passed will serve both as the number of rows and columns
print(np.identity((4), dtype='int'))
print(np.identity((3), dtype='int'))

#repeat an array
rb = np.repeat(a, 1, axis=0)
print(rb)

#initializing arrays
d = np.full((2,5,8), 7, dtype='int16')
e = np.full_like(a, 6)
print(d)
print(e)
test = np.full((5, 5,), 1)
test[1, 1:4] = 0
test[3, 1:4] = 0
test[2, 1:4] = 0
test[2, 2] = 9
print(test)

#This is a little test from the tutorial I watched
test1 = np.ones((5,5), dtype='int')
z = np.zeros((3,3))
z[1,1] = 9
test1[1:4, 1:4] = z
print(test1)

#copying arrays
a = np.array([[[1, 2, 3],
             [4, 5, 6]],
             [[7, 8, 9],
             [10, 11, 12]]])
b = a.copy()
try:
    b[2] = 122
except:
    pass
print(b)
print(a)

#mathematics
print(a+2)
print(a+b)
print(a/2)
print(a%2)
print(a-2)
print(a**b)
print(a*b)

print(a[::-1, ::-1])

#statistics
print(a.mean())
#or
print(np.mean(a))
# print(a.mode())
# print(a.median())
print(a.max())
#or
print(np.max(a, axis =1))
print(a.min())
#or
print(np.min(a, axis =1))
print(a.sum())
#or
print(np.sum(a , axis =1))

#reshaping arrays
a_reshaped = a.reshape((2, 3, 2))
print(a_reshaped)

#Stacking arrays
V1 =np.array([2, 5, 6])
V2 =np.array([4, 7, 9])
print(np.vstack((V1,V2)))
print(np.hstack((V1,V2)))

# txt = np.genfromtxt('Random_numbers.txt')

print(a>3)

file = open('Random_numbers.txt').read()
print(file)

ear#numpy arange fucntion: this is just like the regular python range function but here an ndarray instead of a list is created.
array = np.arange(0, 12, 2)
print(array)
