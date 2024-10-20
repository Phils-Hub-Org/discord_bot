from Components.bot import bot

class OnReactionRemove:
    @staticmethod
    async def on_reaction_remove(reaction, user):
        """
        Triggered when a reaction is removed from a message.

        Parameters:
        - reaction (discord.Reaction): The reaction that was removed.
        - user (discord.User): The user who removed the reaction.
        """
        print(f'Reaction removed: {reaction.emoji} by {user.name} (ID: {user.id})')

        if user == bot.user:
            return  # Ignore the bot's own reactions
        
        print(f'{user.name} removed {reaction.emoji} from the message: "{reaction.message.content}"')