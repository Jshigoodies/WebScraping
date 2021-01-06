import discord
from discord.ext import commands, tasks
import random

token = "NzkxODE1ODM4OTIyNDQwNzI1.X-Up9w.GeRNP1yWfzeBSRj7lpqrzCd7cFw"

client = commands.Bot(command_prefix= ".")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(aliases=["h"])
async def _help(ctx):
    await ctx.send("h (help), ping, 8ball, join <- joins vc, leave <- leaves vc, clear (deletes the message above it), kick, ban, unban")

status = ["Dead", "I feel the power of Anime", ":D :D :D"]

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, question):
    responses = ["no", "yes", "maybe"]
    await ctx.send(f"Question: {question}\nAnswser: {random.choice(responses)}")


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.command()
async def kick(ctx, member: discord.Member, *,
               reason=None):  # the '*' is so you can make the reason a sentence instead of a single word after taking in the arguemnts of the command name and discord member
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_id = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_id):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.name}#{user.discriminator}. Very sorry {user.mention}")
            break

client.run(token)