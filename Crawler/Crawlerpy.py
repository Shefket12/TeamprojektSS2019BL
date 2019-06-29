import requests
import json
import csv
try:
    import httplib
except:
    import http.client as httplib

class DataCrawler:

    def __init__(self, csvPath):
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
     
    def get(self, FirstSeason, LastSeason):
        csv = open(self.csvPath, "w")
        csv.write("Date" + "," + "," + "," + "HomeTeam" + "," + "AwayTeam" + "," + "GoalsHome" + "," + "GoalsAway" + "\n")
        if(self.internet_on() == False):
            raise Exception('You should check your internet connection, before you proceed')
        
        else:
            for i in range(FirstSeason, (LastSeason+1)):
                for j in range(0, 35):
                    counter = 0
                    Game = {}
                    Date = {}
                    HTID = {}
                    ATID = {}
                    GoalsHome = {}
                    GoalsHome1 = 0
                    GoalsHome2 = 0
                    GoalsAway = {}
                    GoalsAway1 = 0
                    GoalsAway2 = 0
                
                    todos = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{i}//{j}').text)
        
                    for game in (todos):
                        Game[counter] = game
                        for team in Game[counter]:
                            Date[counter] = Game[counter]['MatchDateTime']
    
                                      
                            Team1 = Game[counter]['Team1']
                            HTID[counter] = Team1['TeamId']

                            Team2 = Game[counter]['Team2']
                            ATID[counter] = Team2['TeamId']

                                    #Safe scored goals by team, by going through the list
                                    #check, if the finalscore is in Matchresults[0] or Matchresults[1]
                            Matchresults = Game[counter]['MatchResults']

                            Result = Matchresults[0]
                            GoalsHome1 = Result['PointsTeam1']
                            GoalsAway1 = Result['PointsTeam2']

                            Result = Matchresults[1]
                            GoalsHome2 = Result['PointsTeam1']
                            GoalsAway2 = Result['PointsTeam2']
                                        
                            if(GoalsHome1+GoalsAway1 >= GoalsHome2+GoalsAway2):
                                Result = Matchresults[0]
                                GoalsHome[counter] = Result['PointsTeam1']
                                GoalsAway[counter] = Result['PointsTeam2']
                            elif(GoalsHome2+GoalsAway2 > GoalsHome1+GoalsAway1):
                                Result = Matchresults[1]
                                GoalsHome[counter] = Result['PointsTeam1']
                                GoalsAway[counter] = Result['PointsTeam2']
                            
                        rowGame = Date[counter]+","+str(i)+","+str(j)+"," + str(HTID[counter]) +  "," +  str(ATID[counter]) +  "," +str(GoalsHome[counter]) + "," + str(GoalsAway[counter]) +"\n"
                            
                        csv.write(rowGame)
                        counter += 1
