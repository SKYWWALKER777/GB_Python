# Задача 1

lst = [2, 3, 4, 6, 7, 8]
result = list(filter(lambda x: x > 5, lst))
print(result)

# Задача 2

lst = [1, 5, 2, 3, 4, 6, 1, 7]
result = []
temp = [lst[0]]
for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        temp.append(lst[i])
    else:
        if len(temp) > len(result):
            result = temp
        temp = [lst[i]]
if len(temp) > len(result):
    result = temp
print(result)

# Задача 3

lst = [1, 4, 2, 3, 4, 6, 1, 7]
unique_lst = list(set(lst))
count = len(lst) - len(unique_lst)
print(count)
print(unique_lst)
