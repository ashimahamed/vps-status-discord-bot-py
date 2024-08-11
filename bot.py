import discord
from discord.ext import commands
import psutil
import platform

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Notify that the bot is online and ready to use
    print(f'Bot {bot.user} is now online and ready to check your VPS status!')

@bot.command(name='status')
async def vps_status(ctx):
    # Get system information using platform and psutil libraries
    uname = platform.uname()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    # Create a status message to send back to Discord
    status_message = (
        f"**System Information**\n"
        f"**System:** {uname.system}\n"
        f"**Node Name:** {uname.node}\n"
        f"**Release:** {uname.release}\n"
        f"**Version:** {uname.version}\n"
        f"**Machine:** {uname.machine}\n"
        f"**Processor:** {uname.processor}\n\n"
        f"**CPU Usage:** {cpu_usage}%\n"
        f"**Memory Usage:** {memory.percent}% used "
        f"({memory.used // (1024 ** 2)} MB / {memory.total // (1024 ** 2)} MB)\n"
        f"**Disk Usage:** {disk.percent}% used "
        f"({disk.used // (1024 ** 3)} GB / {disk.total // (1024 ** 3)} GB)"
    )

    # Send the status message to the channel where the command was used
    await ctx.send(status_message)

# Run the bot using the token
bot.run(TOKEN)
