# Use Semantic Versioning: https://semver.org/
# Ensure that new code works on Testing branch before committing to Main

import math
import random
import time

# initepl = {
#   "Arsenal":83,
#   "Manchester City":85,
#   "Liverpool":83,
#   "Aston Villa":80,
#   "Tottenham Hotspur":81,
#   "Manchester United":82,
#   "Newcastle United":80,
#   "Brighton & Hove Albion":77,
#   "West Ham United":78,
#   "Chelsea":80,
# }
# initech = {
#   "Leicster City":75,
#   "Ipswitch Town":69,
#   "West Bromwich Albion":71,
#   "Leeds United":73,
#   "Southampton":73,
#   "Hull City":70,
#   "Preston North End":70,
#   "Cardiff City":70,
#   "Middlesborough":71,
#   "Sunderland":69,
# }
# # basedict = {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":0}

leagues = {
  "england":{"epl":{
            "Arsenal":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Bukayo Saka", "Declan Rice", "William Saliba"]},
            "Chelsea":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Christopher Nkunku", "Enzo Fernandez", "Reece James",]},
            "Manchester City":{"points":4,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Erling Haaland", "Kevin De Bruyne", "Ruben Dias",]},
            "Liverpool":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Mohamed Salah","Alexis Mac Allister","Virgil van Dijk",]},
            "Tottenham Hotspur":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Heung-Min Son", "Giovani Lo Celso", "Cristian Romero",]},
            "Manchester United":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Rasmus Hojlund", "Bruno Fernandes", "Harry Maguire",]},
            "Luton Town":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Elijah Adebayo", "Ross Barkley", "Ryan Giles",]},
            "Aston Villa":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Ollie Watkins", "Boubacar Kamara", "Pau Torres",]},
            },
    "ech":{
    "Leicester City":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Jamie Vardy","Wilfred Ndidi","Ricardo Pereira"]},
    "Ipswitch Town":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["George Hirst","Conor Chaplin","Leif Davis",]},
    "West Bromwitch Albion":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Josh Maja","John Swift","Darnell Furlong",]},
    "Leeds United":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Georginio Rutter","Glen Kamara","Joe Rondon"]},
    "Southhampton":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Che Adams","Carlos Alcaraz","Kyle Walker-Peters",]},
    "Hull City":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":["Liam Delap","Jean Seri","Sean McLoughlin"]},
    },},
}

commentary = {
  "miss":[],
  "goal":[],
  "end":[],
  "start":[],
  "dispos":[],
}
database = {}
def initcom():
  global commentary
  for i in commentary:
    with open((i+".txt"), mode = "r") as file:
      commentary[i] = file.readlines()
def initdatabase():
  global database
  with open("players.txt", "r+") as file:
    plist = file.readlines()
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
timings = {
  "matchintervals":{"normal":0.75,"goal":1.5},
  "attmatchend":2,
  "normatchend":0.025,
}
def retrieveplayerdata(player):
  global database  
  return database[player]
def chalp(stat):
  return random.randint(stat, 140)
def chalres(t1hasball, test1, test2, player1, player2, pos1, pos2):
  goal1 = False
  goal2 = False
  if test1 > test2:
    if t1hasball and pos2 == "D" and (pos1 == "A" or pos1 == "M" or (pos1 == "D" and random.randint(0,3) == 0)):
      goal1 = True
      t1hasball = False
    elif not t1hasball and not test1 > test2+random.randint(0,30):
      t1hasball = True
  elif test2 > test1:
    if not t1hasball and pos1 == "D" and (pos2 == "A" or pos2 == "M" or (pos2 == "D" and random.randint(0,3) == 0)):
      goal2 = True
      t1hasball = True
    elif t1hasball and test2 > test1+random.randint(0,30):
      t1hasball = False
  return t1hasball, goal1, goal2
def simchal(p1stats, p2stats, pos1, pos2):
  if pos1 == "M" or pos2 == "M":
    test1 = chalp(p1stats[5])
    test2 = chalp(p2stats[5])
  elif pos1 == "D" and pos2 == "A":
    test1 = chalp(p1stats[4])
    test2 = chalp(p2stats[3]+20) if random.randint(0, 1) == 0 else chalp(p2stats[1])
  elif pos1 == "A" and pos2 == "D":
    test1 = chalp(p2stats[4])
    test2 = chalp(p1stats[3]+20) if random.randint(0, 1) == 0 else chalp(p1stats[1])
  else:
    test1 = chalp(p1stats[0])
    test2 = chalp(p2stats[0])
  return test1, test2
def simmatch(team1,team2,league,spectating):
  watching = team1 in spectating or team2 in spectating
  league[team1]["played"] += 1
  league[team2]["played"] += 1
  score1 = {}
  score2 = {}
  goal1 = False
  goal2 = False
  msq1, msq2 = pickmatchsquad(league[team1]), pickmatchsquad(league[team2])
  t1hasball = random.randint(0, 1) == 0
  if watching:
    commentpick = random.choice(commentary["start"])
    print(f"Attending Matchday: {team1} vs {team2}.\n\n{commentpick}")
  for i in range(1,19):
    if watching and (goal1 or goal2):
      time.sleep(timings["matchintervals"]["goal"])
    elif watching:
      time.sleep(timings["matchintervals"]["normal"])
    player1 = random.choice(msq1)
    player2 = random.choice(msq2)
    p1stats = retrieveplayerdata(player1)
    p2stats = retrieveplayerdata(player2)
    pos1 = p1stats[6]
    pos2 = p2stats[6]
    test1, test2 = simchal(p1stats,p2stats,pos1,pos2)
    tempball = t1hasball
    t1hasball, goal1, goal2 = chalres(t1hasball, test1, test2, player1, player2, pos1, pos2)
    minutes = random.randint(math.floor((i*5)-4),math.floor(i*5))
    if goal1:
      score1[minutes] = 1
      league[team1]["gf"] += 1
      league[team2]["ga"] += 1
      if watching:
        commentpick = random.choice(commentary["goal"])
        print(f"[{minutes}] GOAL! {player1} scores for {team1}! {commentpick} {team1} {len(score1)} - {len(score2)} {team2}\n")
    elif goal2:
      score2[minutes] = 1
      league[team2]["gf"] += 1
      league[team1]["ga"] += 1
      if watching:
        commentpick = random.choice(commentary["goal"])
        print(f"[{minutes}] GOAL! {player2} scores for {team2}! {commentpick}\n {team1} {len(score1)} - {len(score2)} {team2}")
    elif tempball != t1hasball and watching:
      commentpick = random.choice(commentary["dispos"])
      if t1hasball:
        print(f"[{minutes}] {player1} {commentpick} {player2}.")
      else:
        print(f"[{minutes}] {player2} {commentpick} {player1}.")
    tempball = t1hasball
  if len(score1) > len(score2):
    result1 = "W"
    league[team1]["points"] += 3
    result2 = "L"
  elif len(score2) > len(score1):
    result1 = "L"
    result2 = "W"
    league[team2]["points"] += 3
  else:
    result1 = "D"
    league[team1]["points"] += 1
    result2 = "D"
    league[team2]["points"] += 1
  league[team1]["gd"] = league[team1]["gf"] - league[team1]["ga"]
  league[team2]["gd"] = league[team2]["gf"] - league[team2]["ga"]
  commentpick = random.choice(commentary["end"])
  if watching:
    print(commentpick)
  print(f"\n{result1} {team1} {len(score1)} - {len(score2)} {team2} {result2}\n------------------------------------------")
  if watching:
    time.sleep(timings["attmatchend"])
  else:
    time.sleep(timings["normatchend"])
  return league
def printtable(table):
  print("Team Name|Points|Played|Goal Difference|Goals For|Goals Against|Rating")
  for i in table:
    print(i,table[i]["points"],table[i]["played"],table[i]["gd"],table[i]["gf"],table[i]["ga"],calcavgrat(table,i))
def generatefixtures(league):
  fixtures = {}
  bowl = list(league.keys())
  for _weeks in league:
    while bowl:
      hometeam = random.choice(bowl)
      bowl.remove(hometeam)
      awayteam = random.choice(bowl)
      bowl.remove(awayteam)
      fixtures[hometeam] = awayteam
  return fixtures
def weekbyweek(lname,lstr):
  lfixtures = {}
  seasonlength = {
    "epl":14,
    "ech":10,
  }
  for week in range(seasonlength[lstr]):
    lfixtures[week] = generatefixtures(lname)
  return lfixtures
def playerrat(player):
  global database
  cum = 0
  statcum = 0
  pstats = database[player].copy()
  pos = pstats[6]
  if pos == "A":
    cum = pstats[0]+pstats[1]+pstats[3]
    statcum = 3
  elif pos == "M":
    cum = pstats[2]+pstats[5]
    statcum = 2
  elif pos == "D":
    cum = pstats[4]+pstats[5]
    statcum = 2
  return cum, statcum
def calcavgrat(league, team):
  cum = 0
  statcum = 0
  for player in league[team]["squad"]:
    cum, statcum = playerrat(player)
  return cum // statcum
def radj():
  return random.randint(-3,3)
def updaterating(league):
  global database
  for team in league:
    rchan = round((league[team]["gd"]/4) + (league[team]["points"]/2))
    for player in league[team]["squad"]:
      ratadj(player,rchan)
  return league
def ratadj(player,rchan=0):
  agebonus = {14:8,15:8,16:8,17:6,18:5,19:5,20:5,21:4,22:3,23:2,24:1,25:1,26:0,27:0,28:0,29:0,30:-1,31:-2,32:-3,33:-4,34:-5,35:-6,36:-7,37:-8,38:-9,39:-10,40:-12}
  position = database[player][6]
  age = database[player][8]
  if position == "A":
    database[player][0] += rchan + radj() + agebonus[age]
    database[player][1] += rchan + radj() + agebonus[age]
    database[player][3] += rchan + radj() + agebonus[age]
  elif position == "M":
    database[player][2] += rchan + radj() + agebonus[age]
    database[player][5] += rchan + radj() + agebonus[age]
  elif position == "D":
    database[player][4] += rchan + radj() + agebonus[age]
    database[player][5] += rchan + radj() + agebonus[age]
  database[player][8] += 1
  for stat in range(len(database[player])-3):
    if database[player][stat] < 10:
      database[player][stat] = 10
    elif database[player][stat] >= 120:
      database[player][stat] = 120
def updatefas(epl,ech):
  for player in database:
    if database[player][7] not in epl and database[player][7] not in ech:
      ratadj(player,random.randint(-5,5))
def resetleague(league):
  for i in league:
    league[i]["points"], league[i]["played"], league[i]["won"], league[i]["lost"], league[i]["drawn"],  league[i]["gd"], league[i]["gf"], league[i]["ga"] = 0,0,0,0,0,0,0,0
  return league
def findtop(league):
  # temporary solution
  templeague = league.copy()
  templeague["Temp"], templeague["temp"] = {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":[]}, {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":[]}
  top = ["Temp","temp"]
  for j in range(2):
    for i in templeague:
      if templeague[i]["points"] > templeague[top[j]]["points"]:
        top[j] = i
    templeague.pop(top[j])
  return top
def findbottom(league):
  templeague = league.copy()
  # temporary solution
  templeague["Temp"], templeague["temp"] = {"points":9999,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":[]}, {"points":9999,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":[]}
  top = ["Temp","temp"]
  for j in range(2):
    for i in templeague:
      if templeague[i]["points"] < templeague[top[j]]["points"]:
        top[j] = i
    templeague.pop(top[j])
  return top
def updown(relegated, promoted, topl, botl):
  for i in relegated:
    botl[i] = {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":topl[i]["squad"]}
    topl.pop(i)
  for i in promoted:
    topl[i] = {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"squad":botl[i]["squad"]}
    botl.pop(i)
  return botl, topl
def pickmatchsquad(team):
  squad = ["Bad Guy","Bad Guy","Bad Guy"]
  for player in team["squad"]:
    rat = playerrat(player)
    pos = database[player][6]
    if pos == "D" and rat > playerrat(squad[0]):
      squad[0] = player
    elif pos == "M" and rat > playerrat(squad[1]):
      squad[1] = player
    elif pos == "A" and rat > playerrat(squad[2]):
      squad[2] = player
  return squad
def handletrans(origin, player, dest, epl, ech):
  oleague = epl if origin in epl else ech if origin in ech else False
  dleague = epl if dest in epl else ech if dest in ech else False
  if player in database:
    if oleague:
      oleague[origin]["squad"].remove(player)
    if dleague:
      dleague[dest]["squad"].append(player)
      database[player][7] = dest
def main():
  initdatabase()
  epl = leagues["england"]["epl"]
  ech = leagues["england"]["ech"]
  runitback = "y"
  initcom()
  while runitback.lower() == "y":
    epl = resetleague(epl)
    ech = resetleague(ech)
    eplfixtures = weekbyweek(epl,"epl")
    echfixtures = weekbyweek(ech,"ech")
    spectating = []
    morespec = "y"
    while morespec.lower() == "y":
      spectating.append(input("Input a team to spectate."))
      morespec = input("Add another team? y/n")
    for i in eplfixtures:
      for match in eplfixtures[i]:
        simmatch(match,eplfixtures[i][match],epl,spectating)
      print("###############################\nEnglish Premier League")
      printtable(epl)
      with open("epl.txt", mode = "w") as file:
        file.write(str(epl))
    for i in echfixtures:
      for match in echfixtures[i]:
        simmatch(match,echfixtures[i][match],ech,spectating)
      print("###############################\nEFL Championship")
      printtable(ech)
      with open("ech.txt", mode = "w") as file:
        file.write(str(ech))
    print("###############################\nEnglish Premier League")
    printtable(epl)
    print("###############################\nEFL Championship")
    printtable(ech)
    epl = updaterating(epl)
    ech = updaterating(ech)
    relegated = findbottom(epl)
    promoted = findtop(ech)
    ech, epl = updown(relegated, promoted, epl, ech)
    for _ in range(5):
      new, stats = regen()
      database[new] = stats
    updatefas(epl,ech)
    printdatabase(database)
    maketrans = bool(input("Make transfers?").lower() == "y")
    while maketrans:
      print("Transfer Window Open")
      handletrans(input("Input Origin Team or FA if free agent"), input("Input Player"), input("Input Destination Team"), epl, ech)
      maketrans = input("Make another transfer?").lower() == "y"
    runitback = input("Simulate another season?")
def printdatabase(database):
  for i in database:
    print(i, database[i])
def regen(ythrating=60, team="Free Agent"):
  firstnames = ['John', 'Noah', 'George', 'Oliver', 'Muhammad', 'Arthur', 'Leo', 'Harry', 'Oscar', 'Henry', 'Theodore', 'Erling', 'Kevin', 'Ruben', 'Reece', 'Christopher', 'Enzo', 'Mohamed', 'Alexis', 'Virgil', 'Bukayo', 'Declan', 'William', 'Ollie', 'Boubacar', 'Pau', 'Heung-Min', 'Giovani', 'Cristian', 'Rasmus', 'Bruno', 'Harry', 'Evan', 'Kaoru', 'Lewis', 'Jarrod', 'Edson', 'Nayef', 'Callum', 'Sandro', 'Kieran', 'Elijah', 'Ross', 'Ryan', 'Matheus', 'Mario', 'Nelson', 'Zeki', 'Mike', 'Jordan', 'Cameron', 'Gustavo', 'Anel', 'Jamie', 'Wilfred', 'Ricardo', 'Che', 'Carlos', 'Kyle', 'George', 'Conor', 'Leif', 'Josh', 'John', 'Darnell', 'Georginio', 'Glen', 'Joe', 'Liam', 'Jean', 'Sean', 'Milutin', 'Benjamin', 'Yakou', 'Karlan', 'Mark', 'Emmanuel', 'Hayden', 'Dael', 'Mason', 'Jobe', 'Daniel', 'Jesse', 'Jerome', 'Kylian', 'Ethan', 'Vinicius', 'Henry', 'Big', 'Bad'] 
  lastnames = ['Smith', 'Jones', 'Williams', 'Taylor', 'Davies', 'Brown', 'Wilson', 'Evans', 'Thomas', 'Johnson', 'Roberts', 'Walker', 'Wright', 'Robinson', 'Thompson', 'White', 'Hughes', 'Edwards', 'Green', 'Lewis', 'Wood', 'Haris', 'Martin', 'Jackson', 'Clarke', 'Haaland', 'de Bruyne', 'Dias', 'James', 'Nkunku', 'Fernandez', 'Salah', 'MacAlister', 'van Dijk', 'Saka', 'Rice', 'Saliba', 'Watkins', 'Kamara', 'Torres', 'Son', 'Celso', 'Romero', 'Hojlund', 'Fernandes', 'Maguire', 'Ferguson', 'Mitoma', 'Dunk', 'Bowen', 'Alvarez', 'Aguerd', 'Wilson', 'Tonali', 'Trippier', 'Adebayo', 'Barkley', 'Giles', 'Cunha', 'Lemina', 'Semedo', 'Amdouni', 'Tresor', 'Beyer', 'Archer', 'Hamer', 'Ahmedhodzic', 'Vardy', 'Ndidi', 'Pereira', 'Adams', 'Alcaraz', 'Walker-Peters', 'Hirst', 'Chaplin', 'Davis', 'Maja', 'Swift', 'Furlong', 'Rutter', 'Rondon', 'Delap', 'Seri', 'McLoughlin', 'Osmajic', 'Whiteman', 'Storey', 'Meite', 'Ahearne-Grant', 'McGuinness', 'Latte', 'Hackney', 'Fry', 'Burstow', 'Bellingham', 'Ballard', 'Lingard', 'Boateng', 'Mbappe', 'Junior', 'Martin', 'Boy', 'Chap', 'Lad', 'Guy']
  poslist = ["A","M","D",]
  player = random.choice(firstnames) + " " + random.choice(lastnames)
  pstats = [random.randint(20,ythrating),random.randint(20,ythrating),random.randint(20,ythrating),random.randint(20,ythrating),random.randint(20,ythrating),random.randint(20,ythrating),random.choice(poslist),team,random.randint(14,21)]
  return player, pstats
# initdatabase()
# for i in database:
#   if len(database[i]) < 7:
#     print(i)
if __name__ == "__main__":
  main()