# The most basic python function
def f():
    return 0

print(f())

# All python functions return a value
def f():
    print("hello, world")

print(f())

# Function example with parameters
def box(row, col):
    print("+" + "-"*row + "+")

    for i in range(col):
        print("|" + "."*row + "|")

    print("+" + "-"*row + "+")

box(2, 1)
box(6, 6)
box(6, 3)
box(4, 6)

# Printing `print`
print(print)
