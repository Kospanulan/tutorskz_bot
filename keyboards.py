from telebot import types
import numpy as np

disciplines = {"physics": "Физика", "math": "Математика", "programming": "Программирование",
               "cancel": "Отмена", "complete": "Готово!"}

clients = {"task": "Мне нужны решения задач.", "solution": "Я буду решать задачи.",
           "cancel": "Отмена"}

program_lang = {"cpp": "C++", "py": "Python",
                "cancel": "Отмена", "complete": "Готово!"}


# cancel_btn = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
# complete_btn = types.InlineKeyboardButton(text="Готово!", callback_data="complete")


def classification(type, dict):
    pass


def make_keyboard(keyboard, data, upd):
    for callback, t in data.items():
        if callback == upd:
            t += u'\U00002705'
        keyboard.add(types.InlineKeyboardButton(text=t, callback_data=callback))
    return keyboard


def typeof_client(upd=""):
    return make_keyboard(types.InlineKeyboardMarkup(), clients, upd)


def set_task_discipline(upd=""):
    return make_keyboard(types.InlineKeyboardMarkup(), disciplines, upd)


def set_disciplines_for_solution(upd=""):
    return make_keyboard(types.InlineKeyboardMarkup(), disciplines, upd)


def set_program_lang(upd=""):
    return make_keyboard(types.InlineKeyboardMarkup(), program_lang, upd)
