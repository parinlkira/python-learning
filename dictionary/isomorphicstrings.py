
str1, str2 = 'paper123', 'title222'

#defining a flag variable to keep state
flag = True

# checking length equality of strings
if len(str1) != len(str2):
    flag = False

# creating two maps for the ismorphic check and looping
else:
    map1, map2 = {}, {}

    for c1, c2 in zip(str1, str2):
        if c1 in map1:
            if map1[c1] != c2:
                flag = False
        else:
            map1[c1] = c2

        if c2 in map2:
            if map2[c2] != c1:
                flag = False
        else:
            map2[c2] = c1

if flag:
    print('Isomorphic')
else:
    print('Non Isomorphic')

