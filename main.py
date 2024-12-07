from RobloxApi import GetGroupMemberCount, GetUniverseVisits

import discord, os, json
from discord import Activity, Intents
from discord.ext import commands, tasks

idle = discord.Status.idle
online = discord.Status.online
watch = discord.ActivityType.watching
client = commands.Bot(command_prefix=None, intents=Intents.default(), status=idle)


with open("config.json") as jFile:
    data = json.load(jFile.read())
    visitsChannelId = data["visitsChannelId"]
    membersChannelId = data["membersChannelId"]
    robloxGroupId = data["robloxGroupId"]
    robloxGameId = data["robloxGameId"]
    jFile.close()


#on ready
@client.event
async def on_ready():
    print('bot is ready')
    Ping.start()
    check.start()


@tasks.loop(minutes=1)
async def Ping():
    await client.change_presence(activity=Activity(type=watch, name=f"ping: {round(client.latency*1000)}ms"))


@tasks.loop(hours=2)
# Change Number   ^ To Change When The Channels Update
async def check():
    await client.change_presence(status=online)

    MembersChannel = client.get_channel(int(visitsChannelId))
    VisitsChannel = client.get_channel(int(membersChannelId))

    if not robloxGroupId == "None":
        members = GetGroupMemberCount(robloxGroupId)
        try:
            if members is not None:
                await MembersChannel.edit(name=f'Group Members: {str(members)}'
                                          )
                print('updated member channel')
            else:
                pass
        except Exception as e:
            print(f"cannot update members channel because of {e}")
    else:
        pass


    if not robloxGameId == "None":
        visits = GetUniverseVisits(robloxGameId)
        try:
            if visits is not None:
                await VisitsChannel.edit(name=f'Game Visits: {str(visits)}')
                print('updated visits channel')
            else:
                pass
        except Exception as e:
            print(f"cannot update visits channel because of {e}")
    else:
        pass

    await client.change_presence(status=idle)


client.run(os.environ['Token'])