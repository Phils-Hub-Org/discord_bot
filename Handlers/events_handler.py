"""
Events are triggered by actions within Discord, allowing your bot to respond to various occurrences in real-time.
Here are some common events:

    on_ready: # Triggered when the bot is ready and fully connected to the Discord API.

    on_message: Triggered when a new message is sent in a text channel the bot can access.
    on_message_edit: Triggered when a message is edited in a text channel the bot can access.
    on_message_delete: Triggered when a message is deleted in a text channel the bot can access.
    on_message_bulk_delete: Triggered when multiple messages are deleted at once in a text channel.

    on_member_join: Triggered when a new member joins a guild the bot is in.
    on_member_remove: Triggered when a member leaves, is kicked, or banned from a guild the bot is in.
    on_member_update: Triggered when a member's status or details (like roles or nickname) are updated.
    on_member_ban(guild, user): Called when a member is banned from a guild.
    on_member_unban(guild, user): Called when a member is unbanned from a guild.

    on_reaction_add: Triggered when a reaction is added to a message in a text channel.
    on_reaction_remove: Triggered when a reaction is removed from a message in a text channel.

    on_message_reaction_add: Triggered when a reaction is added to a specific message.
    on_message_reaction_remove: Triggered when a reaction is removed from a specific message.

    on_guild_join: Triggered when the bot joins a new guild.
    on_guild_remove: Triggered when the bot is removed from a guild.
    on_guild_update: Triggered when a guild's details (like name or region) are updated.

    on_voice_state_update: Triggered when a user's voice state (like joining, leaving, or moving voice channels) is updated.

    on_channel_create: Triggered when a new channel is created in a guild.
    on_channel_delete: Triggered when a channel is deleted in a guild.
    on_channel_update: Triggered when a channel's details (like name or permissions) are updated.

    on_guild_role_create: Triggered when a new role is created in a guild.
    on_guild_role_delete: Triggered when a role is deleted from a guild.
    on_guild_role_update: Triggered when a role's details (like name or permissions) are updated.

    on_typing: Triggered when someone starts typing in a channel.

    on_error: Triggered when an error occurs while processing any event.
    on_command_error: Triggered when an error occurs during command execution.

    on_application_command: Triggered when a new application command (slash command) is created.
    on_application_command_completion: Triggered when an application command (slash command) is successfully completed.

    on_invite_create: Triggered when a new invite is created in a guild.
    on_invite_delete: Triggered when an invite is deleted in a guild.

    on_user_update: Triggered when a user's details (like username or avatar) are updated.

    on_guild_sticker_create: Triggered when a new sticker is created in a guild.
    on_guild_sticker_delete: Triggered when a sticker is deleted from a guild.
    on_guild_sticker_update: Triggered when a sticker's details are updated in a guild.

    on_scheduled_event_create: Triggered when a scheduled event is created in a guild.
    on_scheduled_event_update: Triggered when a scheduled event in a guild is updated.
    on_scheduled_event_delete: Triggered when a scheduled event is deleted from a guild.
"""

from Events.on_ready import OnReady

from Events.on_message import OnMessage
from Events.on_message_edit import OnMessageEdit
from Events.on_message_delete import OnMessageDelete
from Events.on_message_bulk_delete import OnMessageBulkDelete

from Events.on_member_join import OnMemberJoin
from Events.on_member_remove import OnMemberRemove
from Events.on_member_update import OnMemberUpdate

from Events.on_reaction_add import OnReactionAdd
from Events.on_reaction_remove import OnReactionRemove

from Events.on_message_reaction_add import OnMessageReactionAdd
from Events.on_message_reaction_remove import OnMessageReactionRemove

from Events.on_guild_join import OnGuildJoin
from Events.on_guild_remove import OnGuildRemove
from Events.on_guild_update import OnGuildUpdate

from Events.on_voice_state_update import OnVoiceStateUpdate

from Events.on_channel_create import OnChannelCreate
from Events.on_channel_delete import OnChannelDelete
from Events.on_channel_update import OnChannelUpdate

from Events.on_guild_role_create import OnGuildRoleCreate
from Events.on_guild_role_delete import OnGuildRoleDelete
from Events.on_guild_role_update import OnGuildRoleUpdate

from Events.on_typing import OnTyping

from Events.on_error import OnError
from Events.on_command_error import OnCommandError

from Events.on_application_command import OnApplicationCommand
from Events.on_application_command_completion import OnApplicationCommandCompletion

from Events.on_integration_create import OnIntegrationCreate
from Events.on_integration_delete import OnIntegrationDelete
from Events.on_integration_update import OnIntegrationUpdate

from Events.on_webhook_update import OnWebhookUpdate

from Events.on_invite_create import OnInviteCreate
from Events.on_invite_delete import OnInviteDelete

from Events.on_user_update import OnUserUpdate

from Events.on_guild_sticker_create import OnGuildStickerCreate
from Events.on_guild_sticker_delete import OnGuildStickerDelete
from Events.on_guild_sticker_update import OnGuildStickerUpdate

from Events.on_scheduled_event_create import OnScheduledEventCreate
from Events.on_scheduled_event_update import OnScheduledEventUpdate
from Events.on_scheduled_event_delete import OnScheduledEventDelete

from Components.bot import bot

class EventsHandler:

    class OnReadyHandler:
        @bot.event
        async def on_ready():
            print("You're all set!")
            await OnReady.on_ready()

    class OnMessageHandler:
        @bot.event
        async def on_message(message):
            await OnMessage.on_message(message)

        @bot.event
        async def on_message_edit(before, after):
            await OnMessageEdit.on_message_edit(before, after)

        @bot.event
        async def on_message_delete(message):
            await OnMessageDelete.on_message_delete(message)

        @bot.event
        async def on_message_bulk_delete(messages):
            await OnMessageBulkDelete.on_message_bulk_delete(messages)

    class OnMemberHandler:
        @bot.event
        async def on_member_join(member):
            await OnMemberJoin.on_member_join(member)

        @bot.event
        async def on_member_remove(member):
            await OnMemberRemove.on_member_remove(member)

        @bot.event
        async def on_member_update(before, after):
            await OnMemberUpdate.on_member_update(before, after)

    class OnReactionHandler:
        @bot.event
        async def on_reaction_add(reaction, user):
            await OnReactionAdd.on_reaction_add(reaction, user)

        @bot.event
        async def on_reaction_remove(reaction, user):
            await OnReactionRemove.on_reaction_remove(reaction, user)
        
        @bot.event
        async def on_message_reaction_add(message, reaction):
            await OnMessageReactionAdd.on_message_reaction_add(message, reaction)
        
        @bot.event
        async def on_message_reaction_remove(message, reaction):
            await OnMessageReactionRemove.on_message_reaction_remove(message, reaction)

    class OnGuildHandler:
        @bot.event
        async def on_guild_join(guild):
            await OnGuildJoin.on_guild_join(guild)

        @bot.event
        async def on_guild_remove(guild):
            await OnGuildRemove.on_guild_remove(guild)

        @bot.event
        async def on_guild_update(before, after):
            await OnGuildUpdate.on_guild_update(before, after)

    class OnVoiceStateHandler:
        @bot.event
        async def on_voice_state_update(member, before, after):
            await OnVoiceStateUpdate.on_voice_state_update(member, before, after)

    class OnChannelHandler:
        @bot.event
        async def on_channel_create(channel):
            await OnChannelCreate.on_channel_create(channel)

        @bot.event
        async def on_channel_delete(channel):
            await OnChannelDelete.on_channel_delete(channel)

        @bot.event
        async def on_channel_update(before, after):
            await OnChannelUpdate.on_channel_update(before, after)

    class OnGuildRoleHandler:
        @bot.event
        async def on_guild_role_create(role):
            await OnGuildRoleCreate.on_guild_role_create(role)

        @bot.event
        async def on_guild_role_delete(role):
            await OnGuildRoleDelete.on_role_delete(role)

        @bot.event
        async def on_guild_role_update(before, after):
            await OnGuildRoleUpdate.on_role_update(before, after)

    class OnTypingHandler:
        @bot.event
        async def on_typing(channel, user, when):
            await OnTyping.on_typing(channel, user, when)

    class OnErrorHandler:
        @bot.event
        async def on_error(event, *args, **kwargs):
            await OnError.on_error(event, *args, **kwargs)
        
        @bot.event
        async def on_command_error(ctx, error):
            await OnCommandError.on_command_error(ctx, error)

    class OnApplicationCommandHandler:
        @bot.event
        async def on_application_command(command):
            await OnApplicationCommand.on_application_command(command)

        @bot.event
        async def on_application_command_completion(command):
            await OnApplicationCommandCompletion.on_application_command_completion(command)

    class OnIntegrationHandler:
        @bot.event
        async def on_integration_create(integration):
            await OnIntegrationCreate.on_integration_create(integration)

        @bot.event
        async def on_integration_delete(integration):
            await OnIntegrationDelete.on_integration_delete(integration)

        @bot.event
        async def on_integration_update(integration):
            await OnIntegrationUpdate.on_integration_update(integration)

    class OnWebhookHandler:
        @bot.event
        async def on_webhook_update(channel):
            await OnWebhookUpdate.on_webhook_update(channel)

    class OnInviteHandler:
        @bot.event
        async def on_invite_create(invite):
            await OnInviteCreate.on_invite_create(invite)

        @bot.event
        async def on_invite_delete(invite):
            await OnInviteDelete.on_invite_delete(invite)

    class OnUserHandler:
        @bot.event
        async def on_user_update(before, after):
            await OnUserUpdate.on_user_update(before, after)

    class OnGuildStickerHandler:
        @bot.event
        async def on_guild_sticker_create(sticker):
            await OnGuildStickerCreate.on_guild_sticker_create(sticker)

        @bot.event
        async def on_guild_sticker_delete(sticker):
            await OnGuildStickerDelete.on_guild_sticker_delete(sticker)

        @bot.event
        async def on_guild_sticker_update(before, after):
            await OnGuildStickerUpdate.on_guild_sticker_update(before, after)

    class OnScheduledEventHandler:
        @bot.event
        async def on_scheduled_event_create(event):
            await OnScheduledEventCreate.on_scheduled_event_create(event)

        @bot.event
        async def on_scheduled_event_update(before, after):
            await OnScheduledEventUpdate.on_scheduled_event_update(before, after)

        @bot.event
        async def on_scheduled_event_delete(event):
            await OnScheduledEventDelete.on_scheduled_event_delete(event)
