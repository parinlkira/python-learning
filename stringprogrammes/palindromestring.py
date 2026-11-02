# if string is a palindrome just print it, if not a palindrome then 
# make a string palindrome and print it

s = 'Race car'

s1 = s.replace(' ', '')
s2 = s1[::-1]
#print(s2)

if s1.casefold() == s2.casefold():
    print(s, end = '')
else:
    print(s1.casefold() + s2.casefold())