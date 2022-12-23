from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from folder.bot_command import *





app = ApplicationBuilder().token("5716120553:AAERs_jBz7W1FsRYgtvebPQojJzLDscwR0c").build()

app.add_handler(CommandHandler("Hi", hi_fi))
app.add_handler(CommandHandler("time", time_commands))
# app.add_handler(CommandHandler("help", help_commands))
app.add_handler(CommandHandler("sum", sum_commands))
print('server start')

app.run_polling()