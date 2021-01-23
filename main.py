client=discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  if message.content.startswith("hi"):
    await message.channel.send('Hi! i am created by Ranveer Shah for testing purpose')

client.run(os.getenv('TOKEN'))
