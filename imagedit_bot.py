import telebot
import time
from flask import Flask
from threading import Thread
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# BOT TOKEN
bot = telebot.TeleBot("6014279190:AAEpUHeY6eFStBFAQiYVs8kTpezfJtWVEs4")

# FIXED IMAGE URL
REPLY_IMAGE_URL = "https://envs.sh/lg2.jpg"

# Flask keep-alive server
app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# START command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name or "there"
    welcome_text = (
        f"Hello 👋🏻 <b>{user_name}</b>\n\n"
        "<b>I am a Powerful Image Editor Bot 😄</b>\n"
        "<b>Send any Image and See My Magic ✨</b>"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Owner 🙂", callback_data="owner_info"))
    bot.send_message(message.chat.id, welcome_text, parse_mode="HTML", reply_markup=markup)

# Handle image messages
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    wait_msg = bot.reply_to(message, "Wait Let me Cook.... 💓")
    time.sleep(5)
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=wait_msg.message_id)
    except Exception as e:
        print("Delete failed:", e)
    bot.send_photo(message.chat.id, photo=REPLY_IMAGE_URL)

# Handle inline button callback
@bot.callback_query_handler(func=lambda call: call.data == "owner_info")
def callback_owner(call):
    bot.answer_callback_query(call.id, text="Arinjitt Enthina 😂", show_alert=True)

# Run keep-alive server
keep_alive()

# Start the bot
bot.polling()
