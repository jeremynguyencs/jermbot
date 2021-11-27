import discord
import os
import requests
import json
import random

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "u r such a king/queen/monarch",
  "hang in there u got this",
  "ur a great person man"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = (json_data[0]['q']).lower()
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.lower()

  if msg.startswith('@quote'):
    quote = "wise man once said " + get_quote()
    await message.channel.send(quote)
    
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if "thank" in msg and "jerm bot" in msg or "jermbot" in msg:
    await message.channel.send("np")

  if msg.startswith('@repeat '):
    await message.channel.send(msg.replace('@repeat ', ""))

  if msg.startswith('gn') or msg.startswith('good night'):
    await message.channel.send('gn')

client.run(os.getenv('TOKEN'))