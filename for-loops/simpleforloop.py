for i in range(5):
    print(i)

#for a string the syntax is 
s1 = 'python' 

for x in s1:
    print(x)

# sum of n natural numbers 
n = 5; sum = 0
for i in range(1, n+1):
    sum = sum + i

print('Sum is:', sum)

#factorial using for loop
fact = 1; n = 5

for i in range(1, n+1):
    fact = fact*i

print('Factorial is:', fact)