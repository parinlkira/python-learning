# if a function has keyword-only arguments, 
# they must be specified after the * symbol in the function definition
# * at end is not allowed for keyword-only arguments

def fun(a, b, *, c, d):
    print(a, b, c, d)

fun(1, 2, c=3, d=4)
# fun(1, 2, 3, 4)  # This will raise a TypeError because c and d are keyword-only 

# placing * in the beginning of the function definition means 
# keyword-only arguments follow it
def fun(*, a, b):
    print(a, b)

fun(a= 2, b = 4)
# fun(1, 2)  # This will raise a TypeError because a and b are keyword-only 