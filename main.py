import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

dumb_words = ["dumb","stupid","idiot","mad","lunatic","pathetic","shit","unhappy","sad","fail"]

dumb_replies = ["Cheer Up! I am a result of a failed code,still working fine :)","The only stupid thing here is me","Hi i am DumbBOT, a bot who is ...... yeah you guessed it right.","I am idiot to join this server"]

if "responding" not in db.keys():
  db["responding"] = True

def update_replies(new_replies):
  if "dumb" in db.keys():
    dumb = db["dumb"]
    dumb.append(new_replies)
    db["dumb"] = dumb
  else:
    db["dumb"] = [new_replies]

def delete_replies(index):
  dumb = db["dumb"]
  if len(dumb) > index:
    del dumb[index]
    db["dumb"] = dumb

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content


  if db["responding"]:
    options = dumb_replies
    if "dumb" in db.keys():
      options = options + db["dumb"]

    if any(word in msg for word in dumb_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$newreply"):
    new_replies = msg.split("$newreply ",1)[1]
    update_replies(new_replies)
    await message.channel.send("dumb reply added successfully")
    
  if msg.startswith("hi"):
    await message.channel.send('Hi! i am DumbBOT created by Ranveer for testing purpose')

  if msg.startswith("$delreply"):
    dumb = []
    if "dumb" in db.keys():
      index = int(msg.split("$delreply",1)[1])
      delete_replies(index)
      dumb = db["dumb"]
    await message.channel.send(dumb)

  if msg.startswith("$list"):
    dumb = []
    if "dumb" in db.keys():
      dumb = db["dumb"]
    await message.channel.send(dumb)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive()
client.run(os.getenv('TOKEN'))
