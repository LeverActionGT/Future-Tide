#Sahil

print(' \nLoading...\n')

#libraries
from email import message
from pydoc import describe
from re import A
import nextcord
import datetime as dt
import numpy as np
import sys

from pandas import describe_option

#modules
import modules.token_reader as token_reader
import modules.location_information as location_information
import modules.DistanceToShore as distance_to_shore

#token setup
discord_token = token_reader.tokens()['discord']

#bot setup
client = nextcord.Client()
crd = sys.path[0]

# bot ready
@client.event
async def on_ready():
    logValue = f'Bot Running as {client.user}'
    logValue2 = f'Ping: {round(client.latency*1000)}ms'
    print(f'{logValue}\n{logValue2}\n--- ')

#ping command
@client.slash_command(name='ping', description='Ping bot latency')
async def ping(inter: nextcord.Interaction) -> None:
    msg = f'Pong: {round(client.latency*1000)}ms'
    await inter.response.send_message(msg)

#info command
@client.slash_command(name='info', description='About the project and what it is intended to do')
async def info(inter: nextcord.Interaction) -> None:
    embedVar = nextcord.Embed(title='__**Info**__', color=0x26d0ea)
    embedVar.add_field(name='Our mission', value='Future Tide is a discord bot that we created to raise awareness about sea-level rise. This bot allows the user to input any address in the world and it will calculate the number of years it would take for that location to be totally submerged in water at the current pace of sea-level rise. It will also output the same metric but if the temperature is 3°C lower each year so that the user can compare the effects that even a small decrease in temperature will have. The machine learning model and python backend can be adapted to connect to a web application, mobile app, or as a research tool.', inline=False)
    await inter.response.send_message(embed=embedVar)

@client.slash_command(name='geocode', description='Converts address to latitude, longitude, and elevation')
async def geocode(inter: nextcord.Interaction, address:str):
    
    #initialized location class
    location = location_information.Geocoding(address)
    lat = location.latitude
    lon = location.longitude
    elev = location.elevation
    label = location.label
    average_temp = location.avg_temp

    msg = f'**{label}**\nLatitude: {lat}\nLongitude: {lon}\nElevation: {elev}\nAverage Temp:{average_temp}'
    await inter.response.send_message(msg)


@client.slash_command(name='underwater', description='Determines how long until this locaton is underwater')
async def underwater(inter: nextcord.Interaction, address:str):
    location = location_information.Geocoding(address)
    x = location.elevation
    y = location.avg_temp
    label = location.label

    fx = (-4.96*10**(-10)) + (2.08*10**8)*x - 9383028*x**2 + 402*x**3  -0.264*x**4 + 1.11*10**(-4)*x**5 - (2.91*10**(-8))*x**6 + (4.36*10**(-12))*x**7 - (2.86*10**(-16))*x**8
    fy = 208 - 0.0232*x + (1.01+10**(-6))*x**2 - (1.91*10**(-11))*x**3 + (1.35*10**(-16))*x**4

    a = (1.43312*10**(-16))
    b = (0.00144564)

    z = a*fx+ b*fy

    shoredist = distance_to_shore.shore_distance(location.latitude, location.longitude)
    sdo = shoredist.output
    years = sdo*z

    msg = f'**{label}**\nWill be underwater in {years} years'
    await inter.response.send_message(msg)

client.run(discord_token)
