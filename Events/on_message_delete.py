# ...

class OnMessageDelete:
    @staticmethod
    async def on_message_delete(message):
        """
        Triggered when a message is deleted.

        Parameters:
        - message (discord.Message): The message that has been deleted.
        """
        print(f'Message deleted in {message.channel.name} (ID: {message.channel.id}): {message.content}')