# ...

class OnInviteCreate:
    @staticmethod
    async def on_invite_create(invite):
        """
        Triggered when an invite is created.

        Parameters:
        - invite (discord.Invite): The invite that was created.
        """
        print(f'Invite created: {invite.code} (Channel: {invite.channel.name})')