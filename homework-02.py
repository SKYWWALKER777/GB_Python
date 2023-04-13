# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = 3
factorial = 1
factorials_list = []
for i in range(1, N+1):
    factorial *= i
    factorials_list.append(factorial)
print(factorials_list)

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print("X\tY\tZ\tOutput")
for X in [False, True]:
    for Y in [False, True]:
        for Z in [False, True]:
            output = not (X and Y) or Z
            print(f"{X}\t{Y}\t{Z}\t{output}")

# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = 'one'
str2 = 'onetwonine'
result = {}
for char in str1:
    result[char] = str2.count(char)
print(result)

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

N = 3
my_list = list(range(-N, N+1))
shifted_list = my_list[-2:] + my_list[:-2]
print(shifted_list)
