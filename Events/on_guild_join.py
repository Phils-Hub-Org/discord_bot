from Components.ids import IDs

class OnGuildJoin:
    @staticmethod
    async def on_guild_join(guild):
        """
        Triggered when the bot joins a guild.

        Parameters:
        - guild (discord.Guild): The guild that the bot joined.
        """
        print(f'Joined guild: {guild.name} (ID: {guild.id})')

        if guild.id not in IDs.ALLOWED_GUILDS:
            print(f'Bot is in an unauthorized guild: {guild.name}. Leaving...')
            await guild.leave()  # Leave unauthorized guilds
        else:
            print(f"What's up, bitches? I'm here!")