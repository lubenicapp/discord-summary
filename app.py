from decouple import config
import discord
from lib.openai import tldr
from lib.db.message_store import MessageStore


client = discord.Client(intents=discord.Intents.all())

store = MessageStore()

TLDR_TOO_RECENT = "J'ai déjà fait un résumé récemment !"

@client.event
async def on_message(message):
    print(client.user.id, message.author.id)

    if message.author.bot:
        return

    if message.content == 'TLDR':
        messages = [message async for message in message.channel.history(limit=200)]

        filtered_messages = []
        for m in messages:
            if m.author.id == client.user.id and m.content != TLDR_TOO_RECENT:
                break
            if m.author.id == client.user.id:
                continue
            filtered_messages.append(m)

        messages = filtered_messages[::-1]
        if len(messages) < 10:
            await message.channel.send(TLDR_TOO_RECENT)
            return

        prompt = "\n".join([f"{message.author.display_name}: {message.content}" for message in messages])
        await message.channel.send(tldr(prompt).replace('\\n', '\n'))

client.run(config('DISCORD_CODE_BOT'))
