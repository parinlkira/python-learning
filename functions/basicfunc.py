# Defining the Function to calculate the volume of a rectangular prism (cuboid)
def volume (l, b, h):
    vol = l * b * h
    return vol

# calling the function below
v = volume(2, 4, 6)
print(v)

# one more way to call the function using the __main__ block

if __name__ == "__main__":
    v = volume(1, 2, 3)
    print(v)
