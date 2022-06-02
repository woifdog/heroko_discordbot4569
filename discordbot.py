
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    if client.user in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
        if content == '':
            content = first
        if translator.detect(content).lang == DSTLanguage:
            return
        if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
            remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage) 

# Bot起動
client.run(TOKEN)
