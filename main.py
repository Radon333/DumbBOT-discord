import discord
import os
import random

client=discord.Client()

dumb_words=["dumb","stupid","idiot","mad","lunatic","pathetic","shit","unhappy","sad","fail"]

dumb_replies=["Cheer Up! I am a result of a failed code,still working fine :)","The only stupid thing here is me","Hi i am DumbBOT, a bot who is ...... yeah you guessed it right.","I am idiot to join this server"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  msg=message.content

  if msg.startswith("hi"):
    await message.channel.send('Hi! i am DumbBOT created by Ranveer for testing purpose')
  if any(word in msg for word in dumb_words):
    await message.channel.send(random.choice(dumb_replies))

client.run(os.getenv('TOKEN'))
