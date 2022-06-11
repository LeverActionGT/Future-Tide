#Sahil

print(' \nLoading...\n')

#libraries
from email import message
from pydoc import describe
import nextcord
import datetime as dt
import numpy as np
import sys

from pandas import describe_option

#modules
import modules.token_reader as token_reader
import modules.location_information as location_information

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
    print(location)
    msg = f'**{label}**\nLatitude: {lat}\nLongitude: {lon}\nElevation: {elev}'
    await inter.response.send_message(msg)

client.run(discord_token)