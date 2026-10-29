# isaplha() method checks if all characters in the string are alphabetic
s = 'Hello'
print(s.isalpha())

s = 'Hello123'
print(s.isalpha())

# islower() method checks if all characters in the string are lowercase
print(s.islower())

# isupper() method checks if all characters in the string are uppercase
print(s.isupper()) 
print('HELLO'.isupper())

# istitle() method checks if the string is in title case

s = 'Hello World' 
print(s.istitle())

# isspace() method checks if all characters in the string are whitespace
s = '   '
print(s.isspace())

s = ' '
print(s.isspace())

s = '\n\v\r\f' # Here \n is newline, \v is vertical tab,
               # \r is carriage return, \f is form feed which is all whitespace characters
print(s.isspace())

# isprintable() method checks if all characters in the string are printable
s = 'Hello World'
print(s.isprintable())

s = 'Hello\nWorld'
print(s.isprintable())  

# isidentifier() method checks if the string is a valid identifier

s = 'Hello'
print(s.isidentifier())

s = '123Hello'
print(s.isidentifier())

s = 'Hello_World'
print(s.isidentifier())

# isdigit() method checks if all characters in the string are digits

s = '123'
print(s.isdigit())

s = '7\u20823\u2075' 
print(s)
print(s.isdigit())


# isdecimal() method checks if all characters in the string are decimal characters

s = '123.45'
print(s.isdecimal())

s = '-123'
print(s.isdecimal())

# isnumeric() method checks if all characters in the string are numeric

s = '123.45'
print(s.isnumeric())

# isascii() method checks if all characters in the string are ASCII characters

s = 'Hello'
print(s.isascii())

s = 'Hello\u2082'
print(s.isascii())

# isalnum() 

s = 'Hello123'
print(s.isalnum())

s = 'Hello 123 '
print(s.isalnum())