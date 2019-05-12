import requests
import pandas as pd
import json
import time
import csv
from pandas.io.json import json_normalize

######## import the data from the website

df = pd.read_csv('http://www.openligadb.de/api/getmatchdata/bl1/2018/33')   #read the Data from the website
#df.head()                                                                   #print the head of the CSV 

r = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2018/30')
k = r.json()            #safe as JSON
#k #to print the file, to see, how it is built

######## writing values in a csv-file

download_dir = "C:\\Users\\Shefket\\Documents\\Uni\\SS19\\Teamprojekt\\BuliDaten.csv" #where you want the file to be downloaded to 
#remember to change the file, to a valid path on your computer!!

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "Team,GoalsScoredHome,GoalsScoredAway,DateOfGame\n"
csv.write(columnTitleRow)

#for key in dic.keys():
#	name = key             #safe the value at this point in this var
#	email = dic[key]       #safe the value at this point in this var
#	row = name + "," + email + "\n"  #safe the variables in this var
#	csv.write(row)         #write the used values into the csv file



######## Algorithm to get the demanded values  ---> JUST FOR ONE MATCHDAY -> MATCHDAY 30/2018/19

todos = json.loads(r.text)
counter = 0

Game = {}
Date = {}
Hometeam = {}
Awayteam = {}
GoalsHome = {}
GoalsAway = {}


# The todos has different tuples Like: [Team1:{'Name':"...",'TeamID':"...", 'ShortName':"..."}]
# To get different values we save the lists in different vars and then go through the lists in the steps after that with
# 'countable'-variables
for game in todos:
	#Safes the single games in an agile variable
    Game[counter] = game
    #games.append(game)
    for team in Game[counter]:
        #Safe the date
        Date[counter] = Game[counter]['MatchDateTime']
        
        #Safe Teamnames, by going through the list
        Team1 = Game[counter]['Team1']
        Hometeam[counter] = Team1['TeamName']
        Team2 = Game[counter]['Team2']
        Awayteam[counter] = Team2['TeamName']
        
        #Safe scored goals by team, by going through the list
        Matchresults = Game[counter]['MatchResults']
        Result = Matchresults[0]
        GoalsHome[counter] = Result['PointsTeam1']
        GoalsAway[counter] = Result['PointsTeam2']
        
    #to understand what is done here, look at the comments above @ the csv file
    #the empty string is put in, so that there can be differenciated between Home- and Awayteam
    rowHome = str(Hometeam[counter]) + "," + str(GoalsHome[counter]) + "," + ","+ str(Date[counter]) +"\n"
    csv.write(rowHome)
    rowAway = str(Awayteam[counter]) + "," + "," + str(GoalsAway[counter]) + "\n"
    csv.write(rowAway)
        
    counter +=1
    

######## printing the safed variables

#print(Date[5])
#print(Hometeam[5])
#print(Awayteam[5])
#print(GoalsHome[5])
#print(GoalsAway[5])
    #counter += 1
    #print(counter)
Game1 = Game[1]
Matchresults = Game[1]['MatchResults']
Result = Matchresults[0]
print(Matchresults)



#Game1 = todos[1]  #safe Game one from lists
#Game1['MatchID']  #get GameID from that game
	#--> These two lines show in an example what the loop above is doing

######## Algorithm to get the demanded values  ---> FOR A WHOLE SEASON ---> SEASON 18/19

h = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2017/')
g = h.json() 
Buli = json.loads(h.text)
#todos2

count = 0
Match = {}
Date = {}
Hometeam = {}
Awayteam = {}
GoalsHome = {}
GoalsAway = {}


#Match has "just" 306 Games (from 0-305) safed, becaus a Matchday has 9 Games and there are 34 of them ->9*34==306
for game in Buli:
	#Safes the single games in an agile variable
    Match[count] = game
    #for team in Match[count]:
    #games.append(game)
    for team in Match[count]:
        #Safe the date
        Date[count] = Match[count]['MatchDateTime']
        
        #Safe Teamnames, by going through the list
        Team1 = Match[count]['Team1']
        Hometeam[count] = Team1['TeamName']
        Team2 = Match[count]['Team2']
        Awayteam[count] = Team2['TeamName']
        
        #Safe scored goals by team, by going through the list
        Matchresults = Match[count]['MatchResults']
        Result = Matchresults[1]
        GoalsHome[count] = Result['PointsTeam1']
        GoalsAway[count] = Result['PointsTeam2']
           
    count +=1

    


#print(GoalsHome[0])


#print(Match[305])

# switch case, to get a team for a given value
def GetTeamName(argument):
    switcher = {
        1: "FC Bayern",
        2: "Bayer Leverkusen",
        3: "TSG 1899 Hoffenheim",
        4: "Werder Bremen",
        5: "Hertha BSC",
        6: "VfB Stuttgart",
        7: "Hamburger SV",
        8: "FC Augsburg",
        9: "1. FSV Mainz 05",
        10: "Hannover 96",
        11: "VfL Wolfsburg",
        12: "Borussia Dortmund",
        13: "FC Schalke 04",
        14: "RB Leipzig",
        15: "SC Freiburg",
        16: "Eintracht Frankfurt",
        17: "Borussia Mönchengladbach",
        18: "1. FC Köln"
    }
    print(switcher.get(argument, "Invalid Team"))
    
    
# compare a given teamname(String) to a given integer, second string will safed in var through the method 'GetTeamName'
def CompareTeamNames(TeamName, number):
    name = GetTeamName(number)
    Teamname = TeamName
    value = Teamname == name 
    return value

counter1 = 0
counter2 = 0
Team = {}
matches = 0
NumberOfTeams = 18


# going through all hometeams in the whole season
for teams in Hometeam[matches]:
    i = 1
    #print("hello13423t")
    #going through all 18 Clubs
    while i <= NumberOfTeams:
        # compare if current Club is the same as the current Hometeam
        # if so: Increase the hometeams whole seasonscore by the current score
        if(CompareTeamNames(Hometeam[matches], i)):
            print("GOODBYE")
            CurrentTeam = GetTeamName(i)
            Team["CurrentTeam"] += Hometeam[matches]
            
            counter1 +=1
            i += 1
        else:
            i += 1
            #print("hello")
    print("TEST")
    counter2 +=1


#print(countttt)
