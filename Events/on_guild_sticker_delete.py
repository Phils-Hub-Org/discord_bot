# ...

class OnGuildStickerDelete:
    @staticmethod
    async def on_guild_sticker_delete(sticker):
        """
        Triggered when a sticker is deleted from a guild.

        Parameters:
        - sticker (discord.Sticker): The sticker that was deleted.
        """
        print(f'Sticker deleted: {sticker.name} (ID: {sticker.id})')