# ...

class OnMessage:
    @staticmethod
    async def on_message(message):
        """
        Triggered when a message is received.

        Parameters:
        - message (discord.Message): The message that was received.
        """
        print(f'Message received in {message.channel.name} (ID: {message.channel.id}).')
        print(f'Content: {message.content}')