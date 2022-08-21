import telegram

token = '5739936249:AAFNyL0PnbotyXii-2qbct5Is8vx3ar51Wo'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)

#텔레그램으로 스마트폰에 메시지 보내기 