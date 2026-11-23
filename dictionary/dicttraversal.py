# simplest is for loop
a = {1: 'one',
     2: 'two',
     3: 'three'
}

for i in a:
    print(i, a[i])

# keys() method
print(a.keys())

for x in a.keys():
    print(x)

# values() method
print(a.values())

for x in a.values():
    print(x)

# items() method 
print(a.items())

for x, y in a.items():
    print(x, y)

# using get() method which has signature get(key, default=None)
a.get(2)
print(a.get(2))

a.get(5) # Not found, returns None, but if you use a[5] it will raise a KeyError
print(a.get(5))

a.get(5, 'Missing')
print(a.get(5, 'Missing'))

# setdefault() method which has signature setdefault(key, default=None)
# but it is different from get because it will insert the key with 
# the default value if the key is not found whereas get() will not modify 
# the dictionary

a.setdefault(3)
print(a)

a.setdefault(5, 'five')
print(a)

a.setdefault(6)
print(a)