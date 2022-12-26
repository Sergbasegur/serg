from telegram import Update
from telegram.ext import ContextTypes, CallbackContext, ApplicationBuilder


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет, я калькулятор {update.effective_user.first_name}!')

async def hu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет, Boris {update.effective_user}!')   

async def calc_sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    item = msg.split()
    x = int(item[1])
    y = int(item[2])
   
    await update.message.reply_text(f'{x} + {y} = {x + y}!')

