import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN= '봇 토큰 삽입'

#닉네임과 결과 저장하는 딕셔너리
rollResult = {}

#정렬된 결과 저장하는 딕셔너리
sortResult = {}

#봇 시작
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('주사위 또르륵'))
    print("구동 완료")

#명령어 찾기, 봇이면 무시
@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

#주사위 굴리기, 닉네임과 함께 출력
#서버 전용 닉네임이 없으면 None으로 출력됨
#예외처리실패...
@bot.command()
async def roll(ctx):
    rand_roll = random.randint(0, 100)
    nick = ctx.author.nick
    #if nick=='None':
    #    nick=ctx.author.name

    await ctx.channel.send(f':game_die: {ctx.author.mention} rolled: {rand_roll} :game_die:', reference=ctx.message)
    rollResult[nick]=rand_roll

#정렬, value값 내림차순
@bot.command()
async def sort(ctx):
    sortResult = sorted(rollResult.items(), key=lambda x: (x[1], x[0]), reverse=True)
    for key, value in sortResult:
        await ctx.channel.send(f'{key}, {value}')

    rollResult.clear()
    sortResult.clear()

#봇 실행
bot.run(TOKEN)