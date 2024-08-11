This Python-based Discord bot allows users to check the status of their VPS directly from a Discord server. The bot provides essential system information, including CPU usage, memory consumption, and disk space usage, all with a simple command. It's perfect for developers and system administrators who want quick insights into their server's performance without leaving Discord.

Features:
System Information: Retrieves basic system details like OS, processor, and machine architecture.
CPU Usage Monitoring: Displays the current CPU usage percentage.
Memory Usage Monitoring: Shows the current memory usage with detailed statistics.
Disk Usage Monitoring: Reports disk space usage on the root partition.

Installation
Clone the Repository:


```
git clone https://github.com/yourusername/vps-status-checker-bot.git
cd vps-status-checker-bot
```

Install Dependencies:
Ensure you have Python 3.x installed, then install the required Python packages:

```
pip install discord.py psutil
```

Set Up Your Bot:
```
Replace 'YOUR_DISCORD_BOT_TOKEN' in the code with your actual Discord bot token.
```

Run the Bot:
```
python vps_status_bot.py
```
Usage
Once the bot is running, use the !status command in any channel where the bot has access to get an overview of your VPS's status.
