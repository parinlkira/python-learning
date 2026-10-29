# startswith(prefix, start, end)
# endswith(suffix, start, end)

s1 = 'python is very easy'

print(s1.startswith('python'))
print(s1.startswith('is', 7))

print(s1.endswith('easy'))

s1 = 'abc@gmail.com'

print(s1.endswith('gmail.com'))

# removeprefix(prefix) method helps to remove the specified prefix 
# from the string

s1 = 'python programming'
print(s1.removeprefix('py'))

# removesuffix(suffix) method helps to remove the specified suffix 
# from the string
 
print(s1.removesuffix('ing'))

# partition(sep) method splits the string at the first 
# occurrence of the specified separator, output is a tuple containing 
# the part before the separator, the separator itself, 
# and the part after the separator

s1 = 'python is easy'
print(s1.partition('is'))

# rpartition(sep) method splits the string at the last 
# occurrence of the specified separator

s1 = 'python is easy'
print(s1.rpartition('s'))