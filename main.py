import asyncio

from disnake import Intents
from disnake.ext.commands import Bot

from src.shared.config import akarichan_config

COGS = ['src.cogs.grant_role']

class AkariChan(Bot):
    def __init__(self, intents: Intents) -> None:
        super().__init__(intents=intents, sync_commands_debug=True)
        for cog in COGS:
            self.load_extension(cog)
    
    async def on_ready(self):
        print('Connected %s' % self.user.name)

async def main():
    intents: Intents = Intents.all()
    bot = AkariChan(intents=intents)
    await bot.start(akarichan_config.token)

if __name__ == '__main__':
    asyncio.run(main())
