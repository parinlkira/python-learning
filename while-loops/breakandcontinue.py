i = 0
# break statement example 
while True:
    i = i+1
    if i > 4:
        break;
    print(i)

#continue statement example

i = 0
while i < 7:
    i+=1
    if i % 3 == 0:
        continue
    print(i)