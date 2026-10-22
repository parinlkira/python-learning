# Count number of digits
n = 2346
i = 0

while n > 0:
    i += 1
    n = n // 10
    
print('Number of Digits is:', i)

#sum of digits of a number 

n = 1346
sum = 0

while n > 0:
    rem = n % 10
    sum = sum + rem
    n = n // 10

print('Sum of digits:', sum)