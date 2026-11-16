# way to create a list using comprehension is 
# [expression for item in iterable if condition]

l = [x for x in range(1,5)]
print(l)

l1 = [x**2 for x in range(1,5)]
print(l1)

l2 = [x.lower() for x in 'pYThoN ']
print(l2)

l3 = [int(x) for x in '12345']
print(l3)

l4 = [x for x in 'ab*7de'if x.isalpha()]
print(l4)

# nested list concepts

l = [[1,2], [3,4], [5,6]]

print('Accessing sublist:', l[0])
print('Accessing element in sublist:', l[0][1])
print('Accessing another element in sublist:', l[2 ][0])

# representing 2-D matrix in python using nested lists

l = [[1,2,3,4], [3,5,7,9], [2,4,6,8], [4,3,2,1]]
print(l)
print('Accessing element in 2-D matrix:', l[2][3])

# list can also be used to represent heterogeous tabular data 

l = [['Name', 'Age', 'City'], ['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles']]
print(l)
print('Accessing header row:', l[0])
print('Accessing first data row:', l[1])
print('Accessing specific element:', l[2][2])
print('Accessing all names:', [row[0] for row in l[1:]])
print('Accessing all ages:', [row[1] for row in l[1:]])
print('Accessing all cities:', [row[2] for row in l[1:]])
print('Accessing all data rows:', l[1:])

# using list comprehension splitting list data into odd and even

l = [1,2,3,4,5,6,7,8,9]

l1 = [x for x in l if x % 2 == 0]
print(l1)

l2 = [x for x in l if x% 2 != 0]
print(l2)

# find longest list in a nested list

lists = [[1,2,3], [1,1,1,1,1],[2,2,3,3]]

# you can use the max function for this
max_list = max(lists, key = len) # because just using max(lists) will calculate 
                # maximum sum of the sublists only

print('Longest list is:', max_list)