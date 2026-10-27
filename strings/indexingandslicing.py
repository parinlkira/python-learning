# [] brackets operator known as subscript operator is used in string to get index
# strings are also immutable in python like Java, so s[0] = 'new value' won't work

#slicing uses the same operator [] and same signature like range() function
# s1[start:stop:step] just ':' instead of the ',' in range

#single value is just like s1[start]
s = 'Hello World'

print(s[6])

# two values define s[start:stop] but stop in non-inclusive just like range
print(s[3:7])

# no defining start is like default 0 start till num and only : is entire string
print(s[:7])
print(s[:])
print(s[-5:]) # counts rev position from start and gives entire string

# But reverse negative index traversal is not allowed like s[-5:-9]
# only forward direction

print(s[-5:-2])

#using the step now
print(s[0:len(s):1])
print(s[0:11:2])

#skipping values between colons
print(s[0: :2])
print(s[::3])
print(s[::]) #prints entire string

#reversing a string and storing it in a new string sinc immutable

s2 = s[ : : -1 ]
print(s2)
print(s[-3::-1])
print(s[-3:-9:-1]) 

print(s[8:2:-1]) #stops at 3 and not 2 since range of stop noninclusive