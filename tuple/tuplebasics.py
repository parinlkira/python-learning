# This is a basic tuple example in Python
t1 = (1, 2, 3)
print(t1)

t2 = tuple([4,5,6])
t3 = ()
print(type(t3))

t4 = (3) # this is not a tuple, just an integer within parentheses
print(type(t4)) 

# for only one element tuple, a comma is required
t4 = (7,)
print(t4)

t5 = 10,11,12,12,14 # tuple without parentheses is also valid
print(t5)

t6 = tuple('python')
print(t6)
t7 = tuple(range(1,6))
print(t7)

# accessing elements of a tuple
print(t1[0])
print(t1[-1])

# slicing a tuple
print(t1[1:3])
print(t1[:2])
print(t1[::2])
print('Tuple in reverse:', t5[::-1])

for x in t1 :
    print(x)

# tuple comprehension general syntax - 
#  (*(expression for item in iterable if condition),)
# * is used to unpack the generator expression into the tuple

t = (*(x for x in range(5)),)
print(t)

t = tuple(x for x in range(1,5))
print(t)

# concat 
t = (1,3,4)
t2 = (5,6,7)
t = t + t2 
print(t)

# repetition
t = (1,2,3)
t = t * 2
print(t)

# packing and unpacking in two lines

t = 1, 2, 3  # packing
x, y, z = t  # unpacking
print(x, y, z)

t1 = 1, 2, 3, 4, 5
a, b, *c = t1
print(a, b, c)

*d, b, c = t1 
print(d, b, c)

# nested unpacking
t2 = (1, (2, 3), 4)
a, (b, c), d = t2
print(a, b, c, d)