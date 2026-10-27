
input_card = input('Enter 16-digit credit card number: ')

for i in range(len(input_card)):
    if input_card[i] == ' ':
        print(' ', end='')
    elif i < len(input_card) - 4:
        print('X', end='')
    else:
        print(input_card[i], end='')

print() 

# Bari's slicing method

last_digits = input_card[15:]
fours = 'X'*4 + ' '

masked_num = fours*3 + last_digits

print(masked_num)
