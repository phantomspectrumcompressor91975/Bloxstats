import json
from urllib.request import urlopen


requestUrls = [
  ["https://groups.roblox.com/v1/groups/{}", "memberCount"],
  ["https://games.roblox.com/v1/games?universeIds={}", "visits"],
]


def request(ID: int, index: int) -> int | None:
  table = requestUrls[index]
  print(table)
  with urlopen(table[0].format(ID)) as response:
    if response.status == 200:
      data = json.loads(response.read())
      return int(data[table[1]])
    else:
      return None