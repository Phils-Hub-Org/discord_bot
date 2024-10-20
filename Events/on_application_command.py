# ...

class OnApplicationCommand:
    @staticmethod
    async def on_application_command(command):
        """
        Triggered when an application command is executed.

        Parameters:
        - command (discord.ApplicationCommand): The command that was executed.
        """
        print(f'Application command executed: {command.name}')