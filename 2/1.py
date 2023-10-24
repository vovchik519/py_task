def find_star_position(s):
    for i, char in enumerate(s):
        if char == '*':
            return i
    return -1
    
input_string = input("Введите строку: ")

position = find_star_position(input_string)

if position != -1:
    print(f"Первая звездочка найдена на позиции {position}.")
else:
    print("Звездочка не найдена в строке.")