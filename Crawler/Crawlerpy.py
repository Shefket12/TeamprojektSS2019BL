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
    
    def clear(self):
        csv = open(self.csvPath, "w")
        
        
                        
    def getSeasons(self, FirstSeason, LastSeason):
        csv = open(self.csvPath, "w")
        csv.write("Date" + "," + "Season" + "," + "GameDay" +"," + "HomeTeam" + "," + "AwayTeam" + "," + "GoalsHome" + "," + "GoalsAway" + "\n")
        if(self.internet_on() == False):
            raise Exception('You should check your internet connection, before you proceed')
        
        else:
            for i in range(FirstSeason, (LastSeason+1)):
                counter = 0
                Game = {}
                
                Date = {}
                Season = {}
                GameDay = {}
                HomeTeam = {}
                AwayTeam = {}
                
                GoalsHome = {}
                GoalsHome1 = 0
                GoalsHome2 = 0
                GoalsAway = {}
                GoalsAway1 = 0
                GoalsAway2 = 0
                
                todos = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{i}').text)
        
                for game in (todos):
                    Game[counter] = game
                    for team in Game[counter]:
                        
                        Date[counter] = Game[counter]['MatchDateTime']
                        Group = Game[counter]['Group']
                        GameDay[counter] = Group['GroupOrderID']
                        
    
                                      
                        Team1 = Game[counter]['Team1']
                        HomeTeam[counter] = Team1['TeamId']

                        Team2 = Game[counter]['Team2']
                        AwayTeam[counter] = Team2['TeamId']

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
                            
                    rowGame = Date[counter]+","+str(i)+","+str(GameDay[counter])+","+ str(HomeTeam[counter])+  "," +  str(AwayTeam[counter]) +  "," +str(GoalsHome[counter]) + "," + str(GoalsAway[counter]) +"\n"
                            
                    csv.write(rowGame)
                    counter += 1
                    
    
    
    def getNextSeason(self, Season):
        i = Season
        
        csv = open(self.csvPath, "w")
        csv.write("Date" + "," + "Season" + "," + "GameDay" +"," + "HomeTeam" + "," + "AwayTeam" + "\n")
        
        if(self.internet_on() == False):
            raise Exception('You should check your internet connection, before you proceed')
        
        else:
            
            counter = 0
            Game = {}
                
            Date = {}
            Season = {}
            GameDay = {}
            HomeTeam = {}
            AwayTeam = {}
                
            todos = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{i}').text)
        
            for game in (todos):
                Game[counter] = game
                
                for team in Game[counter]:
                    Date[counter] = Game[counter]['MatchDateTime']
                    Group = Game[counter]['Group']
                    GameDay[counter] = Group['GroupOrderID']
                        
    
                                      
                    Team1 = Game[counter]['Team1']
                    HomeTeam[counter] = Team1['TeamId']

                    Team2 = Game[counter]['Team2']
                    AwayTeam[counter] = Team2['TeamId']

                            
                rowGame = Date[counter]+","+str(i)+","+str(GameDay[counter])+","+ str(HomeTeam[counter]) +  "," +  str(AwayTeam[counter]) +"\n"
                            
                csv.write(rowGame)
                counter += 1
                   
