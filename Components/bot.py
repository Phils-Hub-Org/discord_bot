from discord.ext import commands
from Components.intents import Intents

# Set up the bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=Intents.intents)