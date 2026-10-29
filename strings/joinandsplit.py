#replace(old, new, count) method replaces occurrences of 'old' with 'new' 
# in the string. The optional 'count' parameter specifies the 
# maximum number of replacements to make.

s = 'a-b-c-d-e'

s1 = s.replace('-', ',')
print(s1)

print(s.replace('-',',', 3))
print(s.replace('k','m')) # No 'k' in the string, so no replacement occurs

s = 'abcd@gmail.com'
print(s.replace('gmail', 'yahoo'))

# join(iterable) method concatenates the elements
# of an iterable (like a list or tuple) into a single string, 
# with the string it is called on as the separator.

s1 = 'abc'
s2 = 'xyz'
s3 = s1.join(s2)
print(s3)

s1 = '/'
s3 = s1.join(s2)
print(s3)

# split(separator, maxsplit) method splits the string into a list of substrings

s = 'John Smith Ajay'
print(s.split())

print(s.split('h'))

s = 'apple,banana,cherry'
print(s.split(','))
print(s.split(',', 1)) # Split only at the first comma

#rsplit(separator, maxsplit) method splits the string into a 
# list of substrings, starting from the right
s = 'apple,banana,cherry'
print(s.rsplit(',', 1)) # Split only at the last comma

print(s.rsplit(',', 2)) # Split at the last two commas

# Example with maxsplit greater than the number of separators
print(s.rsplit(',', 5)) # Split at all commas from the right    

# splitlines() method splits the string at line breaks and returns a list of lines

s ='First Line \n Second Line \n Third Line\n'

print(s.splitlines())
print(s.splitlines(True)) # Keep the line breaks which is '\n'


