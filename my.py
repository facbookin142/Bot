import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 1. Yahan apna Bot Token dalein (BotFather se mila hua)
TOKEN = "YOUR_BOT_TOKEN_HERE"

# 2. Yahan wo numbers dalein jo aap logo ko dena chahte hain
NUMBERS_LIST = ["9876", "5432", "1122", "3344", "5566", "7788", "9900"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buttons ka design
    keyboard = [
        [
            InlineKeyboardButton("Join Now 1", url="https://t.me/YourChannel1"),
            InlineKeyboardButton("Join Now 2", url="https://t.me/YourChannel2")
        ],
        [InlineKeyboardButton("🎁 Claim Now", callback_query_data="claim")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome! Pehle channels join karein phir Claim button pe click karein:",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "claim":
        # Har user ko list se ek random number milega
        assigned_number = random.choice(NUMBERS_LIST)
        
        await query.edit_message_text(
            text=f"✅ Aapka Unique Number hai: {assigned_number}\n\nIsse safe rakhein!"
        )

def main():
    # Application build karein
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
