for i in range(-1, 2):
    print(i)
# error, outside loop
# break
for i in range(-1, 3):
    if i == 0:
        continue
    if i == 2:
        break
    print(i)
