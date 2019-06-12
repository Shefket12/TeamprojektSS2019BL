import requests
import pandas as pd
import json
import time
import csv
from pandas.io.json import json_normalize


class DataCrawler:

    def __init__(self, csvPath):
        self.Matchdays = []
        self.csvPath = csvPath
        
    def clear_Matchdays(self):
        self.Matchdays = []
        
    def add_Season(self, SeasonYear, FirstMatchday, LastMatchday):
        for i in range(FirstMatchday, LastMatchday):
            self.Matchdays.append(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{SeasonYear}//{i}'))
        
    def write_CSVFile(self):
        csv = open(self.csvPath, "w") 
  
    #the following are iterable variables, i.e.: Hometeam[1] != Hometeam[2] -> thats also the way, you call a variable
        counter = 0
        Game = {}
        Date = {}
        Hometeam = {}
        Awayteam = {}
        GoalsHome = {}
        GoalsAway = {}

        for days in self.Matchdays:
        #todos is a local variable, that safes the current matchday
            todos = json.loads(days.text)
	
        #to write the current matchday and in the next cell the given names for the rows into the csv-file
	#this part is only for clarity reasons, if one wants to take a look at the data
        #Mday = f"Matchday{i}" + "," + "," + "," + "," + "\n"
        #csv.write(Mday)
        #columnTitleRow = "DateOfGame,HomeTeam,AwayTeam,GoalsScoredHome,GoalsScoredAway\n"
        #csv.write(columnTitleRow)
	
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
                