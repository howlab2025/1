import telegram

def send_telegram_channel_message(channel_id, message):

    my_token = '-----------발급받은 토큰을 입력하세요----------'
    bot = telegram.Bot(token=my_token)
    
    bot.sendMessage(chat_id=channel_id, text=str(message))


if __name__ == '__main__':  

    channel_id = '@py100_test'    
    message = '채널에 보내는 메시지입니다.'
    send_telegram_channel_message(channel_id, message)
    