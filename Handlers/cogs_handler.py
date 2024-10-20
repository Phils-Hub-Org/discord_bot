"""
Commands
Commands are actions that users can invoke via chat messages. They allow for interactive functionality in your bot.
    @commands.has_role(role): Checks if the user invoking the command has a specific role. This ensures that only users with the appropriate roles can execute certain commands.
    @commands.has_any_role(*roles): Checks if the user has any of the specified roles. Useful for commands that should be accessible to multiple roles.

    @commands.is_owner(): Checks if the user invoking the command is the owner of the bot. This is ideal for commands that should be restricted to the bot owner only.
    @commands.guild_only(): Ensures that the command can only be used within a server (guild) and not in direct messages (DMs). This is useful for commands that rely on server-specific data.
    @commands.dm_only(): Restricts a command to be used only in direct messages, preventing usage in guild channels.

    @commands.has_permissions(permissions): Validates if the user has the required permissions (e.g., manage_channels, kick_members) to execute the command.
    @commands.bot_has_permissions(permissions): Checks if the bot itself has the necessary permissions to perform a command. This prevents errors when the bot tries to execute a command without the required permissions.
    
    @commands.cooldown(rate, per, BucketType): Limits how frequently a command can be used. For instance, you can set a command to allow one use per user every 30 seconds to prevent spam.

Error Handling
Error Handlers: Customize how your bot responds to errors that occur during command execution. You can define global error handlers or specific error handling for individual commands.

Common Errors:
    commands.MissingRequiredArgument: Raised when a required argument is not provided.
    commands.CommandNotFound: Raised when a command does not exist.

Permissions
    Type 1: Decorator
        @commands.has_permissions(administrator=True): Check if the user executing the command has administrator permissions.
    
    Type 2: Attribute
        ctx.author.guild_permissions.administrator: Check if the user executing the command has administrator permissions.

        ctx.author.guild_permissions.kick_members: Check if the user executing the command has the kick_members permission.
        ctx.author.guild_permissions.ban_members: Check if the user executing the command has the ban_members permission.

        ctx.author.guild_permissions.manage_roles: Check if the user executing the command has the manage_roles permission.
        ctx.author.guild_permissions.manage_channels: Check if the user executing the command has the manage_channels permission.
        ctx.author.guild_permissions.manage_messages: Check if the user executing the command has the manage_messages permission.
"""

from Components.bot import bot

class CogsHandler:
    @staticmethod
    async def initialize():
        await bot.load_extension('Cogs.everyone')
        await bot.load_extension('Cogs.moderator')
        await bot.load_extension('Cogs.administrator')
        await bot.load_extension('Cogs.owner')