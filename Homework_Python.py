# Homework № 1

# a, b = 2, 1
# print(a, " ", b)
# a = a + b
# b = a - b
# a = a - b
# print(a, " ", b)


# Homework № 2 ----------------------------------------------------------

# a = int(input("Введите число от 1 до 99: "))
# b = a - (a % 10)  # десятки
# a = a % 10  # единицы
# if a == 1:
#     print(a + b,  "копейка")
# if 2 <= a <= 4:
#     print(a + b, "копейки")
# if a == 0 or 5 <= a <= 10:
#     print(a + b, "копеек")
# # elif 11 >= a <= 14:
# else:
#
#     # c = (a % 10) + (round(a // 10))
#     print(a + b, "копеек")


# Homework № 3 -----------------------------------------------------------

# a = int(input("Количество символов: "))
# b = input("Тип символа: ")
# print("0 - горизонтальная")
# print("1 - вертикальная")
# n = int(input("ориентация линии: "))
# i = 0
# while i < a:
#     if n == 0:
#         print(b, end=" ")
#     if n == 1:
#         print(b)
#     i += 1


# Homework № 4 -----------------------------------------------------------

# a = int(input("Введите количество чисел последовательности: "))
# res = 0
# summa = 0
# for i in range(a):
#     b = float(input("Введите число: "))
#     summa += b
#     res = summa / a
# print("количество чисел: ", a)
# print("среднее арифметическое: ", round(res, 2))


# Homework № 5 -----------------------------------------------------------

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.insert(0, x)
#     else:
#         print(x, "не делится на 3 без остатка.")
# print(s)


# Homework № 6 -----------------------------------------------------------

# print("Введите элементы списка: ")
# n = int(input("n =  "))
# array = [int(input("-> ")) for i in range(n)]
# print(array)
# print("Введите индекс: ")
# k = int(input("k = "))
# print("Введите значение: ")
# c = int(input("c = "))
# array.insert(k, c)
# print(array)


# Homework № 7 -----------------------------------------------------------

# Вычисление площади фигур
# from math import sqrt, pi
#
# print("Выбор фигуры: ")
# print("1 - треугольник")
# print("2 - прямоугольник")
# print("3 - круг")
# x = int(input(": "))
# s = 0
# if x == 1:
#     a = int(input("Введите сторону а = "))
#     b = int(input("Введите сторону b = "))
#     c = int(input("Введите сторону c = "))
#     p = (a + b + c) / 2
#     print("S = ", round(sqrt(p * (p - a) * (p - b) * (p - c)), 2))
# if x == 2:
#     a = int(input("Введите сторону а = "))
#     b = int(input("Введите сторону b = "))
#     print("S = ", a * b)
# if x == 3:
#     a = int(input("Введите сторону а (радиус) = "))
#     print("S = ", round(pi * (a ** 2), 2))
# if x < 0 or x > 3:
#     print("Значение некорректное, попробуйте еще раз !")


# Homework № 8-----------------------------------------------------------

# Вычисление площади фигур (с помощью функций)

# def area():
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     return a * b
#
#
# def area1():
#     a = int(input("Введите радиус: "))
#
#     return 3.14 * a ** 2
#
#
# def area2():
#     a = int(input("Введите основание: "))
#     b = int(input("Введите высоту: "))
#
#     return (a * b) / 2
#
#
# print("Выбор фигуры: ")
# print("1 - прямоугольник")
# print("2 - треугольник")
# print("3 - круг")
# x = int(input(": "))
#
# if x == 1:
#     print(area())
#
# elif x == 2:
#     print(area2())
# elif x == 3:
#     print(area1())
# else:
#     print("Значение не корректное")


# Homework № 9-----------------------------------------------------------
#
# tpl = tuple(input("Введите элементы кортежа: "))  # ввод с клавиатуры
# print(tpl)
from random import randint


# tpl = tuple(randint(0, 9) for i in range(10))  # сгенерировали кортеж
# print(tpl)  # вывели кортеж
# stl = [] # создали пустой СПИСОК
# for i in tpl: # проходим по кортежу
#     if i not in stl: # если элемента нет в списке
#         stl.append(i) # то добавляем его в список
# print(stl) # выводим список
# for i in stl: # проходим по списку
#     print("Количество ", i, "=", tpl.count(i))  # ???  # считаем элементы, и выводим результат


# Homework № 10 -----------------------------------------------------------


# print("Ура! У меня получилось!")  # GitHub


# Homework № 11 -----------------------------------------------------------

# m_olimpia = ["Matvei", "Evgeniya", "Michail", "Maxim", "Natalia"]
# ph_olimpia = ["Maxim", "Matvei", "Alexandr"]
# all_prizewinners = m_olimpia + ph_olimpia  # все призеры
# match_olimpia = set(m_olimpia)  # преобразовали
# phys_olimpia = set(ph_olimpia)  # преобразовали
# two_prizewinners = match_olimpia & phys_olimpia  # призеры двух олимпиад ??????????
# new_match_olimpia = match_olimpia & phys_olimpia  # новый список по матем
# del phys_olimpia  # удалили список по физике
# print("Все призеры: ", all_prizewinners)
# print("Призеры обеих команд: ", two_prizewinners)
# print("Обновленный список призеров по математике: ", new_match_olimpia)

# Homework № 12 -----------------------------------------------------------

# sales = {
#     'John': {
#         'N': 3056,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694
#     },
#     'Tom': {
#         'N': 4832,
#         'S': 6786,
#         'E': 4737,
#         'W': 3612
#     },
#     'Anne': {
#         'N': 5232,
#         'S': 4802,
#         'E': 5820,
#         'W': 1859
#     },
#     'Fiona': {
#         'N': 3904,
#         'S': 3645,
#         'E': 8821,
#         'W': 2451
#     }
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t",  y, ":", sales[x][y])
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])


# Homework № 13 -----------------------------------------------------------

# dict_ = {}
# summ = 0
# sr_bull = 0
# # j = 1
# a = int(input("кол-во: "))
# for i in range(a):
#     key = input(str(i + 1) + " -студент: ")
#     dict_[key] = int(input("бал: "))
# print(dict_)
#
# for k, v in dict_.items():
#     print(k, "->", v)
#     summ += v
#     sr_bull = summ / len(dict_)
#
# for i in dict_:
#     if dict_[i] > sr_bull:
#         print(dict_[i])
#
# print("Средний балл: ", round(sr_bull, 1))

# --------------------------------------------------------------------------------------------
#
# students = {}
#
# n = int(input("Кол-во студентов: "))
# s = 0
# for i, key in enumerate(range(n), 1):
#     name = input(str(i) + "-й студент: ")
#     point = int(input("Балл: "))
#     students[name] = point  # записали данные в словарь
#     s += point
#
# average = s / n
# print("Средний балл:", average)
# for key in students:
#     if students[key] > average:
#         print(key)


# def func(i):
#     return i[1]
#
#
# d = {"b": 15, "a": 7, "c": 3}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# print(dict(lst))


# Homework № 14 -----------------------------------------------------------

# Найти S параллелепипеда и прямоугольника
# def outer(a, b, c):  # создали функцию, передали стороны параллелепипеда
#     def inner(i, j):  # создали вложенную функцию, передали стороны прямоугольника
#         return i * j # вернет произведение сторон (S прямоугольника)
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))  # используем (вызываем) вложенную функцию (умножение сторон)
#     return s # наружная функция вернет произведение сторон параллелепипеда (S параллелепипеда)
#
#
# print(outer(2, 4, 6))  # вызываем функцию, передаем вводимые значения (стороны фигур)
# print(outer(5, 8, 2))  # вызываем функцию, передаем вводимые значения (стороны фигур)
# print(outer(1, 6, 8))  # вызываем функцию, передаем вводимые значения (стороны фигур)

# ------------------------------
# s = 0  # объявили переменную
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s  # сделали переменную глобальной
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(s)  # выводим содержимое глобальной переменной
# outer(2, 4, 6)  # вызываем функцию, передаем вводимые значения (стороны фигур)
# print(s)  # выводим содержимое глобальной переменной
# outer(5, 8, 2)  # вызываем функцию, передаем вводимые значения (стороны фигур)
# print(s)  # выводим содержимое глобальной переменной
# outer(1, 6, 8)  # вызываем функцию, передаем вводимые значения (стороны фигур)
# print(s)  # выводим содержимое глобальной переменной

# ------------------
#
# def outer(a, b, c):  # 2, 4, 6
#     s = 0  # 44
#
#     def inner(i, j):
#         nonlocal s
#         s = s + i * j  # s += i * j   # s = 20 + 24 = 44
#
#     inner(a, b)  # 2, 4
#     inner(a, c)  # 2, 6
#     inner(b, c)  # 4, 6
#     return 2 * s  # 2 * 44
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# Homework № 15 -----------------------------------------------------------

# print(list(filter(lambda i: i == i[::-1], ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom'))))

# Homework № 16 -----------------------------------------------------------

#
# def avg(fn):
#     def wrap(*arg):
#         a = ""
#         for i in arg:
#             a += str(i) + ", "  # "2, 3, 3, 4, "
#         print("Среднее арифметическое:", a[:-2], "=", fn(*arg) / len(arg))
#
#     return wrap
#
#
# @avg
# def summa(*args):  # (2, 3, 3, 4) # функция находящая сумму, *args - любое кол-во элементов
#     print("Сумма чисел:", ", ".join(map(str, args)), "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# Homework № 17 -----------------------------------------------------------
#
# fio = input("Введите ФИО: ").split()
# print(fio)
# print(f"{fio[0]} {fio[1][0]}.{fio[2][0]}.")


# Homework № 18 -----------------------------------------------------------


# import re
#
# s = "+ 7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# pattern = r'\+?7\d{10}'
#
# print(re.findall(pattern, s))


# Homework № 19 -----------------------------------------------------------

# import re
#
# password = "my-p@ssw0rd"
# reg = r"[A-Za-z\d\@-]"
# print(re.findall(reg, password))


# Homework № 20 -----------------------------------------------------------


def negative_numbers(n):
    if not n:
        return 0
    count = 0
    if n[0] < 0:
        count += 1
    return negative_numbers(n[1:]) + count


lst = [-2, 3, 8, -11, -4, 6]
print(negative_numbers(lst))
