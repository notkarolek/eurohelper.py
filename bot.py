import discord
from discord.ext import commands
import os
import threading
from flask import Flask

from logic.cartax import calculate_cartax
from logic.gold import calculate_gbcount
from logic.transfer import calculate_transfer

# --------------------
# Flask Keep-Alive Server
# --------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Europa Helper bot is alive!"

def run_web():
    port = int(os.getenv("PORT", 8000))
    print(f"🌐 Flask keep-alive server running on port {port}")
    app.run(host="0.0.0.0", port=port)

# Start Flask in a background thread
threading.Thread(target=run_web, daemon=True).start()

# --------------------
# Discord Bot Setup
# --------------------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

# --------------------
# Bot Ready Event
# --------------------
@bot.event
async def on_ready():
    print(f'✅ Bot is ready! Logged in as {bot.user.name} (ID: {bot.user.id})')
    print(f'Connected to {len(bot.guilds)} server(s)')
    for guild in bot.guilds:
        print(f'  - {guild.name} (ID: {guild.id})')

# --------------------
# Car Sale Tax Command
# --------------------
@bot.command()
async def cartax(ctx, amount: int):
    amnta, amntb, tax = calculate_cartax(amount)
    if amnta is None:
        await ctx.send(f"{amount:,} is too much to sell for!")
        return
    elif tax == 0:
        await ctx.send(f"No tax applies for {amount:,} GB!")
        return

    await ctx.send(f"The tax is {amnta:,} ({tax}%) GB and the seller keeps {amntb:,} GB")

# --------------------
# GB Counter Command
# --------------------
@bot.command()
async def gold(ctx, money: int):
    gb, remainder = calculate_gbcount(money)
    await ctx.send(f"You can buy {gb} GB and have {remainder:,} $ left.")

# --------------------
# Transfer Tax Command
# --------------------
@bot.command()
async def transfer(ctx, amount: int):
    amnta, amntb, tax = calculate_transfer(amount)

    if amnta is None:
        await ctx.send(f"{amount:,} is an invalid amount!")
        return
    elif tax == 0:
        await ctx.send(f"No transfer tax applies for {amount:,} GB!")
        return

    await ctx.send(f"Transfer tax: {amnta:,} ({tax}%) GB. Amount received: {amntb:,} GB")

# --------------------
# Mobile Help Command
# --------------------
@bot.command()
async def mobile(ctx):
    embed = discord.Embed(
        description=(
            "**How to download mobile launcher:**\n\n"
            "[Download Full](https://www.mediafire.com/file/ulsdg5gp76btxf4/launcher%25283%2529.apk/file)\n"
            "[Download Lite](https://www.mediafire.com/file/0nmejoumm9nolqg/simple.apk/file)\n\n"
            "After Downloading **Read The Text On The Splash Screen Carefully!**\n"
            "In the main launcher screen, click the left icon with an up symbol\n"
            "It will lead you to a webpage, in it click **Download Data**\n"
            "On the same website as the download button is a link to **full video tutorial** on extracting\n\n"
            "```Version: 1.3.7 GIT\nVariants:\n Normal (AML 1.3 | Monetloader*)\n Light (No Extra Mod Engines)\n\n *Monetloader is extremely basic and without commands!!```"
        )
    )
    await ctx.send(embed=embed)
    
    
@bot.command()
async def launcher(ctx):
  embed = Discord.embed(
    description=(
    """🎮 **How to Set Up the Launcher for the First Time** 🎮

[Website](https://europa-mobile.netlify.app/downloadfiles)

1️⃣ **Download the Launcher APK**  
   - Download the launcher APK from the website and install it onto your device.

2️⃣ **Install the APK**  
   - Follow your device’s prompts to complete the installation.

3️⃣ **Download Game Files**  
   - On the same website, click **Download Game Files**.

4️⃣ **Open the Launcher**  
   - Enter the launcher, wait for it to load, then click **Play**.  
   - Set your preferences in the **Settings**.

5️⃣ **Extract the Game Data**  
   - Open **ZArchiver** or your preferred file explorer.  
   - Navigate to the folder where the game data ZIP files are downloaded (e.g., etc.zip, pvr.zip, dxt.zip) and open the ZIP.

6️⃣ **Copy the Files**  
   - Enable **Selection Mode** and select all files.  
   - Hold and choose **Copy**.

7️⃣ **Paste into Launcher Folder**  
   - Navigate to the launcher data folder:  
     `Android/data/com.arizona.game/files`  
   - Paste the copied files and wait until the process finishes.

8️⃣ **Join the Server**  
   - Open the launcher again, click **Play**, and enjoy the game! 🚀

✨ **Enjoy!**
"""
      )
    )
    await ctx.send(embed=embed)
# --------------------
# Run Bot
# --------------------
token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    print("❌ ERROR: DISCORD_BOT_TOKEN not found in environment variables!")
    exit(1)

bot.run(token)