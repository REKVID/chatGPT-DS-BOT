import discord
import os
import openai

# gpt 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
# ds  ("MTE0NjMxOTAzNDQ4MTEzMTU5MA.Gm-joc.x9synvrrgm5-TCH1yEAg8RkUnEWjSP4h-NzmF4")










# Установите свой токен для Discord бота
DISCORD_TOKEN = 'MTE0NjMxOTAzNDQ4MTEzMTU5MA.Gm-joc.x9synvrrgm5-TCH1yEAg8RkUnEWjSP4h-NzmF4'

# Установите ваш API-ключ для OpenAI
OPENAI_API_KEY = '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'

# Инициализация бота Discord
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

# Инициализация API OpenAI
openai.api_key = OPENAI_API_KEY

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    # Игнорирование сообщений от ботов, включая самого себя
    if message.author.bot:
        return

    if message.content.startswith('/chat'):
        user_input = message.content.replace('/chat', '').strip()

        # Отправляем запрос к API ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=str(user_input),
            top_p=1.0,
            temperature=0.9,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            max_tokens=1000,
            stop=["You:"]
        )

        bot_reply = response.choices[0].text.strip()

        await message.channel.send(bot_reply)

# Запуск бота
client.run(DISCORD_TOKEN)