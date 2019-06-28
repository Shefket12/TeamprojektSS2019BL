#!/usr/bin/env python
# coding: utf-8

# In[5]:


# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import sys
from Algorithm.parse_csv_data import parse
from Algorithm.base_probability import*

class ProbabilityAlgorithm:
    
    #every Algorithm has an index
    #base algorithm = 0
    #poisson regression = 1
    def __init__(self):
        self.matches = []
        self.algorithmIndex = 0
    
    def setAlgorithm(self, index):
        self.algorithmIndex = index
        print(index)
    
    def printData(self):
        for i in self.matches:
            print(i)
       
    def processData(self, filename, FirstSeason, LastSeason, FirstGameDay, LastGameDay):
        self.matches = parse(filename, FirstSeason, LastSeason, FirstGameDay, LastGameDay)
        self.printData()
        
    def deleteData(self):
        self.matches = []
        
    def getResult(self,HomeTeam, GuestTeam):
        
        if(self.matches == []):
            sys.stderr.write("No matches given to caluculate")
        else:
            # Basis algorithm:
            if(self.algorithmIndex == 0):
                probabilities = [get_probability_hometeam_wins(self.matches, HomeTeam, GuestTeam), get_probability_external_team_wins(self.matches, HomeTeam, GuestTeam), get_probability_draw(self.matches, HomeTeam, GuestTeam)]
            
            # Poisson regression
            elif(self.algorithmIndex == 1):
                print("TODO: implement Possion Regression")
            else:
                sys.stderr.write("No algorithm given for the calculation")
            
            return probabilities
    
