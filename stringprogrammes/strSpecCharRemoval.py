#Given a string containing mixed characters, 
# Construct a new string that includes only alphabetic characters and spaces. 
# Replace every other character (punctuation, symbols, digits) with a space.

scan = 'These+notes#reveal9Newton seeking-out an{underlying structure to/the\pyramid}'
clean = ''

for ch in scan:
    if ch.isalpha() or ch.isspace():
        clean = clean + ch
    else:
        clean = clean + ' '
        
print(clean)
                                  