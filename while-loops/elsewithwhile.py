i = 0
# Can use else with if, while, for and try | only in python
while i < 5:
    i+= 1
    print(i)
else:
    print('Inside Else Block to denote successful completion of loop')

print("End of code")

#if break statement in between, else will not execute as unsuccessful 
#completion of loop so direct exit

i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print(i)
else:
    print('Inside else')

print('End of Code')