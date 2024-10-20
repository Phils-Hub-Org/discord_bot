from Components.bot import bot

class OnReactionAdd:
    @staticmethod
    async def on_reaction_add(reaction, user):
        """
        Triggered when a reaction is added to a message.

        Parameters:
        - reaction (discord.Reaction): The reaction that was added.
        - user (discord.User): The user who added the reaction.
        """
        print(f'Reaction added: {reaction.emoji} by {user.name} (ID: {user.id})')

        if user == bot.user:
            return  # Ignore the bot's own reactions
        
        print(f'{user.name} added {reaction.emoji} to the message: "{reaction.message.content}"')