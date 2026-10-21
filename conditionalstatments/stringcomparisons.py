# Important to note and understand the String Comparison rules as per 
# English Dictionary order

# Here s1 > s2 means that s1 comes after s2 in dictionary

print('apply' > 'apple') # Because y comes after e
print('cat' < 'catch') # Because length greater after cat
print('data' > 'Data') # Because Capital Letter have precedence before LowerCase
print('2nd' < 'Byte') # nums have lower precedence than char

# Order of precedence - nums < lowercase < uppercase

s1 = 'software'
s2 = 'Hardware'
 
print( s1 > s2)
print('python' < 'pycharm') # Because of t vs c comparison at 3rd char
print('integer' == 'integer')
print('printer' > 'print')

# Short Circuiting concept is interesting, basically no need to check 
# cond1 and/or cond2, then in case of and if 1st false, 2nd cond not checked
# and in case of or if 1st true 2nd cond not checked

# But what happens when you compare non-boolean such as 5 and 10? basically
# any number other than 0 = False is True = 1, 5, -7, -15 ....

print(5 and 10) # So in case true and true yields the last checked condition value
print(10 and 5)
print(5 and 0)

print(5 or 10)
print(0 or 10)

# Chaining Comparisons only python can do this and not Java and C 
# if a> b and b> c then can write as a>b>c

a = 10
b = 5
c = 3

if a > b > c  :
    print('True')

print('No Else required just like Java')

a = b = 5
c = 3
print(a == b > c)
