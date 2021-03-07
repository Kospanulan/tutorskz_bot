import config
import keyboards as kb
import messages as msg

import telebot
import os
from flask import Flask, request
import logging

if __name__ == '__main__':
    bot = telebot.TeleBot(config.TOKEN)

    @bot.message_handler(commands=['start'])
    def hello_msg(message):
        task_discipline = ""
        task_deadline = ""


        bot.send_message(message.chat.id, msg.choice_service, reply_markup=kb.typeof_client())


    @bot.callback_query_handler(func=lambda call: call.data in kb.clients)
    def callback_handler(call):
        if call.data == "task":
            edit_msg(call.message, msg.choice_task_discipline, kb.set_task_discipline())
        elif call.data == "solution":
            edit_msg(call.message, msg.choice_solution_discipline, kb.set_disciplines_for_solution())
        elif call.data == "cancel":
            if call.message.text == msg.choice_service:
                edit_msg(call.message, msg.bye)
            else:
                edit_msg(call.message, msg.choice_service, kb.typeof_client())
        elif call.data == "complete":
            pass


    @bot.callback_query_handler(func=lambda call: call.data in kb.disciplines.keys())
    def discipline_handler(call):
        if call.data != "programming":
            edit_msg(call.message, msg.choice_task_discipline, kb.set_task_discipline(call.data))
        else:
            edit_msg(call.message, msg.choice_task_prog_lang, kb.set_program_lang())

    @bot.callback_query_handler(func=lambda call: call.data in kb.program_lang)
    def program_lang_handler(call):
        edit_msg(call.message, msg.choice_task_discipline, kb.set_program_lang(call.data))

    def edit_msg(message, text, keyboard=None):
        bot.edit_message_text(message_id=message.id, chat_id=message.chat.id, text=text, reply_markup=keyboard)


    if "HEROKU" in list(os.environ.keys()):
        logger = telebot.logger
        telebot.logger.setLevel(logging.INFO)

        server = Flask(__name__)


        @server.route("/bot", methods=['POST'])
        def getMessage():
            bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
            return "!", 200


        @server.route("/")
        def webhook():
            bot.remove_webhook()
            bot.set_webhook(
                url="https://min-gallows.herokuapp.com/bot")  # этот url нужно заменить на url вашего Хероку приложения
            return "?", 200


        server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
    else:
        # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
        # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
        bot.remove_webhook()
        bot.polling(none_stop=True)

"""
Насчет настройки переменной окружения в Хероку - заходим в настройки приложения в Хероку и видим пункт "Config Variables".
И добавляем туда переменную HEROKU, чтобы наш бот отличал - запущен он на сервере или на локальной машине.
Но это уже не обязательно, это вкусовщна. Просто для меня это удобно.

"""
