print("Enter number of menu items: ")
num_items = int(input())

for i in range(1, num_items + 1):
    print("Enter menu item", i, ": ")
    item = input()
    print('Enter price of', item, ':')
    price = input('')

    dash = 20 - len(item) - len(price)
    print(item + ('-'*dash) + price)



