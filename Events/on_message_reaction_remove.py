# ...

class OnMessageReactionRemove:
    @staticmethod
    async def on_message_reaction_remove(reaction, user):
        """
        Triggered when a user removes a reaction from a message.

        Parameters:
        - reaction (discord.Reaction): The reaction that was removed.
        - user (discord.User): The user who removed the reaction.
        """
        print(f'Message reaction removed: {reaction.emoji} by {user.name} (ID: {user.id})')