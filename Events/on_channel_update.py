# ...

class OnChannelUpdate:
    @staticmethod
    async def on_channel_update(before, after):
        """
        Triggered when a channel is updated.

        Parameters:
        - before (discord.abc.GuildChannel): The channel before the update.
        - after (discord.abc.GuildChannel): The channel after the update.
        """
        print(f'Channel updated: {before.name} (ID: {before.id})')
        print(f'Before: Name: {before.name}, Topic: {before.topic}, Position: {before.position}')
        print(f'After: Name: {after.name}, Topic: {after.topic}, Position: {after.position}')