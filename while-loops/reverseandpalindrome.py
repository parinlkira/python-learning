# reverse a number

n = 1257
rev = 0

while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

print('Reverse of the number is:', rev)

# check if number is a palindrome

n = 1221
rev = 0
m = n

while n > 0:
    r = n % 10
    rev = rev * 10 + r 
    n = n // 10

if rev == n:
    print('Number is a palindrome')
else:
    print('Number is not a palindrome')