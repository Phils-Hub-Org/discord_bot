# ...

class OnChannelCreate:
    @staticmethod
    async def on_channel_create(channel):
        """
        Triggered when a new channel is created.

        Parameters:
        - channel (discord.abc.GuildChannel): The channel that has been created.
        """
        print(f'Channel created: {channel.name} (ID: {channel.id})')