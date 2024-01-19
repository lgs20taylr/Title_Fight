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
# "":{
#   "record":[],
#   "squad":["", "", "",]
# },
epl = {
  "Manchester City":{
    "record":[],
    "squad":["Erling Haaland", "Kevin De Bruyne", "Rúben Dias",]
  },
  "Chelsea":{
    "record":[],
    "squad":["Christopher Nkunku", "Enzo Fernández", "Reece James",]
  },
  "Arsenal":{
    "record":[],
    "squad":["Bukayo Saka", "Declan Rice", "William Saliba",]
  },
  "Liverpool":{
    "record":[],
    "squad":["Mohamed Salah", "Alexis Mac Allister", "Virgil van Dijk",]
  },
  "Aston Villa":{
    "record":[],
    "squad":["Ollie Watkins", "Boubacar Kamara", "Pau Torres",]
  },
  "Tottenham Hotspur":{
    "record":[],
    "squad":["Heung-Min Son", "Giovani Lo Celso", "Cristian Romero",]
  },
  "Manchester United":{
    "record":[],
    "squad":["Rasmus Højlund", "Bruno Fernandes", "Harry Maguire",]
  },
  "Brighton & Hove Albion":{
    "record":[],
    "squad":["Kaoru Mitoma", "Lewis Dunk", "Evan Ferguson",]
  },
  "West Ham United":{
    "record":[],
    "squad":["Jarod Bowen", "Edson Álvarez", "Nayef Aguerd",]
  },
}

def retrieveplayerdata(player):
  for i in database:
    if player in i:
      return i, database[i]
def teamplayer(league, team):
  if league[team]["squad"]:
    return retrieveplayerdata(random.choice(league[team]["squad"]))
def chalp(stat):
  return random.randint(stat, 140)
def simchal(t1hasball, goals1, goals2):
  print(test1, test2)
  if test1 > test2:
    print(player1, "beat", player2)
    if t1hasball and pos2 == "D":
      goals1 += 1
    elif not t1hasball:
      t1hasball = True
  elif test2 > test1:
    print(player2, "beat", player1)
    if not t1hasball and pos1 == "D":
      goals2 += 1
    elif t1hasball:
      t1hasball = False
  else:
    print("Equal")
  return goals1, goals2
def simmatch():
  pac = 0
  sho = 1
  dri = 3
  dfn = 4
  phy = 5
  player1, p1stats = teamplayer(epl, "Manchester City")
  player2, p2stats = teamplayer(epl, "Chelsea")
  pos1 = p1stats[6]
  pos2 = p2stats[6]
  if pos1 == "M" or pos2 == "M":
    chalp(p1stats[phy])
    chalp(p2stats[phy])
  elif pos1 == "D" and pos2 == "A":
    chalp(p1stats[dfn])
    chalp(p2stats[dri]) if random.randint(0, 1) == 0 else chalp(p2stats[sho])
  elif pos1 == "A" and pos2 == "D":
    chalp(p2stats[dfn])
    chalp(p1stats[dri]) if random.randint(0, 1) == 0 else chalp(p1stats[sho])
  else:
    chalp(p1stats[pac])
    chalp(p2stats[pac])
