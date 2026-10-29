# capitalize() method converts the first character
# of the string to uppercase and the rest to lowercase

s = 'hello world'
print(s.capitalize())

s = 'helLO World'
print(s.capitalize())

# upper() method converts all characters of the string to uppercase
print(s.upper())

# lower() method converts all characters of the string to lowercase
print(s.lower())

# title() method converts the first character of each word 
# to uppercase and the rest to lowercase
print(s.title())

# swapcase() method converts uppercase characters to lowercase and vice versa
print(s.swapcase())

# casefold() method converts the string to lowercase for caseless comparisons
print(s.casefold()) # use this method for string comparisons 
                    # works like equalsIgnoreCase() in Java


