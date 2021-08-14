# Importing the math module
import math

# Using the `as` keyword with factorial
from math import factorial as f

print(f(5))

# Some variables (pi, e, tau)
print(math.pi, math.e, math.tau)

# Common functions (ceil, sqrt, log10, pow, gcd)
from math import ceil, sqrt, log10, pow, gcd

print(ceil(3/2))
print(sqrt(9))
print(log10(1000))
print(pow(2, 100))
print(pow(2, 9))
print(gcd(12, 15))
