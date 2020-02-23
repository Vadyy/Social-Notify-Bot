import discord
from discord.ext import commands

import sys, traceback

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['/', ' / ']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow / to be used in DMs
        return '/'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.simple',
                      'cogs.commands',
                      'cogs.owner']

bot = commands.Bot(command_prefix=get_prefix, description='SFT Social Bot')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} \nVersion 0.1 \nLibrary Version: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(activity=discord.Streaming(name='Sun Energy', platform="Twitch", url='https://twitch.tv/pewdiepie'))
    print(f'Successfully logged in and booted...!')


bot.run('NjcxMzc5MjI5NTg1MzA5Njk2.Xi8FLw.xlhcG1MwsyiHdpfcDtN5K1X_wBg', bot=True, reconnect=True)
