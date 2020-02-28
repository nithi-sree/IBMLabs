# ax**2 + bx + c = 0
import cmath

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

#discriminant
d = (b**2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)

print("The Solution for {0}x^2 + {1}x + {2} is {3} and {4}".format(a, b, c, sol1, sol2))
