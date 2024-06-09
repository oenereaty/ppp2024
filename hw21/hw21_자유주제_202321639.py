import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import pandas as pd
import random

token = "7454510874:AAHBPK598I_kSGR1tcVRaKocQEdzOsGtmFQ"
id = "7266844044"

bot = telegram.Bot(token)

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

filename = "노랭이 전면개정판.xlsx"
df = pd.read_excel(filename, engine='openpyxl').drop(columns=['Unnamed: 2'])

word_dict = dict(zip(df['단어'], df['뜻']))
random_words = random.sample(list(word_dict.items()), 30)
send_words = []
for word, mean in random_words:
    send_words.append(f"{word}: {mean}")

def handler(update, context):
    user_text = update.message.text
    if user_text == "영단어":
        bot.send_message(chat_id=id, text=f"오늘의 영단어!\n")
        bot.send_message(chat_id=id , text=("\n".join([i for i in send_words])))
    else:
        bot.send_message(chat_id=id, text="잘못 입력하셨습니다.")


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
