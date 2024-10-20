# ...

class OnMessageBulkDelete:
    @staticmethod
    async def on_message_bulk_delete(messages):
        """
        Triggered when multiple messages are deleted simultaneously.

        Parameters:
        - messages (List[discord.Message]): The list of messages that were deleted.
        """
        print(f'{len(messages)} messages were bulk deleted in {messages[0].channel.name} (ID: {messages[0].channel.id}).')