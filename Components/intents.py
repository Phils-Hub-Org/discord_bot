"""
List of Intents
Intents.default(): This will enable the basic intents that are commonly required. It includes:

Guilds: Receive guild-related events.
Guild Messages: Receive message events in guilds (servers).
Guild Message Reactions: Receive reaction events in guild messages.
Guild Members: Receive member-related events.
Intents.all(): This enables all intents, including those that may not be necessary for your bot but could be useful depending on its functionality:

guilds: Allows access to guild-related events.
members: Allows access to member-related events (user presence, join, leave).
messages: Allows access to message events (send, edit, delete).
message_reactions: Allows access to message reaction events (add, remove).
voice_states: Allows access to voice state events (join, leave, mute).
presences: Allows access to presence updates for members (online, offline, etc.).
guild_integrations: Allows access to guild integration events.
guild_webhooks: Allows access to webhook events in guilds.
invites: Allows access to invite-related events.
dm_messages: Allows access to direct message events.
dm_reactions: Allows access to reactions in direct messages.
dm_typing: Allows access to typing indicators in direct messages.
guild_typing: Allows access to typing indicators in guilds.
guild_bans: Allows access to ban-related events.
guild_emojis: Allows access to emoji-related events in guilds.
guild_stickers: Allows access to sticker-related events in guilds.
guild_scheduled_events: Allows access to scheduled events in guilds.
"""

import discord

class Intents:
    
    intents = discord.Intents.all()  # Enable all intents