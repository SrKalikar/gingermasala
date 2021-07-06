import telegram 
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1554223528:AAH7ZlltAlGrlCympw1V6P31ivBMEM2wrwU', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='(%asctimes), - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

def start(update, context):
     context.bot.send_message(chat_id=update.effective_chat.id, text="yo nigger")
start_handler=CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
def info(update,context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="This is an example bot created for experemental purpose.Enjoy it at your own risk.")
info_handler=CommandHandler('Info',info)
dispatcher.add_handler(info_handler)
def show_commands(update,context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Some useful commands to handle this bot\n1) /start\n2) /info")
show_commands_handler=CommandHandler('showcommands',show_commands)
dispatcher.add_handler(show_commands_handler)
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
  


 def main(self):
  self.start=start
  self.info=info
  self.show_commands= show_commands
  self.unknown = unknown
  return main()

updater.start_polling()
updater.idle()
if __name__ == '__main__':
  main(self)
