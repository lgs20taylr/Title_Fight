# Use Semantic Versioning: https://semver.org/
# Ensure that new code works on Testing branch before committing to Main

import random
import time
import json

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
            "Arsenal":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":83},
            "Chelsea":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":80},
            "Manchester City":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":85},
            "Liverpool":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":83},
            "Aston Villa":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":80},
            "Tottenham Hotspur":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":81},
            "Manchester United":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":82},
            "Brighton & Hove Albion":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":77},
            "West Ham United":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":78},
            "Newcastle United":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":80},
            "Luton Town":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":72},
            "Burnley":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":74},
            "Sheffield United":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":73},
            "Wolverhampton Wonderers":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":74},
            },
    "ech":{
    "Leicster City":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":75},
    "Ipswitch Town":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":69},
    "West Bromwitch Albion":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":71},
    "Leeds United":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":73},
    "Southhampton":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":73},
    "Hull City":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":70},
    "Preston North End":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":70},
    "Cardiff City":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":70},
    "Middlesborough":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":71},
    "Sunderland":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":69},
    "Blackburn Rovers":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":69},
    "Watford":{"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":70},
    },},
}

commentary = {
  "miss":[],
  "goal":[],
  "end":[],
  "start":[],
}
def initcom():
  global commentary
  for i in commentary:
    with open((i+".txt"), mode = "r") as file:
      commentary[i] = file.readlines()
timings = {
  "matchintervals":1,
  "attmatchend":3,
  "normatchend":0.05,
}

# def initleague(league):
#   table = {}
#   for i in league:
#     table[i] = basedict
#     table[i]["rating"] = league[i]
#   return table
# def pickleague(leaguechoice):
#   global epl, ech
#   if leaguechoice == "y":
#     epl = initleague(initepl)
#     ech = initleague(initech)
#   else:
#     epl = initleague(initepl)
def simmatch(team1,team2,league,spectating):
  watching = team1 in spectating or team2 in spectating
  league[team1]["played"] += 1
  league[team2]["played"] += 1
  score1 = {}
  score2 = {}
  if watching:
    commentpick = random.choice(commentary["start"])
    print(f"Attending Matchday: {team1} vs {team2}.\n\n{commentpick}")
  for i in range(1,10):
    if watching:
      time.sleep(timings["matchintervals"])
    opquality = random.randint(0,180)
    chance1 = random.randint(0,league[team1]["rating"])
    chance2 = random.randint(0,league[team2]["rating"])
    minutes = random.randint((i*10)-9, i*10)
    if chance1 > chance2 and chance1 >= opquality:
      score1[minutes] = 1
      league[team1]["gf"] += 1
      league[team2]["ga"] += 1
      if watching:
        commentpick = random.choice(commentary["goal"])
        print(f"[{minutes}] GOAL! {team1} scores! {commentpick}\n {team1} {len(score1)} - {len(score2)} {team2}")
    elif chance2 > chance1 and chance2 >= opquality:
      score2[minutes] = 1
      league[team2]["gf"] += 1
      league[team1]["ga"] += 1
      if watching:
        commentpick = random.choice(commentary["goal"])
        print(f"[{minutes}] GOAL! {team2} scores! {commentpick}\n {team1} {len(score1)} - {len(score2)} {team2}")
    elif chance1 > chance2 and chance1 < opquality and watching and random.randint(0,3) == 1:
      commentpick = random.choice(commentary["miss"])
      print(f"[{minutes}] {commentpick} ({team1})")
    elif chance2 > chance1 and chance2 < opquality and watching and random.randint(0,3) == 1:
      commentpick = random.choice(commentary["miss"])
      print(f"[{minutes}] {commentpick} ({team2})")
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
  print("Team Name|Points|Played|Goal Difference|Goals For|Goals Against|Rating|")
  for i in table:
    print(i,table[i]["points"],table[i]["played"],table[i]["gd"],table[i]["gf"],table[i]["ga"],table[i]["rating"])
def generatefixtures(league):
  fixtures = {}
  bowl = list(league.keys())
  for weeks in league:
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
    "epl":24,
    "ech":24,
  }
  for week in range(seasonlength[lstr]):
    lfixtures[week] = generatefixtures(lname)
  return lfixtures
def updaterating(league):
  for team in league:
    league[team]["rating"] += round((league[team]["gd"]/4) + (league[team]["won"]/2))
    if league[team]["rating"] < 30:
      league[team]["rating"] = 30
  return league
def resetleague(league):
  for i in league:
    league[i]["points"], league[i]["played"], league[i]["won"], league[i]["lost"], league[i]["drawn"],  league[i]["gd"], league[i]["gf"], league[i]["ga"] = 0,0,0,0,0,0,0,0
  return league
def findtop(league):
  # temporary solution
  templeague = league.copy()
  templeague["Temp"], templeague["temp"] = {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":0}, {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":0}
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
  templeague["Temp"], templeague["temp"] = {"points":9999,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":0}, {"points":9999,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":0}
  top = ["Temp","temp"]
  for j in range(2):
    for i in templeague:
      if templeague[i]["points"] < templeague[top[j]]["points"]:
        top[j] = i
    templeague.pop(top[j])
  return top
def updown(relegated, promoted, topl, botl):
  for i in relegated:
    botl[i] = {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":topl[i]["rating"]}
    topl.pop(i)
  for i in promoted:
    topl[i] = {"points":0,"played":0,"won":0,"drawn":0,"lost":0,"gf":0,"ga":0,"gd":0,"rating":botl[i]["rating"]}
    botl.pop(i)
  return botl, topl
def main():
  epl = leagues["england"]["epl"]
  ech = leagues["england"]["ech"]
  morespec = "y"
  runitback = "y"
  initcom()
  while runitback.lower() == "y":
    epl = resetleague(epl)
    ech = resetleague(ech)
    eplfixtures = weekbyweek(epl,"epl")
    echfixtures = weekbyweek(ech,"ech")
    spectating = []
    while morespec.lower() == "y":
      spectating.append(input("Input a team to spectate."))
      morespec = input("Add another team? y/n")
    for i in eplfixtures:
      for match in eplfixtures[i]:
        simmatch(match,eplfixtures[i][match],epl,spectating)
      with open("epl.txt", mode = "w") as file:
        file.write(str(epl))
    for i in echfixtures:
      for match in echfixtures[i]:
        simmatch(match,echfixtures[i][match],ech,spectating)
      with open("ech.txt", mode = "w") as file:
        file.write(str(ech))
    epl = updaterating(epl)
    ech = updaterating(ech)
    print("###############################\nEnglish Premier League")
    printtable(epl)
    print("###############################\nEFL Championship")
    printtable(ech)
    relegated = findbottom(epl)
    promoted = findtop(ech)
    ech, epl = updown(relegated, promoted, epl, ech)
    runitback = input("Simulate another season?")
if __name__ == "__main__":
  main()