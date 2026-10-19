
# numeric base conversion functions

a = bin(10)
b = oct(10)
c = hex(10)

print(a, b, c)

type(a) #Remember output of bin() is of type 'str'

a = bin(15)
b = oct(15)
c = hex(15)

print(a, b, c)

s = bin(True)
print(s)

# type conversions below 

f = 16.59
b = True
s1 = '125'
s2 = '0b1010'
s3 = '0xA'

x = int(f)
y = int(b)
z1 = int(s1)
z2 = int(s2, 2)
z3 = int(s3, 16)

print(x, y, z1, z2, z3)
print(type(x), type(y), type(z1), type(z2), type(z3))

i = 12.75
b = False
s = '125.1'

x = float(i)
y = float(b)
z = float(s)

print(x, y, z)
print(type(x), type(y), type(z))

#bool type giving true for any value 

i1 = 10
i2 = -12
f = -1.2e-3
c = 3 + 4j
s = 'False'

x = bool(i1)
y = bool(i2)
z = bool(f)
w = bool(c)
v = bool(s)

print(x, y, z, w, v)
print(type(x), type(y), type(z), type(w), type(v))

# Only times/cases it gives false 

print(bool(False), bool(0), bool(0.0), bool(''), bool(None), bool())

# complex() type conversion

print(complex(10), complex(-12.75), complex(True), complex(False),
      complex(3, 4), complex(0, -1.2e-3), complex('3+4j'))

# str() type conversion

print(str(10), str(-12), str(-1.2e-3), str(True), str(False), str(None))

print(type(str(10)), type(str(-12)), type(str(-1.2e-3)), 
      type(str(True)), type(str(False)), type(str(None)))