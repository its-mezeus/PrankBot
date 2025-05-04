import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Your bot token
bot = telebot.TeleBot("6014279190:AAHHxh5IWcM2IpWCFcJJz-WdVFkfaS67E9c")

# Fixed image URL
REPLY_IMAGE_URL = "https://envs.sh/lg2.jpg"

# /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name or "there"
    welcome_text = (
        f"Hello 👋🏻 <b>{user_name}</b>\n\n"
        "<b>I am a Powerful Image Editor Bot 😄</b>\n"
        "<b>Send any Image and See My Magic ✨</b>"
    )

    # Inline "Owner 🙂" button
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Owner 🙂", callback_data="owner_info"))

    bot.send_message(message.chat.id, welcome_text, parse_mode="HTML", reply_markup=markup)

# Handle image uploads
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Send waiting message
    wait_msg = bot.reply_to(message, "Wait Let me Cook.... 💓")

    # Wait 5 seconds
    time.sleep(5)

    # Delete the waiting message
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=wait_msg.message_id)
    except Exception as e:
        print("Failed to delete message:", e)

    # Send the fixed image
    bot.send_photo(message.chat.id, photo=REPLY_IMAGE_URL)

# Handle button callback
@bot.callback_query_handler(func=lambda call: call.data == "owner_info")
def callback_owner(call):
    bot.answer_callback_query(call.id, text="Arinjitt Enthina 😂", show_alert=True)

# Start polling
bot.polling()