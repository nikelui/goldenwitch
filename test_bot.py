from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

# Read token from external location
with open('token.txt', 'r') as tk:
    token = tk.read()

@bot.event
async def on_ready():
    print('{0.user} has joined the Golden Land'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello, sucker!')
    await bot.process_commands(message) # need this to work

@bot.command(name='quit')
async def _quit(ctx):
    await bot.logout()

@bot.command()
async def deal(ctx):
    await ctx.send('Just a test to see if the command works')

bot.run(token)
