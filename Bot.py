import discord
import datetime
import os
import time
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print('------')
    for i in range(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        await client.change_presence(status=discord.Status.online, activity=discord.Game("전략적 팀 전투 "))
        time.sleep(7)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("이원찬 찬양"))
        time.sleep(7)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Visual Studio Code"))
        time.sleep(7)

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
        
    if content.startswith("!용족"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=5ad9ced0f5ab11eb954c75ec6e5adda9", color=0x00ff56)
        embed.set_author(name="<<5용족 3척후병 3감시자 2싸움꾼>>",url="https://lolchess.gg/builder/set5.5?deck=32e2fa40e94011ebbfb6fbef3103b627")
        await message.channel.send(embed=embed)
    
    if content.startswith("!괴생명체"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=042b86f0e9ea11ebb5e589e115fb8433", color=0x00ff56)
        embed.set_author(name="<<4괴생명체  3망령  4주문술사  2싸움꾼>>",url="https://lolchess.gg/builder/set5.5?deck=042b86f0e9ea11ebb5e589e115fb8433")
        await message.channel.send(embed=embed)
    
    if content.startswith("!재생술사"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=527fcb90ef8911eba0c385872c72b794", color=0x00ff56)
        embed.set_author(name="<<4재생술사 2기원자 2빛도자 2악동 3감시자 3>>",url="https://lolchess.gg/builder/set5.5?deck=527fcb90ef8911eba0c385872c72b794")
        await message.channel.send(embed=embed)
        
    if content.startswith("!망각"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=83fa7470fa5811ebb02167a6298483f0", color=0x00ff56)
        embed.set_author(name="<<6망각 2기병대 2철갑 2>>",url="https://lolchess.gg/builder/set5.5?deck=83fa7470fa5811ebb02167a6298483f0")
        await message.channel.send(embed=embed)
        
    if(message.content == "!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))

    if content.startswith("!도움"):
        embed=discord.Embed(description="!롤체지지\n!악동\n!빛도자\n!괴생명체\n!시간\n!CBT\n!오피지지\n!롤체 <닉네임>\n!옵지 <닉네임>\n\n닉네임은 이 디코방에 있는 분만 등록 해놨습니다", color=0x00ff56)
        embed.set_author(name="<<명령어>>")
        await message.channel.send(embed=embed)
        
    if content.startswith("!옵지 붕벵빙봉"):
        embed=discord.Embed(description="오피지지 붕벵빙봉 바로가기\nhttps://www.op.gg/summoner/userName=%EB%B6%95%EB%B2%B5%EB%B9%99%EB%B4%89", color=0x00ff56)
        embed.set_author(name="<<붕벵빙봉>>")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체 붕벵빙봉"):
        embed=discord.Embed(description="롤체지지 붕벵빙봉 바로가기\nhttps://lolchess.gg/profile/kr/%EB%B6%95%EB%B2%B5%EB%B9%99%EB%B4%89", color=0x00ff56)
        embed.set_author(name="<<붕벵빙봉>>")
        await message.channel.send(embed=embed)

    if content.startswith("!옵지 응애나아기롤리니"):
        embed=discord.Embed(description="오피지지 응애나아기롤리니 바로가기\nhttps://www.op.gg/summoner/userName=응애나아기롤리니", color=0x00ff56)
        embed.set_author(name="<<응애나아기롤리니>>")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체 응애나아기롤리니"):
        embed=discord.Embed(description="롤체지지 응애나아기롤리니 바로가기\nhttps://lolchess.gg/profile/kr/응애나아기롤리니", color=0x00ff56)
        embed.set_author(name="<<응애나아기롤리니>>")
        await message.channel.send(embed=embed)

    if content.startswith("!옵지 챔원삐뽀"):
        embed=discord.Embed(description="오피지지 챔원삐뽀 바로가기\nhttps://www.op.gg/summoner/userName=챔원삐뽀", color=0x00ff56)
        embed.set_author(name="<<챔원삐뽀>>")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체 챔원삐뽀"):
        embed=discord.Embed(description="롤체지지 챔원삐뽀 바로가기\nhttps://lolchess.gg/profile/kr/챔원삐뽀", color=0x00ff56)
        embed.set_author(name="<<챔원삐뽀>>")
        await message.channel.send(embed=embed)

    if content.startswith("!옵지 박죄현"):
        embed=discord.Embed(description="오피지지 박 죄 현 바로가기\nhttps://www.op.gg/summoner/userName=박죄현", color=0x00ff56)
        embed.set_author(name="<<박 죄 현>>")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체 박죄현"):
        embed=discord.Embed(description="롤체지지 박 죄 현 바로가기\nhttps://lolchess.gg/profile/kr/박죄현", color=0x00ff56)
        embed.set_author(name="<<박 죄 현>>")
        await message.channel.send(embed=embed)

    if content.startswith("!옵지 먼치킨빵댕이"):
        embed=discord.Embed(description="오피지지 먼치킨빵댕이 바로가기\nhttps://www.op.gg/summoner/userName=먼치킨빵댕이", color=0x00ff56)
        embed.set_author(name="<<먼치킨빵댕이>>")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체 먼치킨빵댕이"):
        embed=discord.Embed(description="롤체지지 먼치킨빵댕이 바로가기\nhttps://lolchess.gg/profile/kr/먼치킨빵댕이", color=0x00ff56)
        embed.set_author(name="<<먼치킨빵댕이>>")
        await message.channel.send(embed=embed)

    if content.startswith("!옵지 Lv1Midyuqi"):
        embed=discord.Embed(description="오피지지 Lv1 Mid yuqi 바로가기\nhttps://lolchess.gg/profile/kr/lv1midyuqi", color=0x00ff56)
        embed.set_author(name="<<Lv1 Mid yuqi>>")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체 Lv1Midyuqi"):
        embed=discord.Embed(description="롤체지지 Lv1 Mid yuqi 바로가기\nhttps://lolchess.gg/profile/kr/lv1midyuqi", color=0x00ff56)
        embed.set_author(name="<<Lv1 Mid yuqi>>")
        await message.channel.send(embed=embed)
    
    if content.startswith("!옵지 BurbleDust"):
        embed=discord.Embed(description="오피지지 Burbledust 바로가기\nhttps://lolchess.gg/profile/kr/burbledust", color=0x00ff56)
        embed.set_author(name="<<Burble Dust>>")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체 BurbleDust"):
        embed=discord.Embed(description="롤체지지 Burble Dust 바로가기\nhttps://lolchess.gg/profile/kr/burbledust", color=0x00ff56)
        embed.set_author(name="<<Burble Dust>>")
        await message.channel.send(embed=embed)
        
    if content.startswith("!인백이의 드립은"):
        await message.channel.send("개씹노잼입니다")    
        
access_token = os.environ["BOT_TOKKEN"]
client.run(access_token)
