# ...

class OnGuildStickerUpdate:
    @staticmethod
    async def on_guild_sticker_update(before, after):
        """
        Triggered when a sticker is updated in a guild.

        Parameters:
        - before (discord.Sticker): The sticker before the update.
        - after (discord.Sticker): The sticker after the update.
        """
        print(f'Sticker updated: {before.name} (ID: {before.id})')