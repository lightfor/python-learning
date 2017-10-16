x = float(input("x:"))
i = 0
while x != 0:
    if x > 0:
        x -= 1
    else:
        x += 1
    i += 1
    print("%d times %d" %(i, x))
else:
    print("x equals 0", x)
