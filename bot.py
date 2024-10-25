import telebot, time, os
from config import token, api_key, secret_key
from logic import Text2ImageAPI

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def handle_message(message):
    bot.send_message(message.chat.id, """
Привет!👋
Я бот генератор картинок
Я могу генерировать красивые картинки на основе ваших предпочтений👌✔️
Чтобы начать генерировать картинки просто напишите то что вы хотите получить(картину)
Генерация идёт одну минуту или более 30 секунд
Чтобы посмотреть другие боты автора напишите /other_bots !
                     """)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text
    bot.send_message(message.chat.id, "Идёт генерация картинки...")
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', api_key, secret_key)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]

    api.save_image(images, 'decoded_image.jpg')

    with open('decoded_image.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    bot.delete_message(message.chat.id, message.message_id - -1)


bot.infinity_polling()