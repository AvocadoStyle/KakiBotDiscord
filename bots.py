import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('$greet'):
            channel = message.channel
            await channel.send('Say hello!')
        if message.content.startswith('$thumb'):
            channel = message.channel
            await channel.send('Send me that 👍 reaction, mate')
