# ...

class OnWebhookUpdate:
    @staticmethod
    async def on_webhook_update(channel):
        """
        Triggered when a webhook is updated in a channel.

        Parameters:
        - channel (discord.Channel): The channel where the webhook was updated.
        """
        print(f'Webhook updated in channel: {channel.name} (ID: {channel.id})')