n = 4 
print('Enter',n,'numbers')
i = 0; max = 0
while i < n:
    i = i+1
    x = int(input(''))
    if x > max:
        max = x

print('max:', max)

# Find min and max in the same program

n = [4,5,6,1,3,6] # This is the way to write a list in python
i = 0
length = len(n)  # len function to find size of list

max = float('-inf')  #This is how you write Integer.MIN_VALUE in python
min = float('inf') #This is how you write Integer.MAX_VALUE in python

while i < length : 
    
    x = n[i]
    i = i+1 
    if x > max:
        max = x
    if x < min:
        min = x

print('Max is :', max)
print('Min is :', min)