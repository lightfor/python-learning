def compare_num(num1, num2):
    if num1 > num2:
        return str(num1)+">"+str(num2)
    elif num1 == num2:
        return str(num1)+"="+str(num2)
    elif num1 < num2:
        return str(num1)+"<"+str(num2)
    else:
        return ""


number1 = 2
number2 = 1
print(compare_num(number1, number2))
number1 = 2
number2 = 2
print(compare_num(number1, number2))
number1 = 1
number2 = 2
print(compare_num(number1, number2))