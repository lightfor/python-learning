import random


def compare_num(num1, num2):
    if num1 > num2:
        return 1
    elif num1 == num2:
        return 0
    else:
        return -1


number1 = random.randrange(1,9)
number2 = random.randrange(1,9)
print("num1=", number1)
print("num2=", number2)
print(compare_num(number1,number2))
