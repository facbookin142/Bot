import logging
import random
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Token Railway variable se lega (secure method)
TOKEN = os.getenv("8546513391:AAGOYM1HlO_5_Zkze1pH1T9bffA8_O10KlM")

# Numbers list
NUMBERS_LIST = ["9876", "5432", "1122", "3344", "5566", "7788", "9900"]

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Join Now 1", url="https://t.me/YourChannel1"),
            InlineKeyboardButton("Join Now 2", url="https://t.me/YourChannel2")
        ],
        [InlineKeyboardButton("🎁 Claim Now", callback_data="claim")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! Pehle channels join karein phir Claim button dabayein:",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "claim":
        assigned_number = random.choice(NUMBERS_LIST)

        await query.edit_message_text(
            text=f"✅ Aapka Unique Number hai: {assigned_number}\n\nIsse safe rakhein!"
        )

def main():
    if not TOKEN:
        print("TOKEN missing! Railway variables me add karo.")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
