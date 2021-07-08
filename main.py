import discord
import DICT
from bots import MyClient

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.members = True

    client = MyClient(intents=intents)
    client.run(DICT.T["TOKEN"])


#TOKEN: ODYyMzkwNDIwMDg3NzY3MDgw.YOXpqg.-DxFz3xREzdxuEm2AP1b8lmgbSY