import telebot

bot = telebot.TeleBot('YOUR_BOT_TOKEN')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    message_text = message.text

    with open('support_logs.txt', 'a') as file:
        file.write(f"User ID: {user_id}\n")
        file.write(f"Username: {user_name}\n")
        file.write(f"Message: {message_text}\n")
        file.write("\n")

    bot.reply_to(
        message, "Спасибо за ваше обращение! Мы свяжемся с вами в ближайшее время.")


bot.polling()


bot = telebot.TeleBot('YOUR_BOT_TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message, "Привет! Я готов отвечать на ваши вопросы. Отправьте мне вопрос из файла.")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    question = message.text

    try:
        with open('questions.txt', 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.strip() == question.strip():
                    answer = lines[i + 1].strip()
                    bot.reply_to(message, answer)
                    break
            else:
                bot.reply_to(
                    message, "К сожалению, я не знаю ответа на этот вопрос.")
    except FileNotFoundError:
        bot.reply_to(message, "Файл с вопросами не найден.")


bot.polling()
