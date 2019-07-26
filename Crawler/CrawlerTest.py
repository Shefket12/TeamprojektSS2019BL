#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crawler.Crawlerpy import *
import csv   


class CrawlerTest:
        
    def __init__(self, file, FirstSeason, LastSeason):
        """Create a instance to test the Crawler

        'file' must be a valid path on your computer, 'FirstSeason' and 'LastSeason' must be integers with
        'FirstSeason' >= 'LastSeason'"""
        self.filename = file
        self.Crawler = DataCrawler(self.filename)
        self.FirstSeason = FirstSeason
        self.LastSeason = LastSeason
        self.Crawler.getSeasons(self.FirstSeason, self.LastSeason)
    
    

    def checkInternet(self):
        """checks 'internet_on' method

        returns information, if device is connected to internet or not"""
        if(self.Crawler.internet_on()==True):
                print("Internet connection works")
        else:
            print("Check your internet connection")
    
        
    def checkNumOfGames(self):
        """Checks, if number of games is correct

        Counts how many games are in the csv-file and calculates, with 'FirstSeason' 
        and 'LastSeason' if the count equals a calculated number.
        If not, it returns, if there are too many or too few games"""
        counter = 0
        numOfGames = 0
        with open(self.filename)as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
    
            #counting the rows\n",
            for row in csv_reader:
                counter += 1
                
            numOfGames = ((self.LastSeason+1)-self.FirstSeason) * 34 * 9
            #first row isn't a Game
            counter -= 1
            
        if(numOfGames == counter):
            print("All fine")
        elif(numOfGames > counter): 
            print("There too few games in the file")
        else:
            print("There are too many games in the csv file")


#A way to use the Testclass
"""
from Crawler.CrawlerTest import *

Test = CrawlerTest("Data/BundesligaTest.csv", 2008,2018)
Test.checkInternet()
Test.checkNumOfGames()
"""