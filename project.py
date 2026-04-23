from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def main():
    bot = telegram.Bot("6520228246:AAFOi2IowXZK9hxs9wX0hO7WGoxgSJc-v3M")
    async with bot:
        print(await bot.get_me())

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help message."""
    await update.message.reply_text("Send /start to get a welcome message.\nSend any text to get it echoed back.")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send weather information."""
    
    await update.message.reply_text("")

application = Application.builder().token("6520228246:AAFOi2IowXZK9hxs9wX0hO7WGoxgSJc-v3M").build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("echo", echo))
application.add_handler(CommandHandler("help", help))

# on non command i.e message - echo the message on Telegram
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the bot until the user presses Ctrl-C
application.run_polling(allowed_updates=Update.ALL_TYPES)

application.run_polling(allowed_updates=Update.ALL_TYPES)
