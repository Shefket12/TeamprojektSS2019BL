import requests
import json
import csv
try:
    import httplib
except:
    import http.client as httplib

class DataCrawler:

    def __init__(self, csvPath):
        self.Matchdays = []
        self.csvPath = csvPath
	
    #method, to check the internet-connection, returning True and False as resulst
    #only the HEAD and no HTML will be fetched
    def internet_on(self):
        conn = httplib.HTTPConnection("www.ecosia.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False
        
    def clear_Matchdays(self):
        self.Matchdays = []
        
    def add_Season(self, SeasonYear, FirstMatchday, LastMatchday):
        if(self.internet_on() == False):
            raise Exception('You should check your internet connection, before you proceed')
        else:
            for i in range(FirstMatchday, LastMatchday):
                self.Matchdays.append(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{SeasonYear}//{i}'))
        
    def write_CSVFile(self):
        csv = open(self.csvPath, "w") 
  
    #the following are iterable variables, i.e.: Hometeam[1] != Hometeam[2] -> thats also the way, you call a variable
        counter = 0
        Game = {}
        Date = {}
    	HTID = {}
    	ATID = {}
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
    
                #Safe Teamnames and TeamIDs, by going through the list
                    Team1 = Game[counter]['Team1']
                    HTID[counter] = Team1['TeamId']
                
                    Team2 = Game[counter]['Team2']
                    ATID[counter] = Team2['TeamId']

                #Safe scored goals by team, by going through the list
                    Matchresults = Game[counter]['MatchResults']
                    Result = Matchresults[1]
                    GoalsHome[counter] = Result['PointsTeam1']
                    GoalsAway[counter] = Result['PointsTeam2']

            #to understand what is done here, look at the comments above @ the csv file
            #the empty string is put in, so that there can be differenciated between Home- and Awayteam    
                rowGame = Date[counter] + "," + str(HTID[counter]) +  "," +  str(ATID[counter]) +  "," +str(GoalsHome[counter]) + "," + str(GoalsAway[counter]) +"\n"
                csv.write(rowGame)

                counter += 1
                
