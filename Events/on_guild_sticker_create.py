# ...

class OnGuildStickerCreate:
    @staticmethod
    async def on_guild_sticker_create(sticker):
        """
        Triggered when a new sticker is created in a guild.

        Parameters:
        - sticker (discord.Sticker): The sticker that was created.
        """
        print(f'Sticker created: {sticker.name} (ID: {sticker.id})')