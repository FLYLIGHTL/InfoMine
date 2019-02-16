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

        
    if message.content==("?ench 화염으로부터 보호"):
        
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
            description="**code** 6\n**ID** minecraft:aqua_affinity\n**최대 레벨** I\n\n**물 안에서 활동이 자유로워지도록 도와줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 가시"):
        
        embed = discord.Embed(
            title="**가시**",
            description="**code** 7\n**ID** minecraft:throne\n**최대 레벨** III\n\n**상대방이 나를 때리면 상대방이 데미지를 입습니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 물갈퀴"):
        
        embed = discord.Embed(
            title="**물갈퀴**",
            description="**code** 8\n**ID** minecraft:depth_strider\n**최대 레벨** III\n\n**물에서 빨리 움직일 수 있게 해줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 차가운 걸음"):
        
        embed = discord.Embed(
            title="**차가운 걸음**",
            description="**code** 9\n**ID** minecraft:frost_walker\n**최대 레벨** II\n\n**물 위에서 걸어다니면 물 표면이 얼음이 됩니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 귀속 저주"):
        
        embed = discord.Embed(
            title="**귀속 저주**",
            description="**code** 10\n**ID** minecraft:binding_curse\n**최대 레벨** II\n\n**갑옷을 한 번 착용하게 되면 벗을 수 없습니다(단, 죽을 시 드롭합니다)**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 날카로움"):
        
        embed = discord.Embed(
            title="**날카로움**",
            description="**code** 16\n**ID** minecraft:sharpness\n**최대 레벨** V\n\n**검의 공격력을 증가시켜 줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 강타"):
        
        embed = discord.Embed(
            title="**강타**",
            description="**code** 17\n**ID** minecraft:smite\n**최대 레벨** V\n\n**모든 언데드 몹에 대해 공격력이 증가됩니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 살충"):
        
        embed = discord.Embed(
            title="**살충**",
            description="**code** 18\n**ID** minecraft:ban_of_arthropods\n**최대 레벨** V\n\n**모든 벌레류 몹에 대해 공격력이 증가됩니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 밀치기"):
        
        embed = discord.Embed(
            title="**밀치기**",
            description="**code** 19\n**ID** minecraft:knockback\n**최대 레벨** II\n\n**검으로 쳤을 때 넉백(밀려나는 거리)가 증가합니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content==("?ench 화염"):
        
        embed = discord.Embed(
            title="**화염**",
            description="**code** 20\n**ID** minecraft:flame\n**최대 레벨** I\n\n**검으로 치면 맞은 엔티티에 불이 붙습니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 약탈"):
        
        embed = discord.Embed(
            title="**약탈**",
            description="**code** 21\n**ID** minecraft:looting\n**최대 레벨** III\n\n**엔티티를 죽였을 때 드롭되는 아이템이 증가합니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 휘몰아치는 칼날"):
        
        embed = discord.Embed(
            title="**휘몰아치는 칼날**",
            description="**code** 22\n**ID** minecraft:sweeping\n**최대 레벨** III\n\n**검으로 긁는 공격을 할 때 공격력이 증가됩니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 효율"):
        
        embed = discord.Embed(
            title="**효율**",
            description="**code** 32\n**ID** minecraft:efficiency\n**최대 레벨** V\n\n**도구를 사용했을 때 더 빨리 캘 수 있습니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 섬세한 손길"):
        
        embed = discord.Embed(
            title="**섬세한 손길**",
            description="**code** 33\n**ID** minecraft:silk_touch\n**최대 레벨** I\n\n**캤을 때 그 아이템 그대로 드롭됩니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 내구성"):
        
        embed = discord.Embed(
            title="**내구성**",
            description="**code** 34\n**ID** minecraft:unbreaking\n**최대 레벨** III\n\n**아이템의 내구도를 증가시켜 줍니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 행운"):
        
        embed = discord.Embed(
            title="**행운**",
            description="**code** 35\n**ID** minecraft:fortune\n**최대 레벨** III\n\n**광물 등을 캤을 때 드롭되는 아이템의 개수가 증가됩니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 힘"):
        
        embed = discord.Embed(
            title="**힘**",
            description="**code** 48\n**ID** minecraft:power\n**최대 레벨** V\n\n**활의 공격력이 증가됩니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 밀어내기"):
        
        embed = discord.Embed(
            title="**밀어내기**",
            description="**code** 49\n**ID** minecraft:punch\n**최대 레벨** II\n\n**활을 쐈을 때 넉백(밀려나는 거리)가 증가됩니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 발화"):
        
        embed = discord.Embed(
            title="**발화**",
            description="**code** 50\n**ID** minecraft:fire_aspect\n**최대 레벨** II\n\n**활에 맞는 엔티티가 불이 붙습니다**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 무한"):
        
        embed = discord.Embed(
            title="**무한**",
            description="**code** 51\n**ID** minecraft:infinity\n**최대 레벨** I\n\n**화살을 한 개만 가지고 있어도 무한정으로 활을 쏠 수 있습니다**",
            color=0x732AA8
            )

        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 바다의 행운"):
        
        embed = discord.Embed(
            title="**바다의 행운**",
            description="**code** 61\n**ID** minecraft:luck_of_the_sea\n**최대 레벨** III\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 미끼"):
        
        embed = discord.Embed(
            title="**미끼**",
            description="**code** 62\n**ID** minecraft:lure\n**최대 레벨** III\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 수선"):
        
        embed = discord.Embed(
            title="**수선**",
            description="**code** 70\n**ID** minecraft:mending\n**최대 레벨** I\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench 소실 저주"):
        
        embed = discord.Embed(
            title="**소실 저주**",
            description="**code** 71\n**ID** minecraft:vanishing_curse\n**최대 레벨** III\n\n**준비 중**",
            color=0x732AA8
            )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("?ench all"):
        await client.send_message(message.channel, "?ench 보호")
        await client.send_message(message.channel, "?ench 화염으로부터 보호")
        await client.send_message(message.channel, "?ench 가벼운 착지")
        await client.send_message(message.channel, "?ench 폭발로부터 보호")
        await client.send_message(message.channel, "?ench 발사체로부터 보호")
        await client.send_message(message.channel, "?ench 호흡")
        await client.send_message(message.channel, "?ench 친수성")
        await client.send_message(message.channel, "?ench 가시")
        await client.send_message(message.channel, "?ench 물갈퀴")
        await client.send_message(message.channel, "?ench 차가운 걸음")
        await client.send_message(message.channel, "?ench 귀속 저주")
        await client.send_message(message.channel, "?ench 날카로움")
        await client.send_message(message.channel, "?ench 강타")
        await client.send_message(message.channel, "?ench 살충")
        await client.send_message(message.channel, "?ench 밀치기")
        await client.send_message(message.channel, "?ench 화염")
        await client.send_message(message.channel, "?ench 약탈")
        await client.send_message(message.channel, "?ench 휘몰아치는 칼날")
        await client.send_message(message.channel, "?ench 효율")
        await client.send_message(message.channel, "?ench 섬세한 손길")
        await client.send_message(message.channel, "?ench 내구성")
        await client.send_message(message.channel, "?ench 행운")
        await client.send_message(message.channel, "?ench 힘")
        await client.send_message(message.channel, "?ench 밀어내기")
        await client.send_message(message.channel, "?ench 발화")
        await client.send_message(message.channel, "?ench 무한")
        await client.send_message(message.channel, "?ench 바다의 행운")
        await client.send_message(message.channel, "?ench 미끼")
        await client.send_message(message.channel, "?ench 수선")
        await client.send_message(message.channel, "?ench 소실 저주")
        

    

access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
