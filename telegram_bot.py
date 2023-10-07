import tracemalloc
tracemalloc.start()
import logging
from telegram import Update, Message
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! How can I assist you today?')
    chat_id = update.effective_chat.id
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Sure! I can help you with any questions you have. Just let me know what you need.')


async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Goodbye! Feel free to reach out if you have any more questions.')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    message_text = update.message.text

    # Forward the message to your chat
    your_chat_id = 'your_chatid'
    await context.bot.send_message(chat_id=chat_id, text=f"User {chat_id} says: {message_text}")

 # Reply to the user in the original chat
    await context.bot.send_message(chat_id=chat_id, text="Your message has been forwarded and will be processed.")


bot_token = 'your_BOT_TOKEN'
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("bye", bye))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()