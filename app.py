from decouple import config
import discord
from lib.openai import tldr
from lib.db.message_store import MessageStore


client = discord.Client(intents=discord.Intents.all())

store = MessageStore()

TLDR_TOO_RECENT = "J'ai déjà fait un résumé récemment !"

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.author.bot and not message.content == 'TLDR':
        store.store({"created_at": message.created_at, "content": message.content, "author": message.author})

    if message.content == 'TLDR':
        messages = [message async for message in message.channel.history(limit=200)][::-1]

        if any(m.author.bot and m.content != TLDR_TOO_RECENT for m in messages):
            await message.channel.send(TLDR_TOO_RECENT)
            return

        messages = [m for m in messages if m.author.bot is False]

        prompt = "\n".join([f"{message.author.display_name}: {message.content}" for message in messages])
        await message.channel.send(tldr(prompt).replace('\\n', '\n'))

client.run(config('DISCORD_CODE_BOT'))
