# ...

class OnMessageEdit:
    @staticmethod
    async def on_message_edit(before, after):
        """
        Triggered when a message is edited.

        Parameters:
        - before (discord.Message): The message before it was edited.
        - after (discord.Message): The message after it was edited.
        """
        print(f'Message edited in {before.channel.name} (ID: {before.channel.id}).')
        print(f'Before: {before.content}')
        print(f'After: {after.content}')