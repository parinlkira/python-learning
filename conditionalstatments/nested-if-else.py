#temparature check

temp = 2

if temp == 25:
    print('Normal')
else: 
    if temp < 25:
        print('Cold')
    else: 
        print('Hot')

# same thing using elif, this is only in python 

if temp == 25:
    print('Normal')
elif temp < 25:
    print('Cold')
else:
    print('Hot')

# Generate discounted bill using if elif ladder

amount = 1500

if amount < 1000:
    amount = amount - amount*0.1
elif amount >= 1000 and amount <= 5000 : 
    amount = amount - amount*0.15
elif amount >= 5000 and amount < 10000:
    amount = amount - amount*0.20
else:
    amount = amount - amount*0.25

print('Discounted amount is:', amount)

# Leap Year Program as per gregorian calender and not julian - year % 4 == 0

year = 2012 

if year % 100 == 0:
    if year % 400 == 0 : 
        print('Leap Year')
    else:
        print("Not a Leap Year")
elif year % 4 == 0:
    print('Leap Year')
else:
    print('Not a Leap Year')