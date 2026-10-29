
s = 'Hello'
print(type(s))

# In python too like java you call methods by the '.' operator
s1 = s.upper()
print(s1)

#find method 
s= 'Hello How are you'

x = s.find('o')  # storing result of variable in x
print(x)

print(s.find('How'))

print(s.find('Something Not There')) # char or var not there then output is -1
 
print(s.find('o',5)) #find(substring, start, end)
print(s.find('o', 5, 7))

#rfind is similar to find but searches from the right
print(s.rfind('o'))
print(s.rfind('o', 0, 15))
print(s.rfind('kite'))

# index method is similar to find but raises ValueError 
# if substring is not found

print(s.index('o')) 
print(s.index('How'))

#rindex method is similar to rfind but raises ValueError if 
# substring is not found
print(s.rindex('o'))
print(s.rindex('o', 0, 15)) 

# count method returns the number of occurrences of a substring

print(s.count('o'))
print(s.count('How'))
print(s.count('Something Not There'))
