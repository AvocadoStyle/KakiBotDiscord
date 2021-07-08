import discord
import DICT

if __name__ == '__main__':
    client = discord.Client()
    @client.event
    async def on_ready():
        print('Logged on as {0}!'.format(client.user))

    @client.event
    async def on_message(message):
        if message.content.startswith('$greet'):
            channel = message.channel
            await channel.send('Say hello!')
        if message.content.startswith('$thumb'):
            channel = message.channel
            await channel.send('Send me that 👍 reaction, mate')


    @client.event
    async def on_member_join(member):
        print(f'{member} has joined the server')


    @client.event
    async def on_member_remove(member):
        print(f'{member} has left the server')


    client.run(DICT.T["TOKEN"])


#TOKEN: ODYyMzkwNDIwMDg3NzY3MDgw.YOXpqg.-DxFz3xREzdxuEm2AP1b8lmgbSY