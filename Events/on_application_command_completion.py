# ...

class OnApplicationCommandCompletion:
    @staticmethod
    async def on_application_command_completion(command):
        """
        Triggered when an application command completes execution.

        Parameters:
        - command (discord.ApplicationCommand): The command that completed.
        """
        print(f'Application command completed: {command.name}')