print(' \nLoading...\n')

#libraries
import nextcord
import datetime as dt
import numpy as np
import sys

#modules
import modules.token_reader as token_reader
import modules.RishitTesting as rishittesting

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
@client.slash_command()
async def ping(inter: nextcord.Interaction) -> None:
    msg = f'Pong: {round(client.latency*1000)}ms'
    await inter.response.send_message(msg)

client.run(discord_token)