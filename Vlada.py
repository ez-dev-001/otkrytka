import telebot
import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

bot = telebot.TeleBot(config.TOKEN)

ADMIN_IDS = [1409326380,946672357]  # Список администраторов

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Проверка, является ли пользователь администратором
    if user_id not in ADMIN_IDS:
        bot.send_message(chat_id, "⛔ У вас нет доступа к этому боту!")
        return

    # Создание кнопки "Далее"
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("➡ Далее", callback_data="next_text")
    markup.add(next_button)

    valentine_text = "💌 Привет,мой пионер!\n Это твой творческий небольшой подарок о котором я говорил.💖 \n \
    я долго думал, как так сделать красиво всё, чтобы это был настоящий приятный подарок.\n\n Нажми на кнопочку и будет продолжение)"

    # Отправка первого сообщения с кнопкой
    bot.send_message(chat_id, valentine_text, reply_markup=markup)

# Обработчик нажатия кнопки (второй шаг)
@bot.callback_query_handler(func=lambda call: call.data == "next_text")
def send_next_text(call):
    chat_id = call.message.chat.id

    # Удаляем предыдущее сообщение с кнопкой
    bot.delete_message(chat_id, call.message.message_id)

    # Создание новой кнопки "Продолжить"
    markup = InlineKeyboardMarkup()
    continue_button = InlineKeyboardButton("❤️ Продолжить", callback_data="final_step")
    markup.add(continue_button)
    valentine_text2= "И пара слов без которых я не могу обойтись. \n \
    Много есть легенд о Дне Святого Валентина. И как врач женил людей, когда был запрет на это, и как герцог с темницы писал письма своей возлюбленной.\n Так позволь же мне ты, Влада, создать нашу с тобой легенду о любви нашей истории.\n\
    Ведь в нынешнее время мало кто говорит о любви, а ведь это плохо. Жизнь и так кидает по разным степям нашей судьби в надежде на то, что мы сможем познать себя, но это не возможно без человека рядом.\n И мое жедание на этот день, чтобы ты была этим человеком с кем я познаю весь спектр эмоций, но я уверенно скажу 'люблю'\n\
    По этому насладись этим днем, ведь про тебя и мою любовь к тебе 💖 "
    # Отправляем второе сообщение с новой кнопкой
    bot.send_message(chat_id, valentine_text2, reply_markup=markup)

# Обработчик нажатия кнопки (третий шаг)
@bot.callback_query_handler(func=lambda call: call.data == "final_step")
def send_final_message(call):
    chat_id = call.message.chat.id

    # Удаляем предыдущее сообщение с кнопкой
    bot.delete_message(chat_id, call.message.message_id)
    valentine_text3="Как ты могла заметить тема подарка связана с LEGO. \n По этому я подготовил еще кое-что..."


    text_msg=bot.send_message(chat_id, valentine_text3)
    # Отправляем первое сообщение о загрузке
    loading_message = bot.send_message(chat_id, "🔄 Загрузка... 0%")
     # Имитация прогресса загрузки (5-7 секунд)
    loading_steps = [5, 17, 26, 39, 52, 68, 79, 91, 100]  # Нерегулярные шаги для реалистичности
    for percent in loading_steps:
        time.sleep(0.7)  # Пауза между обновлениями
        try:
            bot.edit_message_text(f"🔄 Загрузка... {percent}%", chat_id, loading_message.message_id)
        except Exception:
            break  # Если сообщение удалено или ошибка, прекращаем

    # Удаляем сообщение с загрузкой
    bot.delete_message(chat_id, loading_message.message_id)
    bot.delete_message(chat_id, text_msg.message_id)


    # Картинка-открытка (замените URL на свою картинку)
    valentine_image = "https://i.imgur.com/rck2iMm.png"

   
    markup = InlineKeyboardMarkup()
    continue1_button = InlineKeyboardButton("Войти в мир", callback_data="final1_step")
    markup.add(continue1_button)
    # Отправка изображения с поздравлением
    bot.send_photo(chat_id, valentine_image, caption="Добро пожаловать в цифровой мир лего и набора который сейчас у тебя)",reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == "final1_step")
def send_final_message(call):
    chat_id = call.message.chat.id

    # Удаляем предыдущее сообщение с кнопкой
    bot.delete_message(chat_id, call.message.message_id)
    valentine_image = "https://i.imgur.com/P2lScjv.png"
    markup = InlineKeyboardMarkup()
    continue2_button = InlineKeyboardButton("Cделать ЛЕГО копию и добавить её", callback_data="final2_step")
    markup.add(continue2_button)




    bot.send_photo(chat_id, valentine_image, caption="Раз Париж это город любви, то этом мире так же.\n Вот ЛЕГО Бора уже наслаждаеться видами)\n У него есть тоже подарок, но для этого нужно перенсти тебя к нему, сегодня это можно сделать по кнопке",reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == "final2_step")
def send_final_message(call):
    
    chat_id = call.message.chat.id

    # Удаляем предыдущее сообщение
    bot.delete_message(chat_id, call.message.message_id)

    # Отправляем первое сообщение о загрузке
    loading_message = bot.send_message(chat_id, "🔄 Загрузка... 0%")

    # Имитация прогресса загрузки (5-7 секунд)
    loading_steps = [5, 17, 26, 39, 52, 68, 79, 91, 100]  # Нерегулярные шаги для реалистичности
    for percent in loading_steps:
        time.sleep(0.7)  # Пауза между обновлениями
        try:
            bot.edit_message_text(f"🔄 Загрузка... {percent}%", chat_id, loading_message.message_id)
        except Exception:
            break  # Если сообщение удалено или ошибка, прекращаем

    # Удаляем сообщение с загрузкой
    bot.delete_message(chat_id, loading_message.message_id)

    # Отправляем финальное изображение
    final_image = "https://i.imgur.com/Ev8gzgV.png"  # Замени на свою картинку
    bot.send_photo(chat_id, final_image, caption="А вот и ты! Бора принес очень необычный подарок\n\n Сделано Владиком c любовью ❤️")

# Перезапуск бота при ошибке
while True:
    try:
        print("Запуск бота...")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка в bot.polling: {e}. Перезапуск через 5 секунд...")
        time.sleep(5)
