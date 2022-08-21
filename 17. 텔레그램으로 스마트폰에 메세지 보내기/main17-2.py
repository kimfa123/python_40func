import telegram

token ='5739936249:AAFNyL0PnbotyXii-2qbct5Is8vx3ar51Wo'
id = "5429084562"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")

#텔레그램으로 스마트폰에 메시지보내기 