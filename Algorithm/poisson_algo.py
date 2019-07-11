
# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import pandas as pd
import numpy as np
from scipy.stats import poisson
import statsmodels.api as sm
import statsmodels.formula.api as smf
import csv

#replace the IDs of each team with their actual name, for pandas
def replaceIDs(matches, dataframe):
    teamIDs = "Data/TeamIDs.csv"
    with open(teamIDs) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')            
        for row in csv_reader:
            dataframe['HomeTeam'].replace(int(row[0]), row[1],inplace=True)
            dataframe['AwayTeam'].replace(int(row[0]), row[1],inplace=True)

def computeTeta(matches, filename):
    data = pd.read_csv(filename)
    replaceIDs(matches, data)
    goal_model_data =  pd.concat([data[['HomeTeam', 'AwayTeam', 'GoalsHome']].assign(Home=1).rename(columns={'HomeTeam': 'Team', 'AwayTeam': 'Opponent', 'GoalsHome': 'Goals'}),data[['AwayTeam', 'HomeTeam', 'GoalsAway']].assign(Home=0).rename(columns={'AwayTeam': 'Team', 'HomeTeam': 'Opponent', 'GoalsAway': 'Goals'})])
    poisson_model = smf.glm(formula='Goals ~ Home + Team + Opponent', data=goal_model_data, family=sm.families.Poisson()).fit()
    return poisson_model

# computes and Array with the probabilities for different scores between two given teams, i.e. Bayern 3-1 BVB 5,39%
def simulateMatch(matches, homeTeam, awayTeam, filename):
    max_goals=10
    poisson_model = computeTeta(matches, filename)
    home_goals_avg = poisson_model.predict(pd.DataFrame(data={'Team': homeTeam, 'Opponent': awayTeam,'Home':1},
        index=[1])).values[0]
    away_goals_avg = poisson_model.predict(pd.DataFrame(data={'Team': awayTeam, 'Opponent': homeTeam,'Home':0}, 
        index=[1])).values[0]
    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in [home_goals_avg, away_goals_avg]]
    return(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))

# these methods are the same, just with different returns. Give out the probabilit for a team to win or a draw between the teams

def computeWinProbHome(matches, HomeTeam, AwayTeam, filename):
    game = simulateMatch(matches, HomeTeam, AwayTeam, filename)
    winHome = np.sum(np.tril(game, -1))
    return winHome

def computeWinProbAway(matches, HomeTeam, AwayTeam, filename):
    game = simulateMatch(matches, HomeTeam, AwayTeam, filename)
    winAway = np.sum(np.triu(game, 1))
    return winAway

def computeDraw(matches, HomeTeam, AwayTeam, filename):
    game = simulateMatch(matches, HomeTeam, AwayTeam, filename)
    draw = np.sum(np.diag(game))
    return draw