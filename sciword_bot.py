import discord
from random import choice
words = open('sciword.txt').read().splitlines()
client = discord.Client()
@client.event
async def on_message(msg):
	if msg.content == 'word':
		await msg.channel.send(f"{msg.author} ||{choice(words)}||")
if __name__ == '__main__':
	client.run(os.environ['BOT_TOKEN'])
