# ...

class OnIntegrationDelete:
    @staticmethod
    async def on_integration_delete(integration):
        """
        Triggered when an integration is deleted.

        Parameters:
        - integration (discord.Integration): The integration that was deleted.
        """
        print(f'Integration deleted: {integration.name} (ID: {integration.id})')