#Bari's logic without using arrays and such

n = 8
a = 0; b = 1

for i in range(0, n):
    c = a + b
    a = b # this swapping or reassignment is what moves the pointers
    b = c # forward to generate the sequence

print(a) 