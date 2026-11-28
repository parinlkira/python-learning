
def max3(a, b, c, /):
    if a > c and a > b:
        return a
    elif b > c:
        return b
    else:
        return c

print(max3(3, 7, 5))

# write the simple interest function using keyword-only arguments
def simple_interest(*, p, r, t):
    return (p * r * t) / 100

si = simple_interest(p=10000, r = 10, t = 1)

print(si)