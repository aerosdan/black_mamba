from telegram.ext import CommandHandler, Filters, MessageHandler, Updater,Dispatcher
from src.notification.telegram_notfy.conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
#from src.charts.generate_charts import plt
#plt.savefig('diario.png')
import time
a=open('teste','w')
def start(bot, update):
    response_message = "Olá"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
def acao(bot, update):
    response_message ="diario"
    bot.send_photo(chat_id=update.message.chat_id,
                   photo=open('diario.png', 'rb'))
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
def cadastro(bot, update):
    response_message ="Para fazer o cadastro, precisamos apenas que informe seu e-mail: "
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=HTTP_CATS_URL + args[0]
    )


def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('acao', acao)
    )
    dispatcher.add_handler(
        CommandHandler('cadastro', cadastro)
    )
    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()