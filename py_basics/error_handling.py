number1 = "20"
number2 = 20

try:
    total = number1 + number2

    print(total)
except TypeError:
    total = int(number1) + number2
    print(total)