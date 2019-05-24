import requests
import pandas as pd
import json
import time
import csv
from pandas.io.json import json_normalize

######## import the data from the website

def getSeason(SeasonYear):
    global Matchday
    Matchday = {}
    count = 1

    #going through every single Matchday and Safe in the variable 'Matchday[i]' a single Matchday
    for i in range(1,35):
        #using a special method from python, to use a for-loop to get every single matchday
        #the special method is the 'f' in front of the website and the current matchday is in the given '{i}'
        Matchday[count] = requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{SeasonYear}//{i}')
        count += 1

        
###example, how to get a single matchday and to take a look how the data is built in a json-file

#r = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2018/30')
#k = r.json()            #safe as JSON
#k #to print the file, to see, how it is built


##### writing values in a csv-file ######


###Here you can re-write the file, delete the perviously written data and add in the next cell the new data

def clearCSVFile():
    download_dir = "C:\\Users\\Shefket\\Documents\\Uni\\SS19\\Teamprojekt\\BuliDaten.csv" #where you want the file to be downloaded to 
    #remember to change the file, to a valid path on your computer!!

    csv = open(download_dir, "w") 
    #"w" indicates that you're writing strings to the file
    #this also erases the pervious written data
    csv.close()


###how to safe and write the wanted things into the csv
#for key in dic.keys():
#	name = key             #safe the value at this point in this var
#	email = dic[key]       #safe the value at this point in this var
#	row = name + "," + email + "\n"  #safe the variables in this var
#	csv.write(row)         #write the used values into the csv file
	
	
####### Testing, if crawling worked and was safed in the right way
#k = Matchday[34].json()
#k



##### Algorithm to go through every matchday and write the data into the csv-file ######


def writeGamesInFile():
   ##### writing values in a csv-file ######

    ###Here you can re-write the file, delete the perviously written data and add in the next cell the new data

    download_dir = "C:\\Users\\Shefket\\Documents\\Uni\\SS19\\Teamprojekt\\BuliDaten.csv" #where you want the file to be downloaded to 
    #remember to change the file, to a valid path on your computer!!

    csv = open(download_dir, "w") 
    #"w" indicates that you're writing strings to the file
    #this also erases the pervious written data   
    #csv.close()
    
    
    #the following are iterable variables, i.e.: Hometeam[1] != Hometeam[2] -> thats also the way, you call a variable
    counter = 0
    Game = {}
    Date = {}
    Hometeam = {}
    Awayteam = {}
    GoalsHome = {}
    GoalsAway = {}

    for i in range(1, 35):
        #todos is a local variable, that safes the current matchday
        todos = json.loads(Matchday[i].text)
        #to write the current matchday and in the next cell the given names for the rows into the csv-file
        Mday = f"Matchday{i}" + "," + "," + "," + "," + "\n"
        csv.write(Mday)
        columnTitleRow = "DateOfGame,HomeTeam,AwayTeam,GoalsScoredHome,GoalsScoredAway\n"
        csv.write(columnTitleRow)
        # The todos has different tuples Like: [Team1:{'Name':"...",'TeamID':"...", 'ShortName':"..."}]
        # To get different values we save the lists in different vars and then go through the lists in the steps after that with
        # 'countable'-variables
        for game in todos:
            #Safes the single games in an agile variable
            Game[counter] = game
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
                Result = Matchresults[1]
                GoalsHome[counter] = Result['PointsTeam1']
                GoalsAway[counter] = Result['PointsTeam2']

            #to understand what is done here, look at the comments above @ the csv file
            #the empty string is put in, so that there can be differenciated between Home- and Awayteam    
            rowGame = str(Date[counter]) + "," + str(Hometeam[counter]) + "," + str(Awayteam[counter]) + "," +str(GoalsHome[counter]) + "," + str(GoalsAway[counter]) +"\n"
            csv.write(rowGame)

            counter += 1
