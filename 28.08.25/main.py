#getting input from the host(radius)
radius = input("Enter the Radius of the Cylinder:")
#getting input from the host(height)
height = input("Enter the height of the Cylinder:")
#Printing all the inputs to confirm
print("the cylinder dimensions are =", radius,height)

#new variables
r = int(radius)
h = int(height)
pi = 3.14

#volume
v = pi*r**2*h

print(v)

