# Defining the Function to calculate the volume of a rectangular prism (cuboid)
def volume (l, b, h):
    vol = l * b * h
    return vol

# calling the function below its called as positional arguments (the order of arguments matters)
v = volume(2, 4, 6)
print(v)

# one more way to call the function using the __main__ block

if __name__ == "__main__":
    v = volume(1, 2, 3)
    print(v)

# calling the function using keyword arguments (the order of arguments does not matter)
v = volume(l = 2, b = 4, h = 6)
print(v)

v = volume(h = 6, b = 4, l = 2) # calling the function using keyword arguments in a different order
print(v)

# calling the function using a mix of positional and keyword arguments
v = volume(2, b = 3, h = 5)
print(v)

v = volume(2, 3, h = 4) # calling the function using a mix of positional and keyword arguments
print(v)