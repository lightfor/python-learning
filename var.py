x = 1
print(id(x))
x = 1
print(id(x))
x = 2
print(id(x))

# error
# print y

# boxing
a = (1, 2, 3)
(x, y, z) = a
print(x, y, z)


def fun():
    local = 1
    print(local)


fun()
# error
# print(local)

_a = 1
_b = 2


def add():
    global _a
    _a = 3
    return "_a+_b=", _a+_b


def sub():
    global _b
    _b = 4
    return "_a-_b=", _a-_b


print(add())
print(sub())