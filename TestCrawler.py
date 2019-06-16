from CrawlerpyDaniel import *
import csv    
class CrawlerTesting:
        
    #creating a new Datacrawler
    filename = "BuliDaten.csv"
    Crawler = DataCrawler(filename)
    
    #variables for the matchdays(FirstMatchday, LastMatchday)
    FirstMatchday = 1 
    LastMatchday = 3
    
    #checking, if the internet-connection is working, seperately
    Crawler.internet_on()
    
    #fetching the games and writing the into the CSV-file
    Crawler.add_Season(2018, FirstMatchday, LastMatchday)
    #Crawler.add_Season(2017, FirstMatchday, LastMatchday)
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
