#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crawler.Crawlerpy import *
import csv   


class CrawlerTest:
        
    #creating a new Datacrawler
    def __init__(self, file, FirstSeason, LastSeason):
        self.filename = file
        self.Crawler = DataCrawler(self.filename)
        self.FirstSeason = FirstSeason
        self.LastSeason = LastSeason
        self.Crawler.getSeasons(self.FirstSeason, self.LastSeason)
    
    #variables for the matchdays(FirstMatchday, LastMatchday)
    

    
    #checking, if the internet-connection is working, seperately
    def checkInternet(self):
        if(self.Crawler.internet_on()==True):
                print("Internet connection works")
        else:
            print("Check your internet connection")
    
        
    #writing the fetched games into a CSVFile
    
    #checking the number of games(if all desired games are written in the CSV-file)
    def checkNumOfGames(self):
        counter = 0
        numOfGames = 0
        with open(self.filename)as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
    
            #counting the rows\n",
            for row in csv_reader:
                counter += 1
                
            numOfGames = ((self.LastSeason+1)-self.FirstSeason) * 34 * 9
            #first row isnt a Game
            counter -= 1
            
        if(numOfGames == counter):
            print("All fine")
        elif(numOfGames > counter): 
            print("There too few games in the file")
        else:
            print("There are too many games in the csv file")


# In[2]:


Test = CrawlerTest("Data/BundesligaTest.csv", 2011,2018)


# In[3]:


Test.checkInternet()


# In[4]:


Test.checkNumOfGames()


# In[ ]:




