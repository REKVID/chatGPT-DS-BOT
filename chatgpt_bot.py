import discord
import os
import openai







# Установите свой токен для Discord бота
DISCORD_TOKEN = 'YOUR TOKEN'

# Установите ваш API-ключ для OpenAI
OPENAI_API_KEY = 'YOUR API KEY'

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
