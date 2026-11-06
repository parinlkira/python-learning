item = 'Memory Card'
size = 32
price = 11.75

# Now using print function and C style formatting
# Wanted String is 'Cost of 32GB Memory is $11.75'

print('Cost of %dGB %s is $%.2f' %(size, item, price))

data = 2000 
print( '%d' %(data))
print('%i' %(data))
print('%o' %(data))  # Octal representation
print('%x' %(data))  # Hexadecimal representation

print('start %10d end' %(data))

name = 'Raj'
roll = 10
avg = 85.5

# Using python's own formatted printing
# here print({} means placeholders for the values to be inserted)
# print({index:width.precision}) is the way

print('{0}----{1}----{2}'.format(name,roll, avg))

print('{}GB {} is ${}'.format(size, item, price))

print('start {0:15} end'.format(data))

print('start {:15} end'.format(data))
print('start {:<15} end'.format(data))  # Left aligned within 15 spaces
print('start {:>15} end'.format(data))  # Right aligned within 15 spaces
print('start {:^15} end'.format(data))  # Center aligned within 15 spaces
print('start {:*^15} end'.format(data))  # Center aligned within 15 spaces with '*' as fill character
print('start {0:+15} end'.format(data))  # Show sign and align within 15 spaces 
print('start {0:-15} end'.format(data))  # Show sign for negative numbers and align within 15 spaces 
print('start {0:15b} end'.format(data))  # Binary representation within 15 spaces
print('start {0:15o} end'.format(data))  # Octal representation within 15 spaces
print('start {0:15x} end'.format(data))  # Hexadecimal representation within 15 spaces
print('start {0:15,} end'.format(data))  # Number with comma as thousand separator within 15 spaces

data = 125.764363

print('start {0:^15e} end'.format(data))
print('start {0:15.2f} end'.format(data))  # Fixed-point representation with 2 decimal places within 15 spaces
print('start {0:15.4f} end'.format(data))  # Fixed-point representation with 4 decimal places within 15 spaces

# An easier way to format the entire string in python

print(f' Cost of {size}GB {item:^10} is ${price}')