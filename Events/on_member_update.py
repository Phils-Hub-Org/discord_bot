# ...

class OnMemberUpdate:
    @staticmethod
    async def on_member_update(before, after):
        """
        Triggered when a member updates their profile or roles.

        Parameters:
        - before (discord.Member): The member before the update.
        - after (discord.Member): The member after the update.
        """
        print(f'Member updated: {before.name} (ID: {before.id})')