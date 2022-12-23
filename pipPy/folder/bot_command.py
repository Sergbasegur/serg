from telegram import Update
from telegram.ext import  ContextTypes, CallbackContext
import datetime
from folder.spy import *

async def hi_fi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_commands(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def sum_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_commands(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # / sum 123  534543
    x = int(items[0])
    y = int(items[1])


    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def time_commands(update: Update, context: ContextTypes):
    log_commands(update, context)
    await update.message.reply_text(f'{datetime.datetime.now.time()}')


# async def log_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'')