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
        
    #to understand what is done here, look at the comments above
    #the empty string is put in, so that there can be differenciated between Home- and Awayteam
    rowHome = str(Hometeam[counter]) + "," + str(GoalsHome[counter]) + "," + ","+ str(Date[counter]) +"\n"
    csv.write(rowHome)
    rowAway = str(Awayteam[counter]) + "," + "," + str(GoalsAway[counter]) + "\n"
    csv.write(rowAway)
        
    counter +=1
    

######## printing the safed variables

print(Date[5])
print(Hometeam[5])
print(Awayteam[5])
print(GoalsHome[5])
print(GoalsAway[5])
    #counter += 1
    #print(counter)
Game1 = todos[5]
print(Game1['MatchID'])



#Game1 = todos[1]  #safe Game one from lists
#Game1['MatchID']  #get GameID from that game
	#--> These two lines show in an example what the loop above is doing

######## Algorithm to get the demanded values  ---> FOR A WHOLE SEASON ---> SEASON 18/19

h = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2018/')
g = h.json() 
todos2 = json.loads(h.text)
#todos2

counter2 = 0
Game2 = {}


#Game2 has "just" 306 Games (from 0-305) safed, becaus a Matchday has 9 Games and there are 34 of them ->9*34==306
for game in todos2:
	#Safes the single games in an agile variable
    Game2[counter2] = game
    counter2 +=1
    
#print(Game2[305])