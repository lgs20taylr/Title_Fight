# Use Semantic Versioning: https://semver.org/
# Ensure that new code works on Testing branch before committing to Main

import random
import time

initepl = {
  "Arsenal":83,
  "Manchester City":85,
  "Liverpool":83,
  "Aston Villa":80,
  "Tottenham Hotspur":81,
  "Manchester United":82,
  "Newcastle United":80,
  "Brighton & Hove Albion":77,
  "West Ham United":78,
  "Chelsea":80,
}
initech = {
  "Leicster City":75,
  "Ipswitch Town":69,
  "West Bromwich Albion":71,
  "Leeds United":73,
  "Southampton":73,
  "Hull City":70,
  "Preston North End":70,
  "Cardiff City":70,
  "Middlesborough":71,
  "Sunderland":69,
}
basedict = {
  "points":0,
  "played":0,
  "won":0,
  "drawn":0,
  "lost":0,
  "gf":0,
  "ga":0,
  "gd":0,
  "rating":0
}
def initleague(league):
  table = {}
  for i in league:
    table[i] = basedict
    table[i]["rating"] = league[i]
  return table
def pickleague(leaguechoice):
  global epl, ech
  if leaguechoice == "y":
    epl = initleague(initepl)
    ech = initleague(initech)
  else:
    epl = initleague(initepl)
pickleague("y")
print(epl,ech)

def match(team1,team2,league):
  score1 = {}
  score2 = {}
  for i in range(1,10):
    opquality = random.randint(0,100)
    chance1 = random.randint(0,league[team1]["rating"])
    chance2 = random.randint(0,league[team1]["rating"])
    minutes = random.randint((i*10)-10, i*10)
    if chance1 > chance2 and chance1 >= opquality:
      score1[minutes] = 1
    elif chance2 > chance1 and chance2 >= opquality:
      score2[minutes] = 1
  if len(score1) > len(score2):
    result1 = "W"
    result2 = "L"
  elif len(score2) > len(score1):
    result2 = "W"
    result1 = "L"
  else:
    result1, result2 = "D", "D"
  print(f"{result1} {team1} {len(score1)} - {len(score2)} {team2} {result2}\n{score1} - {score2}")
def main():
  pickleague("n")
  match("Chelsea","Arsenal",epl)
main()