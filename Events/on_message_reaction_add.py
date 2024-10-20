# ...

class OnMessageReactionAdd:
    @staticmethod
    async def on_message_reaction_add(reaction, user):
        """
        Triggered when a user adds a reaction to a message.

        Parameters:
        - reaction (discord.Reaction): The reaction that was added.
        - user (discord.User): The user who added the reaction.
        """
        print(f'Message reaction added: {reaction.emoji} by {user.name} (ID: {user.id})')