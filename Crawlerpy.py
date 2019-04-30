import requests
import pandas as pd
import json
import time
from pandas.io.json import json_normalize

df = pd.read_csv('http://www.openligadb.de/api/getmatchdata/bl1/2018/33')   #read the Data from the website
#df = df[['MatchID','Team1','Team2']]
df.head()                                                                   #print the head of the CSV 



#df['API_response'] = df.apply(get_reverse_geocode_data,axis=1)
#df['API_response'].head()
        

##r = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2018/30')
##r.json()


r = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2018/30')
#r.json()
k = r.json()            #safe as JSON
df = pd.DataFrame(k)    #safe as DataFrame
df = df[['Team1']]      #keep only "Team1"

df.head()

k

todos = json.loads(r.text)
counter = 0

Game = {}
Date = {}
Hometeam = {}
Awayteam = {}
GoalsHome = {}
GoalsAway = {}

for game in todos:
    Game[counter] = game
    #games.append(game)
    for team in Game[counter]:
        #Safe the date
        Date[counter] = Game[counter]['MatchDateTime']
        #Safe Teamnames, by going through the lost
        Team1 = Game[counter]['Team1']
        Hometeam[counter] = Team1['TeamName']
        Team2 = Game[counter]['Team2']
        Awayteam[counter] = Team2['TeamName']
        #Safe scored goals by team, by going through the lost
        Matchresults = Game[counter]['MatchResults']
        Result = Matchresults[0]
        GoalsHome[counter] = Result['PointsTeam1']
        GoalsAway[counter] = Result['PointsTeam2']
        
    counter +=1
    
print(Date[0])
print(Hometeam[0])
print(Awayteam[0])
print(GoalsHome[0])
print(GoalsAway[0])
    #counter += 1
    #print(counter)
print(Game1['MatchID'])



#Game1 = todos[1]  #safe Game one from list
#Game1['MatchID']  #get GameID from that game

