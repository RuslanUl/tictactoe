field = [[" "] * 3 for i in range(3)]
count = 0


def greting():
    print("Добро пожаловать\nв игру\nКРЕСТИКИ-НОЛИКИ\n---------------")
    print("Формат ввода:x y\nx - номер строки\ny - номер столбца")


def show_field():
    print("    0 | 1 | 2 |")
    print("-" * 15)
    for i in range(3):
        print(f"{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print("-" * 15)


def turn():
    while True:
        cords = input("Ваш ход!").split()
        if len(cords) != 2:
            print("Введите 2 координаты разделённые пробелом:")
            continue
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа:")
            continue
        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Клетка занята")
        else:
            print("Координаты вне диапозона")


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выйграл X!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выйграл O!")
            return True
    return False


greting()
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = turn()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break

    if count == 9:
        print("Ничья!")
        break
