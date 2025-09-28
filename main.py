import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="", intents=intents)

secret_role = "developer"

@bot.event
async def on_ready():
    print(f"estamos listos para empezar, {bot.user.name} ")


@bot.event
async def on_member_join(member):
    await member.send(f"bienvenido al servidor, {member.name}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} no uses esa palabra!")

    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send(f"hola {ctx.author.mention}! ")


@bot.command()
async def assing(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} el rol de {secret_role} se te ha asignado")
    else:
        await ctx.send("Este rol no existe")


@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} el rol de {secret_role} te ha sido removido")
    else:
        await ctx.send("Este rol no existe")


@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send("Bienvenido al club")


@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Tú no tienes permiso para esto")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
