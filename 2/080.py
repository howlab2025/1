import telegram

my_token = '-----------발급받은 토큰을 입력하세요----------'
my_token = '657609001:AAHQaGxssRQrtfUCc6LqHqOd38Hq8QifZ_8'
# 봇 생성
bot = telegram.Bot(token=my_token)
print(type(bot))
print(bot)

# 봇(사용자) 정보 확인
bot_info = bot.getMe() 
print(type(bot_info))
print(bot_info)