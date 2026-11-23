# flip the dictionary keys:values to a new dicts where it becomes values:keys

original = {'a' : 1, 'b' : 2, 'c' : 1, 'd' : 2, 'e' : 3, 'f' : 2}

# creating empty dict
inverted = {}

# for looping dict
for key, value in original.items():
    if value not in inverted:
        inverted[value] = {key}
    else:
        inverted[value].add(key)

print('Inverted Dictionary is:', inverted)