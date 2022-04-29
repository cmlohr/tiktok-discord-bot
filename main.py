import os
import discord
# import tiktok
import requests

my_secret = os.environ['TOKEN']
client = discord.Client()

# tiktok request block 

# tiktok end




# testing block

# def check_hello():
#     is_hello = random.choice(hello.hello_check)
#     print(is_hello)
#     print(type(is_hello))
#     return is_hello

# end testing block

@client.event
async def on_ready():
    print('We have logged in a {0.user}.  TikTok-bot is active'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

   

    # /suggest begin
    if message.content.startswith("/tiktok status"):
        await message.channel.send("I am connected to TikTok")



client.run(my_secret)
