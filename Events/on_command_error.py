from discord.ext import commands

class OnCommandError:
    @staticmethod
    async def on_command_error(ctx, error):
        """
        Triggered when a command raises an error.

        Parameters:
        - ctx (commands.Context): The context in which the command was invoked.
        - error (commands.CommandError): The error raised by the command.
        """
        # Log the error for debugging purposes
        # print(f'on_command_error {ctx.command}: {error}')

        # Example error handling
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Sorry, that command does not exist.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing argument: {error.param.name}. Please provide it.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument. Please check your input.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have permission to use this command.")
        else:
            await ctx.send("An error occurred while processing the command.")
        
        print(f"on_command_error {ctx.command}: {error}")