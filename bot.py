import os
import pytesseract
from PIL import Image
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)


def start(bot, context):
    bot.message.reply_text(f"Салем {bot.message.from_user.first_name} {bot.message.from_user.last_name}!\nФото жіберіңіз!")


def photo(bot, context):
    id = bot.message.from_user.id
    name = str(id) + ".jpg"
    filepath = "D:\\Python\\Nurbot\\" + name

    largest_photo = bot.message.photo[-1].get_file()
    largest_photo.download(filepath)

    text = image_text(filepath)
    if len(text) == 0:
        bot.message.reply_text("Басқа сурет жіберіп көріңіз!!!")
        os.remove(filepath)
        return

    bot.message.reply_text(text)
    os.remove(filepath)


def image_text(filepath):
    img = Image.open(filepath)
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img,lang='eng', config=custom_config)
    return text


def main():
    updater = Updater("5039796745:AAFS3CmCpIaRKIxCRqP1Sb27im1U5Gcz5yw")
    dp = updater.dispatcher

    photo_handler = MessageHandler(Filters.photo, photo)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(photo_handler)

    updater.start_polling()


main()
