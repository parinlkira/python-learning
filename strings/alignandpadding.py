 #ljust(width[, fillchar])
 # Returns the string left-justified in a string of length width. Padding is done using the specified fill character (default is space).
 
s = 'Hello'

print(s.ljust(7,'*'))

#rjust(width[, fillchar])
# Returns the string right-justified in a string of length width. Padding is done using the specified fill character (default is space).

print(s.rjust(7))
print(s.rjust(7,'-'))

#center(width[, fillchar]) 
# Returns the string centered in a string of length width. Padding is done using the specified fill character (default is space).

print(s.center(8))
print(s.center(9,'-'))

#zfill(width)       
# Returns the numeric string left-filled with zeros to a string of length width.

print(s.zfill(7))

#lstrip([chars])
# Returns a copy of the string with leading characters removed.
# If chars is not specified, it defaults to removing whitespace.

s = '   Hello   '

print(s.lstrip())

s1 = '$$Hello'

print(s1.lstrip('$'))

#rstrip([chars])
# Returns a copy of the string with trailing characters removed.
# If chars is not specified, it defaults to removing whitespace.

s = 'Hello!!'

print(s.rstrip('!'))

#strip([chars])
# Returns a copy of the string with leading and trailing characters removed.
# If chars is not specified, it defaults to removing whitespace.

s = '11Hello11'

print(s.strip('1'))

#special string case

s = '#!Hello  $ *'

x = s.strip('#! $*')
print(x)