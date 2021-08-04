import discord
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("전략적 팀 전투 "))

@client.event
async def on_message(message):
    content = message.content
    if content.startswith("!악동"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=891e2900e9ea11eb9b07371539a3adea", color=0x00ff56)
        embed.set_author(name="<<6악동  2기병대  2신비술사>>" , url="https://lolchess.gg/builder/set5.5?deck=891e2900e9ea11eb9b07371539a3adea")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체지지"):
        embed=discord.Embed(description="https://lolchess.gg/meta", color=0x00ff56)
        embed.set_author(name="<<롤체지지>>", url="https://lolchess.gg/meta")
        await message.channel.send(embed=embed)

    if content.startswith("!CBT"):
        embed=discord.Embed(description="https://www.comcbt.com/xe/c2/4400733", color=0x00ff56)
        embed.set_author(name="<<CBT>>", url="https://www.comcbt.com/xe/c2/4400733")
        await message.channel.send(embed=embed)
    
    if content.startswith("!오피지지"):
        embed=discord.Embed(description="https://op.gg", color=0x00ff56)
        embed.set_author(name="<<오피지지>>",url="https://op.gg")
        await message.channel.send(embed=embed)

    if content.startswith("!빛도자"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=32e2fa40e94011ebbfb6fbef3103b627", color=0x00ff56)
        embed.set_author(name="<<7빛의 인도자  2망령  2기원자  3싸움꾼  2재생술사>>",url="https://lolchess.gg/builder/set5.5?deck=32e2fa40e94011ebbfb6fbef3103b627")
        await message.channel.send(embed=embed)
    
    if content.startswith("!괴생명체"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=042b86f0e9ea11ebb5e589e115fb8433", color=0x00ff56)
        embed.set_author(name="<<4괴생명체  3망령  4주문술사  2싸움꾼>>",url="https://lolchess.gg/builder/set5.5?deck=042b86f0e9ea11ebb5e589e115fb8433")
        await message.channel.send(embed=embed)

    if(message.content == "!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))

    if content.startswith("!도움"):
        embed=discord.Embed(description="!롤체지지\n!악동\n!빛도자\n!괴생명체\n!시간\n!CBT\n!오피지지", color=0x00ff56)
        embed.set_author(name="<<명령어>>")
        await message.channel.send(embed=embed)
        
    if content.startswith("!옵지 붕벵빙봉"):
        embed=discord.Embed(description="오피지지 붕벵빙봉 바로가기",url = "https://www.op.gg/summoner/userName=%EB%B6%95%EB%B2%B5%EB%B9%99%EB%B4%89", color=0x00ff56)
        embed.set_author(name="<<붕벵빙봉>>")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체 붕벵빙봉"):
        embed=discord.Embed(description="롤체지지 붕벵빙봉 바로가기",url = "https://lolchess.gg/profile/kr/%EB%B6%95%EB%B2%B5%EB%B9%99%EB%B4%89", color=0x00ff56)
        embed.set_author(name="<<붕벵빙봉>>")
        await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKKEN"]
client.run(access_token)
