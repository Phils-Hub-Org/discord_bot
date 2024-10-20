# ...

class OnGuildRoleUpdate:
    @staticmethod
    async def on_guild_role_update(before, after):
        """
        Triggered when a role is updated.

        Parameters:
        - before (discord.Role): The role before the update.
        - after (discord.Role): The role after the update.
        """
        print(f'Role updated: {before.name} (ID: {before.id})')
        print(f'Before: {before.permissions}, Color: {before.color}')
        print(f'After: {after.permissions}, Color: {after.color}')