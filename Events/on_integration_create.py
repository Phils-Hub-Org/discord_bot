# ...

class OnIntegrationCreate:
    @staticmethod
    async def on_integration_create(integration):
        """
        Triggered when a new integration is created.

        Parameters:
        - integration (discord.Integration): The integration that was created.
        """
        print(f'Integration created: {integration.name} (ID: {integration.id})')