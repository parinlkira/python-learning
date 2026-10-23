# first pattern 
'''
****
****
****
****
'''

for i in range(1, 5):
    for j in range(1,5):
        print('*', end='')
    print('')

# using single for loop and string repitition
s = '*'

for i in range(1, 6):
    print(s*5)


# second pattern 
'''
*
**
***
****
'''

for i in range(1, 5):
    for j in range(1,i+1):
        print('*', end='')
    print('')

#The way to solve it as per Bari's vids

for i in range(1,6):
    for j in range(1,6):
        if i >= j:
            print('*', end='')
    print('')

# using single for loop and string repitition
s = '*'

for i in range(1, 6):
    print(s*i)

# third pattern 
'''
****
***
**
*
'''

for i in range(1,5):
    for j in range(5,i,-1):
        print('*',end ='')
    print('')

#The way to solve it as per Bari's vids

for i in range(1,6):
    for j in range(1,6):
        if i<=j :
            print('*', end='')
    print('')


# Yet another logic for the same 

for i in range(1, 6):
    for j in range(1, 6 - (i - 1)):
        print('*', end='')
    print('')

# using single for loop and string repitition

for i in range(5, 0, -1):
    print('*' *i)

for i in range(1,6):
    print('*'*(6-i))

# fourth pattern 
'''
****
 ***
  **
   *
'''

for i in range(1, 6):
    for j in range(1, 6):
        if i > j :
            print(' ', end ='')
        else:
            print('*', end ='')
    print(' ')

# using single for loop and string repitition

for i in range(1,6):
    print(' ' *(i-1), end='')
    print('*' *(6-i))