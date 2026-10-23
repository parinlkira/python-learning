# match case in python is same as switch case in java

dayno = int(input('Enter the day no:'))

match dayno:
    case 0:
        print('Monday')
    case 1:
        print('Tuesday')
    case 2:
        print('Wednesday')
    case 3:
        print('Thursday')
    case 4:
        print('Friday')
    case 5:
        print('Saturday')
    case 6:
        print('Sunday')
    case _:
        print('Invalid Day Number') # is the default version of python 