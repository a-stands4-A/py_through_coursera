"""
На доске стоит белая шашка. Требуется определить, может ли она попасть в
заданную клетку, делая ходы по правилам и не пользуясь ходами дамки (т. е.
не используя возможность перемещаться назад после превращения в дамку).
Белые шашки могут ходить по клеткам одного цвета по диагонали вверх-влево
или вверх-вправо. Ходов может быть несколько!

Примечания

Доска имеет размер 8x8, вертикали и горизонтали  нумеруются числами от 1 до 8
начиная с левого нижнего угла. Исходная и конечная клетки не совпадают.

Формат ввода

Вводится клетка, где стоит шашка, а затем клетка, куда шашка должна попасть.

Каждая клетка описывается номером вертикали, а затем номером горизонтали. Под
номером вертикали имеется в виду не номер по вертикали, а номер вертикальной
линии считая слева направо. Аналогичная формулировка используется для номера
горизонтали: нумерация идет снизу вверх. Например, клетка A2 кодируется
как 1 2.

Формат вывода

Выведите слово YES (заглавными буквами), если шашка может попасть из начальной
клетки в указанную, и NO в противном случае.
"""
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x1 <= x2 and y1 <= y2:
    if (x1 % 2 == y1 % 2) == (x2 % 2 == y2 % 2):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
