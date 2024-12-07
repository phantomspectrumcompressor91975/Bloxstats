import json
from urllib.request import urlopen


def GetGroupMemberCount(GroupID: int) -> int | None:
  with urlopen(f"https://groups.roblox.com/v1/groups/{GroupID}") as response:
    if response.status == 200:
      data = json.loads(response.read())
      return int(data["memberCount"])
    else:
      return None


def GetUniverseVisits(universeId: int) -> int | None:
  response = urlopen(f"https://games.roblox.com/v1/games?universeIds={universeId}")
  if response.status == 200:
    resJson = json.loads(response.read())
    data = resJson['data'][0]
    return int(data['visits'])
  else:
    return None