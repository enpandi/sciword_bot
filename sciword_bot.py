import discord
from random import choice
client = discord.Client()
with open('sciword.txt') as sciword_txt:
	words = sciword_txt.read().splitlines()  # word pool
@client.event
async def on_message(msg):
	if msg.content == 'word':
		await msg.channel.send(f"{msg.author} ||{choice(words)}||")
if __name__ == '__main__':
	client.run(os.environ['BOT_TOKEN'])
