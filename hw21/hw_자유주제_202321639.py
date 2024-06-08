import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import pandas as pd

token = "7454510874:AAHBPK598I_kSGR1tcVRaKocQEdzOsGtmFQ"
id = "7266844044"

bot = telegram.Bot(token)

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

import pandas as pd
import random

filename = "노랭이 전면개정판.xlsx"
df = pd.read_excel(filename, engine='openpyxl').drop(columns=['Unnamed: 2'])

word_dict = dict(zip(df['단어'], df['뜻']))

random_words = random.sample(list(word_dict.keys()), 30)

for word in random_words:
    print(f"{word}: {word_dict[word]}")


def handler(update, context):
    user_text = update.message.text
    if user_text == "영단어":
        random_data = df.sample(n=30, replace=False)
        bot.send_message(chat_id=id, text=f"무작위로 선택된 30개의 영단어:\n{random_data}")
    else:
        bot.send_message(chat_id=id, text="잘못 입력하셨습니다.")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)