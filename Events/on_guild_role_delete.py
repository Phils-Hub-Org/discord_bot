# ...

class OnGuildRoleDelete:
    @staticmethod
    async def on_guild_role_delete(role):
        """
        Triggered when a role is deleted.

        Parameters:
        - role (discord.Role): The role that has been deleted.
        """
        print(f'Role deleted: {role.name} (ID: {role.id})')