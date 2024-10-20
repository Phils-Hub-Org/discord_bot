import logging
from Components.bot import bot

logger = logging.getLogger(__name__)

VER = 'v2.0.0'

class OnReady:
    @classmethod
    async def on_ready(cls):
        """
        Triggered when the bot is ready to start.
        """
        try:
            logger.info(f'Logged in as {bot.user.name} {VER}')

            await bot.tree.sync()  # nothing is executed after the 'bot.tree.sync' line
        except Exception as e:
            print(f"Error: {e}")