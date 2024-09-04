import telegram

my_token = '-----------발급받은 토큰을 입력하세요----------'

bot = telegram.Bot(token=my_token)

updates = bot.getUpdates()
print(updates)
print('\n')

for update in updates:
    print(update)
    print('\n')

latest_update = updates[-1]
print(latest_update.message.date)    #날짜
print(latest_update.message.chat.id) #상대방의 chat_id
print(latest_update.message.text)    #받는 메시지