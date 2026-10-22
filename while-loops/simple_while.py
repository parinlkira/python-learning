# simple counter

n = 5
while n > 0:
    print(n)
    n = n - 1

# table of 3 

n = 3 
i = 0
while i < 10:
    i = i+1
    print(n,'X',i,'=',n*i)

# Display digits of a number from righthand side

n = 4365

while n > 0:
    remainder = n % 10
    print(remainder)
    n = n // 10

# sum of n numbers
n = 4
i = 0
sum = 0

while i < n : 
    i = i + 1
    sum = sum + i

print('sum is: ', sum)

# sum of n numbers taking input numbers from user
n = 5
i = 0
sum = 0
print('Enter', n, 'numbers')

while i < n :
    i += 1
    x = int(input(''))
    sum += x

print('Sum is:', sum)