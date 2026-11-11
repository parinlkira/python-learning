# different ways to create lists in Python

l = []  # empty list

l1 = [1,1,2,2,3,3]  # always use square brackets to create a list

l2 = list((3,5,7,9)) # using the list() constructor with a tuple
l3 = list('abcde')

print(l)
print(l1)
print(l2)
print(l3)   

print(l1[2])  # accessing the third element of the list (index starts from 0)
print(l1[-1])  # accessing the last element of the list using negative indexing

# list traversal 

for x in l3:
    print(x)

l4 = [7, 3.2, 'John', True, 5+6j] # list is heterogeneous, 
# can contain different data types

l1[2] = 15
l1.append(20)  # adding an element to the end of the list
l1.remove(3)  # removing the first occurrence of 3 from the list

print(l1[:])
print(l1[::-1]) 

l1 = [1, 2, 3, 4, 5]  # reassigning l1 to a new list
l1[3] = [10,11]

print(l1)  # printing the modified list with a nested list at index 3

# inserting values using slicing

l1 = [1, 2, 3, 4, 5]  # reassigning l1 to a new list again
l1[0:0] = [10]  # inserting 10 at the beginning of the list
# you have to assign it using a [] and it moves the elements and not replace
l1[2:2] = [99]  # inserting 99 at index 2
print(l1)

l1[9:9] = [77]  # inserting 77 at index 9 (end of the list)
# after end which last element+1 index, even you give any index
# it appends it at the end of the list

l1[3:3] = [10,11,12] # since only start and stop is mentioned, 
#any number of elements can be inserted at that position
# but if start, stop and end are inserted, then you have to enter 
# the exact number of element in between start and stop indices
print(l1)

# interesting outputs and cases of the above 

l1 = [1, 2, 3, 4, 5]
l1[1:4] = [10]  # replacing elements from index 1 to 3 with a single element 10
print(l1)       

l1 = [1, 2, 3, 4, 5]
l1[1:4] = [10, 11]  # replacing elements from index 1 to 3 with two elements
print(l1)

l1 = [1, 2, 3, 4, 5]    
l1[1:4] = [10, 11, 12, 13, 14]  # replacing elements from index 1 to 3 with four elements
print(l1)

# including the step also now
l = [1, 2, 3, 4, 5]
l[::2] = [10,11,12]
print(l)

l = [1, 2, 3, 4, 5]
l[::-1] = [10,11,12,13,14] # replacing the entire list in reverse order with new elements
print(l)

l[3:0:-1] = [10,11,12]  # replacing elements from index 3 to 1 in reverse order 
print(l)