import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import datetime

client = commands.Bot(command_prefix = "!", case_insensitive = True)

@client.event
async def on_ready():
  print('The Bot "{0.user}" is ready to use.' .format(client))

####################################################### Help Command #######################################################
@client.command()
async def helps(ctx):
	embed = discord.Embed(title="❗ Command List", description="👑 System Account Details", color=discord.Color.blue())
	embed.set_footer(text="Create by: Canato#1177")
	await ctx.send(embed=embed)

###################################################### Account Details ######################################################
@client.command()
async def account(ctx):
	embed = discord.Embed(title="👑 Account Details", color=discord.Color.red())
	embed.add_field(name=f"```Name: {ctx.author.name}```", value=f"```ID: {ctx.author.id}```", inline=False)
	embed.add_field(name=f"```Status: {ctx.author.status}```", value=f"```Boosted: {ctx.author.premium_since}```", inline=False)
	embed.add_field(name=f"```IP: {ip}```", value=f"```City: {city}```", inline=False)
	embed.add_field(name=f"```Region: {region}```", value=f"```Country: {contry}```", inline=False)
	embed.add_field(name=f"```Postal Code: {postal}```", value=f"```Currency: {currency}```", inline=False)
	embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
	embed.set_footer(text="Create by: Canato#1177")
	await ctx.send(embed=embed)

###################################################### Def´s ######################################################

#IP
def ipget():
    ip = "None"
    try:
        ip = urlopen(Request("https://ipapi.co/ip")).read().decode().strip()
    except Exception as e:
        print(e)
        pass
    return ip

# City
def cityget():
	city = "None"
	try:
		city = urlopen(Request("https://ipapi.co/city")).read().decode().strip()
	except Exception as e:
		print(e)
		pass
	return city

# Region
def regionget():
	region = "None"
	try:
		region = urlopen(Request("https://ipapi.co/region")).read().decode().strip()
	except Exception as e:
		print(e)
		pass
	return region

# Contry
def contryget():
	contry = "None"
	try:
		contry = urlopen(Request("https://ipapi.co/country")).read().decode().strip()
	except Exception as e:
		print(e)
		pass
	return contry

# Postal Code
def postalget():
	postal = "None"
	try:
		postal = urlopen(Request("https://ipapi.co/postal")).read().decode().strip()
	except Exception as e:
		print(e)
		pass
	return postal

# Currency
def currencyget():
	currency = "None"
	try:
		currency = urlopen(Request("https://ipapi.co/currency")).read().decode().strip()
	except Exception as e:
		print(e)
		pass
	return currency

ip = ipget()
city = cityget()
region = regionget()
contry = contryget()
postal = postalget()
currency = currencyget()

client.run('TOKEN')