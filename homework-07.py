import telebot
import random
import functools


def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result


numbers = [1, 2, 3, 4, 5]
squared_numbers = my_map(lambda x: x**2, numbers)
print(squared_numbers)


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


bot = telebot.TeleBot('YOUR_BOT_TOKEN')

target_number = random.randint(1, 1000)
attempts = 0


@bot.message_handler(commands=['start'])
def start(message):
    global target_number, attempts
    target_number = random.randint(1, 1000)
    attempts = 0
    bot.reply_to(
        message, "Привет! Я загадал число от 1 до 1000. Попробуй угадать!")


@bot.message_handler(func=lambda message: True)
def guess_number(message):
    global attempts
    user_number = int(message.text)
    attempts += 1

    if user_number == target_number:
        bot.reply_to(
            message, f"Поздравляю, ты угадал число {target_number}! Количество попыток: {attempts}")
    elif user_number < target_number:
        bot.reply_to(message, "Загаданное число больше.")
    else:
        bot.reply_to(message, "Загаданное число меньше.")


bot.polling()
