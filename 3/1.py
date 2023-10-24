import random

def main_menu():
    print("Выберите игру:")
    print("1. Камень, ножницы, бумага")
    print("2. Угадай число")
    choice = input("Введите номер игры (1 или 2): ")
    if choice == "1":
        play_rock_paper_scissors()
    elif choice == "2":
        play_guess_the_number()
    else:
        print("Неправильный выбор. Попробуйте снова.")
        main_menu()

def play_rock_paper_scissors():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    choices = ["камень", "ножницы", "бумага"]
    user_choice = input("Выберите вашу ставку (камень, ножницы, бумага): ").lower()
    computer_choice = random.choice(choices)

    print(f"Ваш выбор: {user_choice}")
    print(f"Выбор компьютера: {computer_choice}")

    if user_choice in choices:
        if user_choice == computer_choice:
            print("Ничья!")
        elif (
            (user_choice == "камень" and computer_choice == "ножницы")
            or (user_choice == "ножницы" and computer_choice == "бумага")
            or (user_choice == "бумага" and computer_choice == "камень")
        ):
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")
    else:
        print("Неправильный выбор. Попробуйте снова.")
    
    play_again()

def play_guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = input("Угадайте число от 1 до 100: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Введите целое число.")
            continue

        attempts += 1

        if user_guess < number_to_guess:
            print("Загаданное число больше.")
        elif user_guess > number_to_guess:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток.")
            break
    
    play_again()

def play_again():
    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again == "да":
        main_menu()
    else:
        print("Спасибо за игру!")

if __name__ == "__main__":
    main_menu()