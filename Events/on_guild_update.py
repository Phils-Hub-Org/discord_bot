# ...

class OnGuildUpdate:
    @staticmethod
    async def on_guild_update(before, after):
        """
        Triggered when a guild is updated.

        Parameters:
        - before (discord.Guild): The guild before the update.
        - after (discord.Guild): The guild after the update.
        """
        print(f'Guild updated: {before.name} (ID: {before.id})')
        
        if before.name != after.name:
            print(f'Name changed from {before.name} to {after.name}')
        
        if before.region != after.region:
            print(f'Region changed from {before.region} to {after.region}')