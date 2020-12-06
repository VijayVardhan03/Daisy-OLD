
from tswift import Song


from telegram import (Message, Chat, MessageEntity, ParseMode, ChatAction, TelegramError, Update,
                      InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove)

from from telegram.ext import CallbackContext ,CommandHandler, run_async, Filters

from SaitamaRobot import dispatcher
                      
from SaitamaRobot.modules.disable import DisableAbleCommandHandler

@run_async
def lyrics(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message
    query = " ".join(args)
    song = ""
    if not query:
        msg.reply_text("You haven't specified which song to look for!")
        return
    else:
        song = Song.find_song(query)
        if song:
            if song.lyrics:
                reply = song.format()
            else:
                reply = "Couldn't find any lyrics for that song!"
        else:
            reply = "Song not found!"
        if len(reply) > 4090:
            with open("lyrics.txt", 'w') as f:
                f.write(f"{reply}\n\n\nOwO UwU OmO")
            with open("lyrics.txt", 'rb') as f:
                msg.reply_document(document=f,
                caption="Message length exceeded max limit! Sending as a text file.")
        else:
            msg.reply_text(reply)
            
            
            LYRICS_HANDLER = DisableAbleCommandHandler("lyrics", lyrics, pass_args=True)
            
            dispatcher.add_handler(LYRICS_HANDLER)