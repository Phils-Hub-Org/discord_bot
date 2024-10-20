# ...

class OnMemberRemove:
    @staticmethod
    async def on_member_remove(member):
        """
        Triggered when a member leaves the guild.

        Parameters:
        - member (discord.Member): The member who left the guild.
        """
        print(f'Member left: {member.name} (ID: {member.id})')