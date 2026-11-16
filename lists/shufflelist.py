# random module 

import random as rd

print(rd.random())  # prints a random float between 0.0 and 1.0
print(rd.randint(1,100))  # prints a random integer between 1 and 100 inclusive
print(rd.randrange(1,10,2))

for i in range(5):
    print(rd.randint(1,100))

rd.seed(10) # gives the same random numbers each time

for i in range(5):
    print('Random numbs using seed',rd.randint(1,100))

l = [1,2,3,4,5]
print('Random choice from list:', rd.choice(l))    # prints a random element from the list

rd.shuffle(l) # shuffles the list in place
print('Shuffled list:', l) 