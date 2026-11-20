# dictionary creation

d = {1:'one', 2:'two', 3:'three' }
print(d)

# accessing dictionary elements
print(d[1])
print(d.get(2)) 

# modifying elements
d[3] = 'tres'
print(d)

# adding/writing new elements to dictionary
d[4] = 'four'
print(d)

# removing elements from dictionary
del d[4]
print(d)

# traversal using for loop

for key in d:
    print(key) # this will just print the keys of the dictionary

for key in d:
    print(d[key]) # this will print the values of the dictionary

for key, value in d.items():
    print(key, value) # this will print both keys and values of the dictionary

for i in d:
    print(i, d[i]) # this will print both keys and values of 
    # the dictionary using the key to access the value

# dictionary heterogenuous data nature

d = {1:3.5 , 2.5:True, 5+3j : 'abc'}
print(d)

d = {1 : [1, 2, 3], 2:(4,5), 3:{8,9}, 4: {'a': 1, 'b': 2}}
print(d)

d = {(1,2):"hello"} # tuple is allowed as key but list, set and dict 
# is not allowed as key