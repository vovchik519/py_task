num_rows = int(input("Введите количество рядов: "))
num_stars = int(input("Введите количество сидений в ряду: "))
spacing = int(input("Введите отступ между рядами: "))

for i in range(num_rows):
    row = "*" * num_stars
    print(row)

    for j in range(spacing):
        print(" " * num_stars)