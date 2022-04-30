import telebot
from telebot import types
from datetime import datetime
from datetime import date
import calendar

import meals

# creating bot
bot = telebot.TeleBot("5023319166:AAGBxAW60sNf5IHArxQ6k_Xbpzhvw3gmKdc")

curr_date = date.today()

week_day_int = datetime.today().isoweekday()

week_meals = meals.week_scedule

sunday = meals.daily[0]
monday = meals.daily[0]
tuesday = meals.daily[0]
wednesday = meals.daily[0]
thursday = meals.daily[0]
friday = meals.daily[0]
saturday = meals.daily[0]


# start
@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    what = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("My todays meals")
    item2 = types.KeyboardButton("My week meals")

    what.add(item1, item2)

    bot.send_message(message.chat.id, "Welcome! \n Today is: " + calendar.day_name[
        curr_date.weekday()] + "\n Choose what you want to do:".format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=what)


# daily meals
@bot.message_handler(content_types=['text'])
def daily(message):
    if message.chat.type == "private":

        if message.text == "My todays meals":

            if week_day_int == 7:
                bot.send_message(message.chat.id, sunday)
            elif week_day_int == 1:
                bot.send_message(message.chat.id, monday)
            elif week_day_int == 2:
                bot.send_message(message.chat.id, tuesday)
            elif week_day_int == 3:
                bot.send_message(message.chat.id, wednesday)
            elif week_day_int == 4:
                bot.send_message(message.chat.id, thursday)
            elif week_day_int == 5:
                bot.send_message(message.chat.id, friday)
            elif week_day_int == 6:
                bot.send_message(message.chat.id, saturday)
        elif message.text == "My week meals":
            bot.send_message(message.chat.id, week_meals)


bot.polling(none_stop=True)
