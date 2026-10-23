#factors and divisors of a number
number = 15

for i in range(1, number+1):
    if number % i == 0:
        print('factor:', i)
    else:
        continue

#Prime number using the count method

n = 11; count = 0

for i in range(1, n+1):
    if n % i == 0:
        count+= 1;

if count == 2:
    print('Prime')
else:
    print('Not Prime')
