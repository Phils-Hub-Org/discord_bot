""" info

Cogs:
    Cogs are classes that group together related commands and listeners. They subclass commands.Cog, allowing for better organization and modularity in your bot.

Listeners:
    Listeners are methods defined within Cogs that handle specific stock events triggered by Discord (e.g., on_message, on_member_join).
    They allow the bot to respond to various actions that occur in the Discord server.

Summary
    Cogs help structure your bot's functionality, while listeners are specific methods that react to events within that structure.
    Listeners get executed immediately after the event it's listening for is triggered.

Note:
    on_message
        add: await bot.process_commands(message)
        to the end of said event/listener.

Remember:
    listeners are just (grouped) events, so do not use both of the following, only one:
        @bot.event
        async def on_message(message):
            pass
        
        @commands.Cog.listener()
        async def on_message(self, message):
            pass
"""

import os, sys, traceback, logging
from logging.handlers import RotatingFileHandler
from Components.bot import bot
from Components.env import Env
from Components.ids import IDs
from Components.youtube import YouTube
import Utils.py_utility as PyUtility
from Utils.globals_manager import GlobalsManager
from Components.os_validator import OSValidator
from Components.arch_validator import ArchValidator
from Handlers.events_handler import EventsHandler  # Import required to initialize events, especially on_ready

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler = RotatingFileHandler('bot.log', maxBytes=5*1024*1024, backupCount=5)
logging.getLogger().addHandler(handler)

try:
    if PyUtility.getPublicIp() != PyUtility.decryptData(os.getenv('VPS_IP').encode(), os.getenv('IP_AND_PORT_SYMMETRIC_KEY').encode()).decode():
        Env.set(Env.DEVELOPMENT)
    else:
        Env.set(Env.PRODUCTION)
except Exception as err:
    logging.error(f"Error: {err}")
    sys.exit(1)

IDs.initialize()
YouTube.initialize()

class Program:

    @classmethod
    def verifyEnv(cls) -> None:
        result, message = OSValidator.validate(OSValidator.OSValidatorEnum.WINDOWS)
        if not result:
            cls.teardown(message)

        result, message = ArchValidator.validate(ArchValidator.ArchValidatorEnum.X64)
        if not result:
            cls.teardown(message)

    @classmethod
    def initialize(cls) -> None:
        try:
            match Env.get():
                case Env.DEVELOPMENT:
                    GlobalsManager.register('discord_token', os.getenv('DISCORD_TEST_BOT_TOKEN').encode())
                case Env.PRODUCTION:
                    GlobalsManager.register('discord_token', os.getenv('DISCORD_BOT_TOKEN').encode())
            
            GlobalsManager.register('symmetric_key', os.getenv('DISCORD_BOT_SYMMETRIC_KEY').encode())
        
            cls.initEventLoop()
        except Exception as err:
            # cls.teardown(f"Error: {err}")
            cls.teardown(f"Error: {traceback.format_exc()}")
    
    @staticmethod
    def initEventLoop() -> None:
        bot.run(PyUtility.decryptData(GlobalsManager.get('discord_token'), GlobalsManager.get('symmetric_key')).decode())  # Start the asynico event loop
        # Nothing is executed after the 'bot.run' line cause .run is the main event loop
    
    @staticmethod
    def teardown(message: str) -> None:
        print(message)
        sys.exit(1)

if __name__ == "__main__":
    Program.verifyEnv()
    Program.initialize()

# CMD
# "C:\Users\Phil-\Documents\MEGA\__Workbase__\Phils-Hub\Discord Bot\output\Mr Bot 2.0.0.exe"

# POWERSHELL
# & "C:\Users\Phil-\Documents\MEGA\__Workbase__\Phils-Hub\Discord Bot\output\Mr Bot 2.0.0.exe"