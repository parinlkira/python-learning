# list concatenation

l = [1, 2, 3]
l2 = [4,5,6]
l3 = l + l2  # concatenating l and l2 to create l3
print(l3)  # printing the concatenated list

# list repetition
l4 = l * 3  # repeating the list l three times
print(l4)  # printing the repeated list

l + [4]  # concatenating l with a single-element list containing 4
print(l + [4])  # printing the result of the concatenation

l.extend([4,5,6]) # this extends the list l with the elements 4, 5, and 6
# and modifies the original list in place instead of creating a new list
print(l)  # printing the list after extending it with new elements

print(3 in l)  # checking if 3 is an element of the list l

nl1 = [[1,2], [3,4], 4, 5]
print(3 in nl1)  # checking if 3 is an element of the nested list nl1

l1 = [1,2,3]
l2 = [1,2,3,4]
l3 = [1,2,1]

print(l1 == l2)  # checking if l1 and l2 are equal
print(l1 != l3)  # checking if l1 and l3 are not equal  
print(l1 > l2)
print(l1 > l3)

# List traversal techniques

# 1. Simple for loop

for x in l : 
    print(x)  # printing each element of the list l

# 2. Using index-based for loop
for i in range(len(l)):
    print(i, l[i])  # printing each element of the list l using its index

# 3. Using while loop
i = 0 
while i < len(l):
    print(i, l[i])
    i += 1