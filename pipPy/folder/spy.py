from telegram import Update
from telegram.ext import ContextTypes


async def log_commands(update: Update, context: ContextTypes):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()