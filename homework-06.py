# Задача 1
from math import gcd
n = int(input("Введите натуральное число: "))
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))

result = n + nn + nnn
print(result)

# Задача 2

arr = [0, 5, 6, 2, 7, 7, 8, 1, 1, 9]
n = input("Введите трехзначное число: ")

for i in range(len(arr)-2):
    if str(arr[i]) + str(arr[i+1]) + str(arr[i+2]) == n:
        print("Да")
        break
else:
    print("Нет")

# Задача 3


fractions = []
for denominator in range(2, 12):
    for numerator in range(1, denominator):
        if gcd(numerator, denominator) == 1:
            fractions.append(f"{numerator}/{denominator}")

print(fractions)
