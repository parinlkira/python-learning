# how to convert decimals from dec to binary using format

a = 10
format(a, 'b')
print(format(a, 'b' ))

a = 25
print(format(a,'b'))
print(a.bit_length()) # bit_length() gives number of bits 

print(10 & 13) #Careful with & in python it does anding operation with digits
print(format(8,'b'))
print(10 | 13) # | is OR operation
print(format(15,'b'))

print(10 ^ 13)  # is XOR operation XOR - 0 if both bits same, else 1
print(~2)  # Complement operator

a = 10
print(a<<1) # left shift by 1, means number is doubled
print(a<<2) # left shift 2 times means a = 2 pow(2) * a

print(a>>1) # right shift by 1, means number is halved
print(a>>2)

# is and is not basically for memory allocated id pointing

x = 25 
y = 25

if y is x : 
    print('Pointing to same id in memory location')