from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="jarvis")

@bot.event
async def on_ready():
    print("Bot online")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        print("bot message received")
        return
    if message.content.lower().startswith('jarvis'):
        def ingFrom(s):
            for x in s:
                li.append(x)
            if li[len(li)-1]=='e' and li[len(li)-2]!='i':
                del li[len(li)-1]
                li.append("ing")
            elif li[len(li)-1]=='e' and li[len(li)-2]=='i':
                del li[len(li)-1]
                del li[len(li)-1]
                li.append("ying")
                """To Check"""
            elif li[len(li)-2] in 'aeiou' and li[len(li)-1] not in 'aeiou':
                temp = li[len(li)-1]
                del li[len(li)-1]
                li.append(temp)
                li.append(temp)
                li.append("ing")
            elif li[len(li)-1] in 'aeiouy':
                li.append("ing")
            else:
                li.append("ing")
            return "".join(li)
        li=[]

        text = message.content
        firstword = []
        list = [*text]
        count = 0



        if list[6] == ",":
            list.pop(6)
        while list[6] == " ":
            list.pop(6)

        for i in range(6):
            list.pop(0)

        for i in list:
            if i != " ":
                firstword.append(i)
                count = count+1
            else:
                break
        for i in range(count):
            list.pop(0)
        firstword = "".join(map(str, firstword))

        firstword = ingFrom(firstword)
        list = "".join(map(str, list))

        final = firstword + list
        await message.channel.send(final.lower())
        
bot.run('PUT YOUR BOT TOKEN HERE')
