"""Вправа 10-6, 10-7"""

print("Введіть 'q' для виходу з програми")
while True:
    num1 = input("Введіть 1ше число:")
    if num1 == 'q':
        break
    num2 = input("Введіть 2ге число:")
    if num2 == 'q':
        break
    else:
        try:
            num1 = int(num1)
            num2 = int(num2)

        except ValueError:
            print("Потібно ввести цілі числа")
        else:
            sum = num1 + num2
            print(sum)
