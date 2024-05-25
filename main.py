import discord
from discord.ext import commands

# Укажите ваш токен бота
TOKEN = ''
a = ['ванна', 'чистка зубов']
intents = discord.Intents.default()
intents.message_content = True
# Префикс команд
bot = commands.Bot(command_prefix='!', intents=intents)

# Событие запуска бота
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Команда, которая принимает сообщение и сохраняет его в переменную
@bot.command()
async def water(ctx, *, message: str):
    # Сохраняем сообщение в переменную
    saved_message = message
    # Выводим сохраненное сообщение в консоль (для примера)
    print(f'Saved message: {saved_message}')
    # Отправляем подтверждение в чат
    if saved_message == 'ванна':
        await ctx.send(f'наливайте ванну не полностью и чаще мойтесь под душем')
    elif saved_message == 'чистка зубов':
        await ctx.send(f'набирайте воду в стакан и не держите кран открытым пока чистите зубы')
@bot.command()
async def ehelp(ctx):
    await ctx.send(f'список команд {a}')
    

# Запускаем бота
bot.run(TOKEN)
