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
# print(tpl)
# stl = []
# for i in tpl:
#     if i not in stl:
#         stl.append(i)
# print(stl)
# for i in stl:
#     print("Количество ", i, "=", tpl.count(i))  # ???


# Homework № 10 -----------------------------------------------------------


print("Hello GitHub")

