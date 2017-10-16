# like switch
x = 1
y = 2
operator = "/"
result = {
    "+" : x+y,
    "-" : x-y,
    "/" : x/y,
    "*" : x*y
}
print(result.get(operator))