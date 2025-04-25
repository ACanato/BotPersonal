import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

async def get_data(url):
    loop = asyncio.get_event_loop()
    def fetch():
        try:
            return urlopen(Request(url)).read().decode().strip()
        except Exception as e:
            print(f"Erro ao pegar dados de {url}: {e}")
            return "Desconhecido"
    return await loop.run_in_executor(None, fetch)

@client.event
async def on_ready():
    print(f'O bot {client.user} está pronto e online!')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="❗ Lista de comandos", description="👑 Detalhes da conta do utilizador - !account", color=discord.Color.blue())
    embed.set_footer(text="Criado por: .swible")
    await ctx.send(embed=embed)

@client.command()
async def account(ctx):
    ip = await get_data("https://ipapi.co/ip")
    city = await get_data("https://ipapi.co/city")
    region = await get_data("https://ipapi.co/region")
    country = await get_data("https://ipapi.co/country_name")
    postal = await get_data("https://ipapi.co/postal")
    currency = await get_data("https://ipapi.co/currency")

    embed = discord.Embed(title="👑 Detalhes da Conta", color=discord.Color.red())
    embed.add_field(name="Nome", value=ctx.author.name, inline=False)
    embed.add_field(name="ID", value=ctx.author.id, inline=False)
    embed.add_field(name="Status", value=str(ctx.author.status), inline=False)
    embed.add_field(name="Boost", value=str(ctx.author.premium_since), inline=False)
    embed.add_field(name="IP", value=ip, inline=True)
    embed.add_field(name="Cidade", value=city, inline=True)
    embed.add_field(name="Região", value=region, inline=True)
    embed.add_field(name="País", value=country, inline=True)
    embed.add_field(name="Código Postal", value=postal, inline=True)
    embed.add_field(name="Moeda", value=currency, inline=True)
    embed.set_thumbnail(url=ctx.author.display_avatar.url)
    embed.set_footer(text="Criado por: .swible")

    await ctx.send(embed=embed)

client.run('TOKEN')