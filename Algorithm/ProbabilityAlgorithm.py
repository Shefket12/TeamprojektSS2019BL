
# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-


import sys
from Algorithm.parse_csv_data import parse
from Algorithm.base_probability import*
from Algorithm.poisson_algo import *
import pandas as pd
import numpy as np
from scipy.stats import poisson
import statsmodels.api as sm
import statsmodels.formula.api as smf
import csv
from Data.writeTeamIDs import *

class ProbabilityAlgorithm:
    
    #every Algorithm has an index
    #base algorithm = 0
    #poisson regression = 1
    def __init__(self):
        self.matches = []
        self.algorithmIndex = -1
    
    def setAlgorithm(self, index):
        self.algorithmIndex = index
        
    
    def printData(self):
        for i in self.matches:
            print(i)
       
    def processData(self, filename, FirstSeason, LastSeason, FirstGameDay, LastGameDay):
        self.matches = parse(filename, FirstSeason, LastSeason, FirstGameDay, LastGameDay)
        
    def deleteData(self):
        self.matches = []
    
    def hasMatches(self):
        if(self.matches != []):
            return True
        else:
            return False
        
    def getResult(self,HomeTeam, GuestTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday):
        
        if(self.matches == []):
            sys.stderr.write("No matches given to caluculate")
        else:
            # Basis algorithm:
            if(self.algorithmIndex == 0):
                probabilities = [get_probability_hometeam_wins(self.matches, HomeTeam, GuestTeam), get_probability_external_team_wins(self.matches, HomeTeam, GuestTeam), get_probability_draw(self.matches, HomeTeam, GuestTeam)]
            
            # Poisson regression, filename
            elif(self.algorithmIndex == 1):
                try:
                    probabilities = [computeWinProbHome(self.matches, HomeTeam, GuestTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday), 
                    computeWinProbAway(self.matches, HomeTeam, GuestTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday), 
                    computeDraw(self.matches, HomeTeam, GuestTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday)]
                except:
                    probabilities = [1.0/3, 1.0/3, 1.0/3]
                                
            else:
                sys.stderr.write("No algorithm given for the calculation")
            
            return probabilities
    
