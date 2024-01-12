import random

with open("players.txt", "r+") as file:
  plist = file.readlines()
database = {}
for i in plist:
  player = i.split("|")
  temp = player[1].split(",")
  pfacts = []
  for j in temp:
    if j.isnumeric():
      pfacts.append(int(j))
    else:
      pfacts.append(j)
  pfacts.pop(-1)
  database[player[0]] = pfacts
epl = {
  "Manchester City":{
    "record":[],
    "squad":["Erling Haaland", "Kevin De Bruyne", "Rúben Dias",]
  },
  "Chelsea":{
    "record":[],
    "squad":["Christopher Nkunku", "Enzo Fernández", "Reece James",]
  },
}

def retrieveplayerdata(player):
  for i in database:
    if player in i:
      return i, database[i]
def teamplayer(league, team):
  return retrieveplayerdata(random.choice(league[team]["squad"]))
player1, p1stats = teamplayer(epl, "Manchester City")
player2, p2stats = teamplayer(epl, "Chelsea")
pac = 0
sho = 1
pas = 2
dri = 3
dfn = 4
phy = 5
if p1stats[6] == "D":
  test1 = random.randint(p1stats[dfn], 180)
  print("D")
elif p1stats[6] == "M":
  test1 = random.randint(p1stats[phy], 180)
  print("M")
else:
  test1 = random.randint(p1stats[dfn], 180)
  print("A")
if p2stats[6] == "D":
  test2 = random.randint(p2stats[dfn], 180)
  print("D")
elif p2stats[6] == "M":
  test2 = random.randint(p2stats[phy], 180)
  print("M")
else:
  test2 = random.randint(p2stats[dfn], 180)
  print("A")
print(test1, test2)
if test1 > test2:
  print(player1, "beat", player2)
elif test2 > test1:
  print(player2, "beat", player1)
else:
  print("Equal")