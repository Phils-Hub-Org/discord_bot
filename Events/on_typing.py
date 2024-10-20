# ...

class OnTyping:
    @staticmethod
    async def on_typing(channel, user, when):
        """
        Triggered when a user starts typing in a text channel.

        Parameters:
        - channel (discord.TextChannel): The channel where the user is typing.
        - user (discord.User): The user who started typing.
        - when (datetime.datetime): The timestamp of when the user started typing.
        """
        print(f'{user.name} is typing in channel: {channel.name} at {when}')