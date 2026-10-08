#Радышев А.И группа T118

import random
def show_rules():
    print("╔══════════════ИГРА 'МИШЕНЬ' ══════════════╗")
    print("║Мишень находится на позиции от 1 до 10.   ║")
    print("║У вас есть 4 выстрела.                    ║")
    print("║После промаха будет подсказка.            ║")
    print("║Попадание — победа, 4 промаха — поражение.║")
    print("╚══════════════════════════════════════════╝")
def read_choice():
    while True:
        choice = input("Ваш выбор: ")

        if choice == "1" or choice == "2":
            return int(choice)

        print("Введите 1 или 2.")
def read_shot():
    while True:
        try:
            shot = int(input("Введите позицию выстрела (1-10): "))

            if 1 <= shot <= 10:
                return shot

            print("Введите число от 1 до 10.")

        except ValueError:
            print("Введите целое число.")
def get_hint(shot, target):
    if target > shot:
        return "правее"
    elif target < shot:
        return "левее"
    else:
        return "попал"
def show_shots(left):
    print("Осталось выстрелов:", left)
def play_game():
    target = random.randint(1, 10)1

    shots = 4

    while shots > 0:
        show_shots(shots)

        shot = read_shot()
        result = get_hint(shot, target)

        if result == "попал":
            print("Попадание! Вы победили!")
            return

        print("Мимо! Мишень находится", result + ".")
        shots -= 1

    print("Вы проиграли!")
    print("Мишень была на позиции:", target)
def main():
    show_rules()
    print("\n1 - Начать игру")
    print("2 - Выйти из игры")
    choice = read_choice()
    if choice == 1:
        play_game()
    else:
        print("До свидания!")

main()
