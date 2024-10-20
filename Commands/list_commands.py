from Components.bot import bot

# List available commands

COMMAND_LIST = [
    "!hello - Responds with a greeting.\n\tWho: Anyone\n",
    "!greet @user - Greets a user by mentioning them.\n\tWho: Anyone\n",
    "!dogmeme - Sends a random dog meme.\n\tWho: Anyone\n",
    "!randmeme - Sends a random meme.\n\tWho: Anyone\n",
    "!randsong - Sends a random song.\n\tWho: Anyone\n",
    "!randtrailor - Sends a random movie/series trailer.\n\tWho: Anyone\n",
    "!poll [question] [delimiter] [emojis] Sends a poll with the given question and reactions (limit 5).\n\tExample: `!poll question | :emoji1: :emoji2: ...`\n\tWho: Anyone\n",
    "!codeinfo [language] [code] - Sends the code with the given language.\n\tExample: `!codeinfo gsc function`\n\tWho: Anyone\n",
    "!giverole @user [role] - Gives a role to a user.\n\tExample: `!giverole @user Administrator`\n\tWho: Moderators +\n",
    "!purge - Purges all messages in the channel where the command is invoked.\n\tExample: `!purge`\n\tWho: Moderators +\n",
    "!kick @user [reason] - Kicks a user from the server.\n\tExample: `!kick @user`.\n\tWho: Moderators +\n",
    "!create_channel [channel_name] - Creates a new text channel\n\tExample: `!create_channel new_channel`.\n\tWho: Moderators +\n",
    "!pin_message [message_id] - Pins a message by its ID in the current channel\n\tExample: `!pin_message 123456789`.\n\tWho: Moderators +\n",
]

class ListCommands:
    @staticmethod
    async def list_commands(ctx):
        response = "Here are the available commands:\n"
        response += "\n".join(bot.commands)
        await ctx.send(response)