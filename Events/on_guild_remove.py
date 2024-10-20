# ...

class OnGuildRemove:
    @staticmethod
    async def on_guild_remove(guild):
        """
        Triggered when the bot leaves a guild.

        Parameters:
        - guild (discord.Guild): The guild that the bot left.
        """
        print(f'Left guild: {guild.name} (ID: {guild.id})')