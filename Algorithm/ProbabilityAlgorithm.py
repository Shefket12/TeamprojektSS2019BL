#!/usr/bin/env python
# coding: utf-8

# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import sys
from Algorithm.parse_csv_data import parse
from Algorithm.base_probability import*
import pandas as pd
import numpy as np
from scipy.stats import poisson
import statsmodels.api as sm
import statsmodels.formula.api as smf

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
           
        
    # compute tetas for both teams for poisson regression
    def computeTeta(self, filename):
        data = pd.read_csv(filename)
        goal_model_data =  pd.concat([data[['HomeTeam', 'AwayTeam', 'GoalsHome']].assign(Home=1).rename(columns={'HomeTeam': 'Team', 'AwayTeam': 'Opponent', 'GoalsHome': 'Goals'}),data[['AwayTeam', 'HomeTeam', 'GoalsAway']].assign(Home=0).rename(columns={'AwayTeam': 'Team', 'HomeTeam': 'Opponent', 'GoalsAway': 'Goals'})])
        poisson_model = smf.glm(formula='Goals ~ Home + Team + Opponent', data=goal_model_data, family=sm.families.Poisson()).fit()
        return poisson_model

    # computes and Array with the probabilities for different scores between two given teams, i.e. Bayern 3-1 BVB 5,39%
    def simulateMatch(self, homeTeam, awayTeam, filename):
        max_goals=10
        poisson_model = self.computeTeta(filename)
        home_goals_avg = poisson_model.predict(pd.DataFrame(data={'Team': homeTeam, 
                                                                'Opponent': awayTeam,'Home':1},
                                                          index=[1])).values[0]
        away_goals_avg = poisson_model.predict(pd.DataFrame(data={'Team': awayTeam, 
                                                                'Opponent': homeTeam,'Home':0},
                                                          index=[1])).values[0]
        team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in [home_goals_avg, away_goals_avg]]
        return(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))

    # these methods are the same, just with different returns. Give out the probabilit for a team to win or a draw between the teams

    def computeWinProbHome(self, HomeTeam, AwayTeam, filename):
        print(filename)
        game = self.simulateMatch(HomeTeam, AwayTeam, filename)
        winHome = np.sum(np.tril(game, -1))
        return winHome

    def computeWinProbAway(self, HomeTeam, AwayTeam, filename):
        game = self.simulateMatch(HomeTeam, AwayTeam, filename)
        winAway = np.sum(np.triu(game, 1))
        return winAway

    def computeDraw(self, HomeTeam, AwayTeam, filename):
        game = self.simulateMatch(HomeTeam, AwayTeam, filename)
        draw = np.sum(np.diag(game, -1))
        return draw
    
        
    def getResult(self,HomeTeam, GuestTeam, filename):
        
        if(self.matches == []):
            sys.stderr.write("No matches given to caluculate")
        else:
            # Basis algorithm:
            if(self.algorithmIndex == 0):
                probabilities = [get_probability_hometeam_wins(self.matches, HomeTeam, GuestTeam), get_probability_external_team_wins(self.matches, HomeTeam, GuestTeam), get_probability_draw(self.matches, HomeTeam, GuestTeam)]
            
            # Poisson regression, filename
            elif(self.algorithmIndex == 1):
                
                probabilities = [self.computeWinProbHome(HomeTeam, GuestTeam, filename), self.computeWinProbAway(HomeTeam, GuestTeam, filename), self.computeDraw(HomeTeam, GuestTeam, filename)]
                
            else:
                sys.stderr.write("No algorithm given for the calculation")
            
            return probabilities
    
