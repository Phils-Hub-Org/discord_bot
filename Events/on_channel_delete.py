# ...

class OnChannelDelete:
    @staticmethod
    async def on_channel_delete(channel):
        """
        Triggered when a channel is deleted.

        Parameters:
        - channel (discord.abc.GuildChannel): The channel that has been deleted.
        """
        print(f'Channel deleted: {channel.name} (ID: {channel.id})')