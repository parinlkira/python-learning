# variable naming conventions in python and playing with them

a,b,c = 1, 'hello', 3.14
print('Variables can hold different types of values: ', a,b,c)

# if variables hold same values
d, e, c = 1,1,1
print('Variables can hold the same values: ', d, e, c)

# in this case their memory locations are same using "id() function"

print('Memory locations: ', id(d), id(e), id(c))

# Note: In Python, small integers and some strings are cached, 
# so variables with the same value may share the same memory location.

# Also naming variable False is not allowed since keyword, 
# but false is allowed since "false" is not a keyword like java


false = 10;
_a = 'valid'
_a_ = 'also valid'
__b__ = 'also valid'

print('Variable false: ', false)
print('Variable _a: ', _a)
print('Variable _a_: ', _a_)
print('Variable __b__: ', __b__)
