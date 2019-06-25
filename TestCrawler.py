from CrawlerpyDaniel import *
import csv    
class CrawlerTesting:
        
    #creating a new Datacrawler
    filename = "BuliDaten.csv"
    Crawler = DataCrawler(filename)
    
    #variables for the matchdays(FirstMatchday, LastMatchday)
    Season = 2018
    FirstMatchday = 1 
    LastMatchday = 3
    
    #checking, if the internet-connection is working, seperately
    def checkInternet(self, Crawler):
        if(Crawler.internet_on()==True):
                print("Internet funktionert")
	else:
		print("Gerät ist nicht mit dem Internet verbunden")
    
    #fetching the games and saving them into an array
    def addSeasonTest(self, Crawler, Season, FirstMatchday, LastMatchday):
	Crawler.clear_Matchdays()
	Crawler.add_Season(Season, FirstMatchday, LastMatchday)
        
    #writing the fetched games into a CSVFile
    def writeNewCSVFileTest(self, Crawler):
        Crawler.write_CSVFile()
    
    #checking the number of games(if all desired games are written in the CSV-file)
    def checkNumOfGames(self, filename, LastMatchday, FirstMatchday):
        counter = 0
        numOfGames = 0
        with open(filename)as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
    
            #counting the rows\n",
            for row in csv_reader:
                counter += 1
            numOfGames = (LastMatchday-FirstMatchday) * 9
        if(numOfGames == counter):
            print("All fine")
        elif(numOfGames > counter): 
            print("There too few games in the file")
        else:
            print("There are too many games in the csv file")
