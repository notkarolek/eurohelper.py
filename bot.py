import discord
from discord.ext import commands
import os
from threading import Thread
from flask import Flask

from logic.cartax import calculate_cartax
from logic.gold import calculate_gbcount
from logic.transfer import calculate_transfer

# --------------------
# Dummy web server for Koyeb free-tier health checks
# --------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=8000)

# Run the web server in a separate thread
Thread(target=run_web).start()

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
    print(f'Bot is ready! Logged in as {bot.user.name} (ID: {bot.user.id})')
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
    await ctx.send(f"The tax is {amnta:,} ({tax}%) GB and the seller keeps {amntb:,} GB")

# --------------------
# GB Counter Command
# --------------------
@bot.command()
async def gbcount(ctx, money: int):
    gb, remainder = calculate_gbcount(money)
    await ctx.send(f"You can buy {gb} GB and have {remainder} left.")

# --------------------
# Transfer Tax Command
# --------------------
@bot.command()
async def transfer(ctx, amount: int):
    tax, tax_amount = calculate_transfer(amount)
    await ctx.send(f"Transfer tax: {tax_amount} ({tax}%)")

# --------------------
# Mobile Help Command
# --------------------
@bot.command()
async def mobile(ctx):
    await ctx.send(embed=discord.Embed(
        description=(
            "**How to download mobile launcher:**\n\n"
            "[Download](https://github)\n\n"
            "After Downloading **Read The Text On The Splash Screen Carefully!**\n"
            "In the main launcher screen, click the left icon with an up symbol\n"
            "It will lead you to a webpage, in it click **Download Data**\n"
            "On the same website as the download button is a link to **full video tutorial** on extracting\n\n"
            "```Version: 1.3.7 GIT\nVariants:\n Normal (AML 1.3 | Monetloader*)\n  Light (No Extra Mod Engines)\n\n *Monetloader is extremely basic and without commands!!```"
        )
    ))

# --------------------
# Run Bot
# --------------------
token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    print("ERROR: DISCORD_BOT_TOKEN not found in environment variables!")
    exit(1)

bot.run(token)
