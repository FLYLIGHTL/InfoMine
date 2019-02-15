import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print("Login Bot")
    print(client.user.name)
    print(client.user.id)
    print("-------------")
    await client.change_presence(game=discord.Game(name='FLYBOT',type=1))


@client.event
async def on_message(message):

    #?ench
    
    if message.content.startswith("?ench 보호"):
        
        embed = discord.Embed(
            title="**보호**",
            description="**code** 0\n**ID** minecraft:protection\n**최대 레벨** V\n\n**공격받을 시 받는 데미지를 줄여 줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)

        
    if message.content.startswith("?ench 화염으로부터 보호"):
        
        embed = discord.Embed(
            title="**화염으로부터 보호**",
            description="**code** 1\n**ID** minecraft:fire_protection\n**최대 레벨** IV\n\n**화염으로부터 입는 데미지를 줄여 줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)

        
    if message.content.startswith("?ench 가벼운 착지"):
        
        embed = discord.Embed(
            title="**가벼운 착지**",
            description="**code** 2\n**ID** minecraft:feather_falling\n**최대 레벨** IV\n\n**가벼운 착지는 낙하데미지를 줄여 줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)

        
    if message.content.startswith("?ench 폭발로부터 보호"):
        
        embed = discord.Embed(
            title="**폭발로부터 보호**",
            description="**code** 3\n**ID** minecraft:blast_protection\n**최대 레벨** IV\n\n**폭발로부터 입는 데미지를 줄여 줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 발사체로부터 보호"):
        
        embed = discord.Embed(
            title="**발사체로부터 보호**",
            description="**code** 4\n**ID** minecraft:projectille_protection\n**최대 레벨** IV\n\n**발사체로부터 입는 데미지를 줄여 줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 호흡"):
        
        embed = discord.Embed(
            title="**호흡**",
            description="**code** 5\n**ID** minecraft:respiration\n**최대 레벨** III\n\n**물속에서 물방울이 감소하는 속도를 줄여 줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 친수성"):
        
        embed = discord.Embed(
            title="**친수성**",
            description="**code** 6\n**ID** minecraft:aqua_affinity\n**최대 레벨** I\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 가시"):
        
        embed = discord.Embed(
            title="**가시**",
            description="**code** 7\n**ID** minecraft:throne\n**최대 레벨** III\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 물갈퀴"):
        
        embed = discord.Embed(
            title="**물갈퀴**",
            description="**code** 8\n**ID** minecraft:depth_strider\n**최대 레벨** III\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 차가운 걸음"):
        
        embed = discord.Embed(
            title="**차가운 걸음**",
            description="**code** 9\n**ID** minecraft:frost_walker\n**최대 레벨** II\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 귀속 저주"):
        
        embed = discord.Embed(
            title="**귀속 저주**",
            description="**code** 10\n**ID** minecraft:binding_curse\n**최대 레벨** II\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 날카로움"):
        
        embed = discord.Embed(
            title="**날카로움**",
            description="**code** 16\n**ID** minecraft:sharpness\n**최대 레벨** V\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?enchA"):
        
        embed = discord.Embed(
            title="**?**",
            description="**code** n\n**ID** minecraft:?\n**최대 레벨** ?\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 강타"):
        
        embed = discord.Embed(
            title="**강타**",
            description="**code** 17\n**ID** minecraft:smite\n**최대 레벨** V\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 살충"):
        
        embed = discord.Embed(
            title="**살충**",
            description="**code** 18\n**ID** minecraft:ban_of_arthropods\n**최대 레벨** V\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 밀치기"):
        
        embed = discord.Embed(
            title="**밀치기**",
            description="**code** 19\n**ID** minecraft:knockback\n**최대 레벨** II\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 화염"):
        
        embed = discord.Embed(
            title="**화염**",
            description="**code** 20\n**ID** minecraft:flame\n**최대 레벨** I\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 약탈"):
        
        embed = discord.Embed(
            title="**약탈**",
            description="**code** 21\n**ID** minecraft:looting\n**최대 레벨** III\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 휘몰아치는 칼날"):
        
        embed = discord.Embed(
            title="**휘몰아치는 칼날**",
            description="**code** 22\n**ID** minecraft:sweeping\n**최대 레벨** III\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 효율"):
        
        embed = discord.Embed(
            title="**효율**",
            description="**code** 23\n**ID** minecraft:efficiency\n**최대 레벨** V\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 섬세한 손길"):
        
        embed = discord.Embed(
            title="**섬세한 손길**",
            description="**code** 24\n**ID** minecraft:silk_touch\n**최대 레벨** I\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 내구성"):
        
        embed = discord.Embed(
            title="**내구성**",
            description="**code** n\n**ID** minecraft:?\n**최대 레벨** ?\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 행운"):
        
        embed = discord.Embed(
            title="**?**",
            description="**code** n\n**ID** minecraft:?\n**최대 레벨** ?\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 힘"):
        
        embed = discord.Embed(
            title="**?**",
            description="**code** n\n**ID** minecraft:?\n**최대 레벨** ?\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 밀어내기"):
        
        embed = discord.Embed(
            title="**?**",
            description="**code** n\n**ID** minecraft:?\n**최대 레벨** ?\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 발화"):
        
        embed = discord.Embed(
            title="**?**",
            description="**code** n\n**ID** minecraft:?\n**최대 레벨** ?\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 무한"):
        
        embed = discord.Embed(
            title="**?**",
            description="**code** n\n**ID** minecraft:?\n**최대 레벨** ?\n\n**준비 중**",
            color=0x732AA8
            )

        await client.send_message(message.channel, embed=embed)


access_token=os.environ["BOT_TOKEN"]        
client.run(access_token)
