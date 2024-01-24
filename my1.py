# Функция, определяющая цвет поля
def is_same_color(k, l, m, n):
    return (k + l) % 2 == (m + n) % 2


# Функция, определяющая, угрожает ли фигура полю
def threatens(k, l, m, n, figure):
    if figure == 'ферзь':
        return k == m or l == n or abs(k - m) == abs(l - n)
    elif figure == 'ладья':
        return k == m or l == n
    elif figure == 'слон':
        return abs(k - m) == abs(l - n)
    elif figure == 'конь':
        return (abs(k - m) == 2 and abs(l - n) == 1) or (abs(k - m) == 1 and abs(l - n) == 2)
    else:
        return False


# Функции для проверки возможности хода ферзя, ладьи или слона
def can_move_directly(k, l, m, n, figure):
    if figure == 'ферзь':
        return threatens(k, l, m, n, 'ладья') or threatens(k, l, m, n, 'слон')
    elif figure == 'ладья':
        return threatens(k, l, m, n, 'ладья')
    elif figure == 'слон':
        return threatens(k, l, m, n, 'слон')
    else:
        return False


# Функции для поиска второго хода
def find_second_move(k, l, m, n, figure):
    if threatens(k, l, m, n, 'ферзь') or can_move_directly(k, l, m, n, 'ферзь'):
        return "Ферзь может попасть на поле ({}, {}) одним ходом.".format(m, n)
    elif threatens(k, l, m, n, 'ладья') or can_move_directly(k, l, m, n, 'ладья'):
        return "Ладья может попасть на поле ({}, {}) одним ходом.".format(m, n)
    elif threatens(k, l, m, n, 'слон') or can_move_directly(k, l, m, n, 'слон'):
        offset_row = abs((k - m) // 2)
        offset_col = abs((l - n) // 2)
        x = min(k, m) + offset_row
        y = min(l, n) + offset_col
        return "Два хода: сначала на поле ({}, {}), затем на поле ({}, {}).".format(x, y, m, n)
    else:
        return "Фигура не может попасть на поле ({}, {}).".format(m, n)


# Ввод данных пользователем
k = int(input("Введите номер вертикали (от 1 до 8): "))
l = int(input("Введите номер горизонтали (от 1 до 8): "))
m = int(input("Введите номер вертикали для второго поля (от 1 до 8): "))
n = int(input("Введите номер горизонтали для второго поля (от 1 до 8): "))
figure = input("Введите фигуру (ферзь, ладья, слон, конь): ")

# Вывод результатов
print("Поля ({}, {}) и ({}, {}) являются полями одного цвета: {}".format(k, l, m, n, is_same_color(k, l, m, n)))
print("Фигура {} угрожает полю ({}, {}): {}".format(figure, m, n, threatens(k, l, m, n, figure)))
print("Фигура {} может с положения ({}, {}) попасть на поле ({}, {})".format(figure, k, l, m, n) if can_move_directly(k,
                                                                                                                      l,
                                                                                                                      m,
                                                                                                                      n,
                                                                                                                      figure) else find_second_move(
    k, l, m, n, figure))
