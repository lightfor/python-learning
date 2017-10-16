# caution, it's a string
fruit = ("apple")
print(fruit[0])
print(type(fruit))
fruit = ("apple",)
print(fruit[0])
print(type(fruit))
fruit = ("apple", "banana", "grape", "orange")
print(fruit[-1])
print(fruit[0:0])
print(fruit[1:3])
print(fruit[0:-2])  # -2 equals 2
print(fruit[2:-2])
# error, can't assign
# fruit[0] = "a"

