# ...

class OnGuildRoleCreate:
    @staticmethod
    async def on_guild_role_create(role):
        """
        Triggered when a new role is created.

        Parameters:
        - role (discord.Role): The role that has been created.
        """
        print(f'Role created: {role.name} (ID: {role.id})')