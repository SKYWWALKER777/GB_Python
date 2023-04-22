# 1
import math
n = 60
factors = {}
count = 0

for i in range(2, n+1):
    while n % i == 0:
        if i in factors:
            factors[i] += 1
        else:
            factors[i] = 1
        count += 1
        n //= i
    if n == 1:
        break

print([k for k, v in factors.items() for _ in range(v)])
print(count)


# 2
assortment = ["Сливочное", "Бурёнка", "Вафелька", "Сладкоежка"]
in_stock = ["Сливочное", "Вафелька", "Сладкоежка"]
out_of_stock = set(assortment) - set(in_stock)
if out_of_stock:
    print(f"Закончилось: {', '.join(out_of_stock)}")
else:
    print("Ничего не закончилось.")
# 3

n = int(input("Введите количество знаков после запятой: "))
pi = round(math.pi, n)
print(pi)
