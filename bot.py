from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="jarvis")

@bot.event
async def on_ready():
    print("Bot online")

@bot.event
async def on_message(message):
    if message.author == bot.user: # If the message is from a bot and not a human
        print("bot message received")
        return
    if message.content.lower().startswith('jarvis'): #if it starts with jarvis, the .lower() part makes sure it's not case sensitive
        def ingFrom(s): # Present participle function I copied from https://gist.github.com/arjun921/5f38259ea056fdc35617cb7449fb234e
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
        list = [*text] # takes the message and splits it up ['l', 'i', 'k', 'e', ' ', 't', 'h', 'i', 's']
        count = 0


        try:
            if list[6] == ",": #if the seventh character in the message is a comma, remove it  from the list(makes sure it supports messages with and without commas)
                list.pop(6)
        except:
            return #cancels if there's nothing after jarvis
        try:
            list[7]
        except:
            return # cancels if there's tnohing after the comma
        while list[6] == " ": #gets rid of all spaces leading up to the first character
            list.pop(6)

        for i in range(6): # remove the phrase "jarvis" from the beginning of the message
            list.pop(0)

        for i in list:
            if i != " ": # repeats until it finishes the first word in list(until there's a space)
                firstword.append(i)
                count = count+1 # counts how many characters it added to the firstword list
            else:
                break # if there's a space, quit
        for i in range(count): # remove the first word from the list
            list.pop(0)
        firstword = "".join(map(str, firstword)) # convert ['t', 'h', 'i', 's'] into 'this'

        firstword = ingFrom(firstword) # attempts to make the first word a present participle
        list = "".join(map(str, list)) # same as line 63

        final = firstword + list # creates the final text
        await message.channel.send(final.lower()) # send the final message
        
bot.run('PUT YOUR BOT TOKEN HERE')
