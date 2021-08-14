# Ways to declare a list
li1 = list()
li2 = ["3", 1, 2, "3", "four"]

# Operations on a list (adding, deleting, popping, length, getting item at index)
li2.append(9)
print(li2)

li2.remove("3")
print(li2)

li2.pop(1)
print(li2)

print(len(li2), li2[2])

# Ways to declare a tuple
tp1 = tuple()
tp2 = (1, 2, 3, 4)

# Some list operations don't work on tuples
"""
tp2.append(9)
"""
print(len(tp2))

# Convering from lists to tuples and vice versa
li3 = list(tp2)
li3.append(9)
print(li3)
