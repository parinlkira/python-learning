a = 14 
b = 4

print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a // b) # This is floor division giving only quotient
print(a / b) # this is float division giving quotient with decimal points
print(a % b) # this is modulus operator giving remainder

print(2 **5) # this is exponentiation operator giving 2 raised to the power 5

# area of a circle
#importing math module for mathematical operations

import math
r = 4

area = math.pi * r ** 2

print('Area of the circle is: ', area)

# taking input from user

length = int(input('Enter the length: '))
# here you have to typecast length since input() function 
# returns a string by default
breadth = int(input('Enter the breadth:'))
area = length * breadth
print('Area of the rectangle is: ', area)

