#range(start,stop,step) is needed for for loop, start and step optional
#default start = 0 and step = 1 and also, stop is excluded valuewise

print(list(range(5))) #typecasting range to list prints it since it gives
                      # a list of values
print(*range(1,5)) # * unpacks the list and simply gives values
print(range(3,8,2)) # simply printing range will not show the range of values

print(list(range(-5, -1)))
print(tuple(range(-5,3,2))) #tuple typecasting also works
print(*range(10,2,-2))

for i in range(0, 5):
    pass  # pass is used to do nothing in a loop. An empty loop basically