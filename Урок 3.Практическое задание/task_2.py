"""
Задание_2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.

Подсказка:
Попробуйте решить эту задачу в одну строку (такое решение точно есть)

Пример:
Исходный массив: [8, 3, 15, 6, 4, 2], результат: [0, 3, 4, 5]
"""

import random
NUMBERS = []
while len(NUMBERS) < 15:
    i = random.randint(-100, 100)
    NUMBERS.append(i)
print(NUMBERS)

print([NUMBERS.index(i) for i in NUMBERS if i % 2 == 0])
