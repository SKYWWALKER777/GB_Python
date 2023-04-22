# 1
fib_list = []

n = int(input("Введите количество первых элементов последовательности Фибоначчи: "))

fib_list.append(1)
fib_list.append(1)

for i in range(2, n):
    fib_list.append(fib_list[i-1] + fib_list[i-2])

print(fib_list)

# 2
fruits = ['апельсин', 'банан', 'манго', 'яблоко', 'гранат']
letter = input("Введите первую букву фрукта: ")

for fruit in fruits:
    if fruit.startswith(letter):
        print(fruit)

# 3
responses = {
    'привет': 'Привет!',
    'как тебя зовут': 'Меня зовут GB.',
    'как дела': 'У меня всё хорошо, спасибо!',
    'пока': 'Пока!',
}


while True:
    user_input = input("Вы: ")
    if user_input in responses:
        print("Бот: " + responses[user_input])
    else:
        print("Бот: Я не понимаю, о чем вы говорите.")
