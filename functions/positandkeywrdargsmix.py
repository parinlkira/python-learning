# if a function has both positional-only and keyword-only arguments,
# positional-only arguments must be specified before the / symbol
# and keyword-only arguments must be specified after the * symbol in the function definition

def fun(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

fun(1, 2, c= 5, d= 6, e = 1, f = 3)

# fun(a=1, b=2, c=5, d=6, e=1, f=3)  # This will raise a TypeError because a and b are positional-only

# mix of positional-only and keyword-only arguments putting / before *

def fun(a, b, /, *, c, d):
    print(a, b, c, d)
    
fun(1, 2, c=3, d=4)
# fun(a=1, b=2, c=3, d=4)  # This will raise a TypeError because a and b are positional-only