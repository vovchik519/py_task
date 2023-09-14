num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

last_two_digits_num1 = num1 % 100
last_two_digits_num2 = num2 % 100

result = last_two_digits_num1 + last_two_digits_num2

print(f"Сумма двух последних цифр: {result}")