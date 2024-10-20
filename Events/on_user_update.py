# ...

class OnUserUpdate:
    @staticmethod
    async def on_user_update(before, after):
        """
        Triggered when a user updates their profile.

        Parameters:
        - before (discord.User): The user before the update.
        - after (discord.User): The user after the update.
        """
        print(f'User updated: {before.name} (ID: {before.id})')