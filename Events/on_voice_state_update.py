# ...

class OnVoiceStateUpdate:
    @staticmethod
    async def on_voice_state_update(member, before, after):
        """
        Triggered when a user's voice state changes.

        Parameters:
        - member (discord.Member): The member whose voice state has changed.
        - before (discord.VoiceState): The voice state before the change.
        - after (discord.VoiceState): The voice state after the change.
        """
        print(f'{member.name} (ID: {member.id}) has changed their voice state.')
        
        if before.channel is None and after.channel is not None:
            await OnVoiceStateUpdate.joinedVoiceChannel(member, before, after)
        elif before.channel is not None and after.channel is None:
            await OnVoiceStateUpdate.leftVoiceChannel(member, before, after)
        elif before.channel is not None and after.channel is not None and before.channel != after.channel:
            await OnVoiceStateUpdate.changedVoiceChannel(member, before, after)

    @staticmethod
    async def joinedVoiceChannel(member, before, after):
        print(f'Joined voice channel: {after.channel.name} (ID: {after.channel.id})')
    
    @staticmethod
    async def leftVoiceChannel(member, before, after):
        print(f'Left voice channel: {before.channel.name} (ID: {before.channel.id})')
    
    @staticmethod
    async def changedVoiceChannel(member, before, after):
        print(f'Changed voice channel: {before.channel.name} (ID: {before.channel.id}) -> {after.channel.name} (ID: {after.channel.id})')