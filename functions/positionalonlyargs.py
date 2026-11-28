# if a function has positional-only arguments, 
# they must be specified before the / symbol in the function definition
# / at beginning is not allowed for positional-only arguments

def fun(a, b, /, c, d):
    print(a, b, c, d)

fun(1, 2, c=3, d=4)
fun(1, 2, 3, 4)
# fun(a=1, b=2, c=3, d=4)  # This will raise a TypeError because a and b are positional-only

# placing / at the end means positional only arguments follow it
def fun(a, b, /):
    print(a, b)

fun(1, 2)
# fun(a=1, b=2)  # This will raise a TypeError because a and b are positional-only