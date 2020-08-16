import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="toss")
async def toss_a_coin(ctx, number_of_tosses=""):
	if number_of_tosses == "":
		await ctx.send(random.choice(["Heads", "Tails"]))
	else:
		number_of_tosses = int(number_of_tosses)
		result = []
		if number_of_tosses > 500:
			number_of_tosses = 500
		for x in range(0, number_of_tosses):
			result.append(random.choice([1, 0]))
		await ctx.send("Result of {} coin tosses:\nNumber of Heads: {}, {:.3f}%\nNumber of Tails: {}, {:.3f}%".format(number_of_tosses, sum(result), sum(result)/number_of_tosses * 100, number_of_tosses - sum(result), (number_of_tosses - sum(result))/number_of_tosses * 100))

"""
@bot.command(name="spam")
async def spam(ctx, *args):
	if args == []:
		await ctx.send("No message to spam")
		return
	for x in range(0, 10):
		await ctx.send(" ".join(args))
		time.sleep(0.4)
"""

@bot.command(name="echo")
async def echo(ctx, *args):
	if args == []:
		await ctx.send("Nothing to Echo")
		return

	await ctx.send(" ".join(args))
	

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	if message.content == "clear":
		await message.channel.send("Bruh this is not a terminal")

	await bot.process_commands(message)

bot.run(TOKEN)
#client.run(TOKEN)
