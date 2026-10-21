n = 4

if n >= 0:
    print('Positive number')
else:
    print('Negative number')

# checking compound statements 

a = 5
b = 7
c = 3

print( a > b and a > c)
print( a > b or a > c)
print( not a == 5)

# even or odd

if n%2 == 0 :
    print('Even number')
else:
    print('Odd')

# eligible to vote

if n >= 18:
    print('Eligible')
else: 
    print('Ineligible')

# Eligible for work

age = 65
if age >= 18 and age <= 60:
    print('Eligible for work')
else:
    print('Ineligible for work')

# gender m and M check

gender = 'M'

if (gender == 'm' or gender == 'M') :
    print('Gender',gender,'is for Male.' )
else:
    print('Gender ', gender, ' is for Female.')