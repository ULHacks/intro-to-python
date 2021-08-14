# Example of a syntax error
"""
print "python2 feature"
"""

# Examples of runtime errors (NameError, TypeError, ValueError, IndexError)
"""
print(a)
print("2"+2)
a = int(input())

a = [1, 2, 3, 4, 5]
print(a[-6])
"""

# Catching an IndexError example
while True:
    try:
        age = int(input())
        break
    except ValueError:
        print("please enter a valid age")
