#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import numpy
import random
import re

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

BOTNAME = 'HumillasionesBot'
humillasiones = ['Te voy a joder tu puta vida','Cacho perrraaa','Eres una suciaa','Puuuuta, puuta!','Te encanta que te humillen, eh?','Que te calles la puta boca tío']
racho = ['Xaxiiii','Yamiraree','Keguenaa','Yatedigorodrigo','Alejandrikochikooo','Polapatillika']
viva = ['la manada','La manada','vox','box','don francisco franco','Don Francisco Franco','don Francisco Franco','franco','rabazo','RABAZO','jucuarlos','juan carlos','Juan Carlos','cuterga']
noviva = ['podemos']

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def humillar_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    messagelist = humillasiones
    update.message.reply_text(random.choice(messagelist))

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    if ((bool(re.match(r'.*[mM][oO][lL][aA].*',update.message.text))) and ((bool(re.match(r'.*[nN][oO].*',update.message.text))) != True)):
        choices = [0,1]
        choice = random.choice(choices)
        if choice == 1:
            update.message.reply_text(r'Mola')
        else:
            update.message.reply_text(r'Si q mola 🤠')
    elif ((bool(re.match(r'.*[nN][oO].*[mM][oO][lL][aA].*',update.message.text)))):
        choices = [r'No lo ase',r'No mola',r'No mola tío 🙅🏻‍♂️']
        choice = random.choice(choices)
        update.message.reply_text(choice)
    elif (bool(re.match(r'[mM][aAá][sS]',update.message.text))):
        choices = [r'Más',r'Si más',r'Necesitamos más 🤠']
        choice = random.choice(choices)
        update.message.reply_text(choice)
    elif ((bool(re.match(r'[oO][lL][aA]',update.message.text))) or (bool(re.match(r'[hH][oO][lL][aA]',update.message.text)))):
        rchoices = numpy.random.choice([1, 0], size = 100, p =[0.33,0.67])
        rchoice = random.choice(rchoices)
        if rchoice == 1:
            update.message.reply_text(r'Ola')
        else:
            pass
        
    elif (bool(re.match(r'[eE][sS][oO]',update.message.text))):
        pass
    elif ((bool(re.match(r'[yY][Aa][mM][iI][rR][aA][rR][eE].*',update.message.text))) or (bool(re.match(r'[xX][aA][xX][iI].*',update.message.text))) or (bool(re.match(r'[cC][hH][aA][cC][hH][iI].*',update.message.text))) or (bool(re.match(r'.*[rR][aA][cC][hH][oO].*',update.message.text)))):
        rchoices = numpy.random.choice([1, 0], size = 100, p =[0.5,0.5])
        rchoice = random.choice(rchoices)
        if rchoice == 1:
            choice = random.choice(racho)
            update.message.reply_text(choice)
        else:
            pass
    elif (bool(re.match(r'.*[Nn][oO].+?[sS][aA][bBvV][eE][nN].*',update.message.text))):
        choices = [r'Si sabemos',r'Si']
        choice = random.choice(choices)
        update.message.reply_text(choice)
    elif (bool(re.match(r'.*[Nn][oO].+?[pP][uU][eE][dD][eE][nN].*',update.message.text))):
        choices = [r'Si podemos',r'Si']
        choice = random.choice(choices)
        update.message.reply_text(choice)
    elif (bool(re.match(r'[aA][lL][gG][uU][iI][eE][nN].+?[sS][aA][bBvV][eE].*',update.message.text))):
        update.message.reply_text(r'Eso')
    elif (bool(re.match(r'.*[eE][rR][eE][sS].+?[uU][nN].*',update.message.text))):
        update.message.reply_text(r'Si es 🤠🤏🏻')
    elif ((bool(re.match(r'[oO][hH][hH].+?[gG][rR][aA][nN].+?[rR][aA][bB][aA][Zz][Oo].*',update.message.text))) or (bool(re.match(r'.*[tT][uU].+?[aA][mM][oO][?]',update.message.text)))):
        choices = [r'OHH GRAN RABAZO!!',r'🙇🏻‍♂️🙇🏻‍♂️🙇🏻‍♂️',r'OHH GRAN RABAZO!🙇🏻',r'OHH!🙇🏻‍♂️']
        choice = random.choice(choices)
        update.message.reply_text(choice)
    elif (bool(re.match(r'[vVbB][iI][vVbB][aA].*',update.message.text))):
        splitting = update.message.text.split(" ")
        for i in splitting:
            if any(i in s for s in viva):
                choices = [r'Viva',r'Biba',r'Olee!',r'Viva!!']
                choice = random.choice(choices)
                update.message.reply_text(choice)
                break
            elif any(i in s for s in noviva):
                choices = [r'🙅🏻‍♂️',r'No',r'No mola',r'No mola tío 🙅🏻‍♂️']
                choice = random.choice(choices)
                update.message.reply_text(choice)
                break
    elif (bool(re.match(r'.*[mM][eE].*[vVbB][oOiIyY].*[aA].+?[dD][oO][rR][mM][iI][rR].*',update.message.text))):
        choices = [0,1]
        choice = random.choice(choices)
        if choice == 0:
            update.message.reply_text(r'Ya?')
        else:
            choices = humillasiones
            choice = random.choice(choices)
            update.message.reply_text(choice)
    else:
        # If message does not match any condition, there is a 10 percent chance to reply
        rchoices = numpy.random.choice([1, 0], size = 100, p =[0.1,0.9])
        rchoice = random.choice(rchoices)
        if rchoice == 1:
            choices = [r'Eso',r'🤠🤏🏻']
            choice = random.choice(choices)
            update.message.reply_text(choice)
        else:
            pass

def empty_message(update: Update, context: CallbackContext) -> None:
    """
    Empty messages could be status messages, so we check them if there is a new
    group member, someone left the chat or if the bot has been added somewhere.
    """

    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            # Bot was added to a group chat
            if new_member.username == BOTNAME:
                pass
            # Another user joined the chat
            else:
                update.message.reply_text('quien entro')

    # Someone left the chat
    elif update.message.left_chat_member is not None:
        if update.message.left_chat_member.username != BOTNAME:
            update.message.reply_text('quien salio')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1574788396:AAFmjtaxd7YKz3PxMKgRggPsTlcx-Zq8OXQ", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("humillar", humillar_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # on status update i.e user joined the group
    dispatcher.add_handler(MessageHandler(Filters.status_update, empty_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
