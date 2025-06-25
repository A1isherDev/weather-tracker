import asyncio

from telebot.async_telebot import AsyncTeleBot
from TOKENS import BOT_TOKEN

bot = AsyncTeleBot(BOT_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])

async def send_welcome(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ''  #if last name doesn't exist it will replace by space
    full_name = f"{first_name} {last_name}".strip()
    text = f'Hello {full_name}! This bot will help you keep track of the weather in your city.'
    await bot.reply_to(message, text)



@bot.message_handler(commands=['help'])
async def help_message(message):
    text = """Help Menu:

Welcome to the Weather Tracker Bot!
Here’s what you can do:

/start — Start interacting with the bot.

/help — Show this help message.

/weather [city] — Get the current weather for a specific city.

/forecast [city] — See a 3-day weather forecast for a city.

/settings — Customize your preferences (temperature units: °C/°F).

Examples:

/weather London

/forecast New York

If you need any support or encounter issues, feel free to contact with me support@alisherit.uz!

Stay prepared and enjoy the weather! ☀️🌧️❄️"""
    await bot.reply_to(message, text)


asyncio.run(bot.polling())