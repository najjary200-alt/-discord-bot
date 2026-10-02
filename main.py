Import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!مرحبا":
        await message.channel.send("أهلاً بك! أنا بوت Ho_n2(^_-)")

token = os.getenv("DISCORD_BOT_TOKEN")
if not token:
    raise RuntimeError("أضف DISCORD_BOT_TOKEN إلى Secrets")

client.run(token)
