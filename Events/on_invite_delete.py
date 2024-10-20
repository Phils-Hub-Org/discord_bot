# ...

class OnInviteDelete:
    @staticmethod
    async def on_invite_delete(invite):
        """
        Triggered when an invite is deleted.

        Parameters:
        - invite (discord.Invite): The invite that was deleted.
        """
        print(f'Invite deleted: {invite.code} (Channel: {invite.channel.name})')