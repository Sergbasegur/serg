from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from  bot_commands import calc_sum, hi_command, hu_command



app = ApplicationBuilder().token("5834900881:AAGXGsLsHrfiPAeLYkHEMTPkwO4MyltBuFI").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("wer", hu_command))
app.add_handler(CommandHandler("calc", calc_sum))

print('server start')

app.run_polling()