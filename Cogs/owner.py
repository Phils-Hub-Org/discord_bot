import discord
from discord.ext import commands

class GuildOwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setwelcome')
    @commands.is_owner()  # Ensures that only the guild owner can use this command
    async def set_welcome(self, ctx, *, message: str):
        # This would typically involve saving the message to a database or file
        # Here we'll just simulate saving it with a print statement
        await ctx.send(f"Welcome message set to: {message}")

    # @commands.command(name='kick')
    # @commands.has_permissions(kick_members=True)  # Ensure the user has permission to kick members
    # async def kick_member(self, ctx, member: commands.MemberConverter):
    #     # await member.kick(reason="Kicked by the guild owner.")
    #     await ctx.send(f"{member.name} has been kicked from the guild.")
    
    @commands.command(name='giverole')
    @commands.has_permissions(manage_roles=True)
    async def give_role(self, ctx, user: discord.Member, *, role_to_assign: str):
        # Get the roles for reference    
        owner_id = ctx.guild.owner_id  # Get the server owner's ID
        admin_role = discord.utils.get(ctx.guild.roles, name="Administrator")
        mod_role = discord.utils.get(ctx.guild.roles, name="Moderator")

        # Name of the role to assign
        role = discord.utils.get(ctx.guild.roles, name=role_to_assign)

        # print(role.position)  # 14
        # print(admin_role.position)  # 17
        # print(mod_role.position)  # 16

        if role:
            # Check if the author is the server owner
            if ctx.author.id == owner_id:
                # The server owner can assign any role
                await user.add_roles(role)
                # await ctx.send(f"{user.mention} has been given the role {role.name} by the server owner {ctx.author.mention}")
                return

            # Check if the author has the admin role
            elif admin_role in ctx.author.roles:
                # Admins cannot assign the Admin role or any higher roles
                if role.position >= admin_role.position:
                    await ctx.send("You cannot assign this role (it's equal to or higher than the Admin role).")
                    return
                
                # Assign the role to the mentioned user
                await user.add_roles(role)
                await ctx.send(f"{user.mention} has been given the role {role.name} by {ctx.author.mention}")
                return

            # Check if the author has the moderator role
            elif mod_role in ctx.author.roles:
                # Moderators cannot assign the Moderator role or any higher roles
                if role.position >= mod_role.position:
                    await ctx.send("You cannot assign this role (it's equal to or higher than your own role).")
                    return
                
                # Assign the role to the mentioned user
                await user.add_roles(role)
                await ctx.send(f"{user.mention} has been given the role {role.name} by {ctx.author.mention}")
                return

        await ctx.send("Role not found!")

    @commands.command(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx):
        """Purges all messages in the channel where the command is invoked."""
        
        # Get the channel where the command was invoked
        channel = ctx.channel

        # Check if the user is a server owner or has a specific role
        owner_id = ctx.guild.owner_id
        admin_role = discord.utils.get(ctx.guild.roles, name="Administrator")
        mod_role = discord.utils.get(ctx.guild.roles, name="Moderator")
        
        # Common purge function to delete all messages (up to 14 days old)
        async def perform_purge():
            deleted = await channel.purge(limit=None)  # Specify limit=None to remove all messages
            await ctx.send(f"Deleted {len(deleted)} message(s) in {channel.mention}.")

        # Check if the author is the server owner
        if ctx.author.id == owner_id:
            await perform_purge()
            await ctx.send(f"All messages have been deleted by the server owner {ctx.author.mention}.")
            return

        # Check if the author has the admin role
        elif admin_role in ctx.author.roles:
            await perform_purge()
            await ctx.send(f"All messages have been deleted by {ctx.author.mention}.")
            return

        # Check if the author has the moderator role
        elif mod_role in ctx.author.roles:
            await perform_purge()
            await ctx.send(f"All messages have been deleted by {ctx.author.mention}.")
            return

        # If the user doesn't have permission
        await ctx.send("You do not have permission to purge messages in this channel.")

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, kick_messqage: str = "No reason provided."):
        """Kicks a member from the server."""
        if ctx.author.top_role <= user.top_role:
            await ctx.send(f"You cannot kick {user.mention} because they have a higher or equal role.")
            return
        await user.kick(reason=f"Kicked by {ctx.author}, reason: {kick_messqage}")
        await ctx.send(f"{ctx.author.mention} kicked {user.mention} from the server, reason: {kick_messqage}.")

    @commands.command(name='create-channel')
    @commands.has_permissions(manage_channels=True)
    async def create_channel(self, ctx, channel_name: str):
        """Creates a new text channel."""
        # Check if the channel already exists
        existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        if existing_channel:
            await ctx.send(f"A channel named '{channel_name}' already exists.")
            return

        # Create the new channel
        try:
            new_channel = await ctx.guild.create_text_channel(channel_name)
            await ctx.send(f"Channel '{new_channel.name}' has been created.")
        except discord.Forbidden:
            await ctx.send("I do not have permission to create a channel.")
        except discord.HTTPException:
            await ctx.send("An error occurred while creating the channel.")

    @commands.command(name='pin_message')
    @commands.has_permissions(manage_messages=True)
    async def pin_message(self, ctx, message_id: int):
        """Pins a message by its ID in the current channel."""
        try:
            # Fetch the message from the channel using its ID
            message = await ctx.channel.fetch_message(message_id)
            await message.pin()
            await ctx.send(f"Message by {message.author.mention} has been pinned.")
        except discord.NotFound:
            await ctx.send("Message not found. Please provide a valid message ID.")
        except discord.Forbidden:
            await ctx.send("I do not have permission to pin messages.")
        except discord.HTTPException:
            await ctx.send("An error occurred while pinning the message.")

async def setup(bot):
    print("Loading GuildOwnerCog...")
    await bot.add_cog(GuildOwnerCog(bot))