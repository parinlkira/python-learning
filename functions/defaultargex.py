# Example of a function with default arguments in Python

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Example calls to the greet function
greet("Alice")
greet("Bob", "Hi")
greet("Charlie", "Good morning")    

# default argument is used when no value is provided for that parameter in the function call
# In the example above, "Hello" is the default value for the message parameter

# default arguments always are defined by providing a value in the function definition from 
# the rightmost parameters in the function definition.
def volume(l, w, h=1):
    vol = l * w * h
    return vol

# Example calls to the volume function
print(volume(2, 3))
print(volume(2, 3, 4))

def volume(l = 1, w = 1, h = 1):
    vol = l * w * h
    return vol

# Example calls to the volume function with default arguments
print(volume()) # Empty arguments, uses all default values
print(volume(2)) # Only the first argument is provided, others use default values
print(volume(2, 3))

# Default arguments with different datatypes also are allowed
def fun(a=1, b=2.5, c='hello'):
    print(a, b, c)

fun() # Uses all default values
fun(1, 3, 5) # Overrides all default values

# tuple and list also allowed as default arguments
# but gives warning if mutable default arguments are modified inside the function
def fun(a=1, b=(1,2,3), c = [4,5,6]):
    print(a, b, c)

fun() # Uses all default values
fun(2) # Overrides the first argument
fun(2, (4,5,6)) # Overrides the first two arguments
fun(2, 3, 5) # Overrides all arguments

# Note: Modifying mutable default arguments like lists inside the function 
# can lead to unexpected behavior in subsequent calls.

def fun(l = [1, 2, 3]):
    l.append(len(l))
    print(l)

fun() # Modifies the default list.Default is only created once in the first call
fun() # Shows the unexpected behavior due to mutable default argument
fun([10, 11])
fun() # Again modifies the 2nd call's list, showing the cumulative effect of previous calls   