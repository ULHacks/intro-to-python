# Taking input
a = input()
print(a+a)

b = int(input())
print(b+b)

c = float(input())
print(c)

# Taking input with a prompt
age = int(input("What is your age: "))
print("In one year, you will be", age+1)

# More versatile printing with commas, `sep`, and `end`
print(8, 13, 2021, sep="/")

li = [1, 2, 3, 4, 5]

for i in li:
    print(i, end=" ")
