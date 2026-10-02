import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# إضافة أمر تايم
@bot.command(name="تايم")
async def time_command(ctx):
    await ctx.send("أهلاً بك! تم استلام أمر الوقت بنجاح.")

# إضافة أمر سامحت
@bot.command(name="سامحت")
async def forgive_command(ctx):
    await ctx.send("عفا الله عن ما سلف! تم قبول السماح.")

# قراءة التوكن من رندر بأمان
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)

