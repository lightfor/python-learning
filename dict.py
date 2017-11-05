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
for x in result:
    print("%s=" %x, result[x])
print(result.items())
print(result.keys())
print(result.values())