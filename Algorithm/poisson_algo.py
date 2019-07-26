
# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import pandas as pd
import numpy as np
from scipy.stats import poisson
import statsmodels.api as sm
import statsmodels.formula.api as smf
import csv

def replaceIDs(dataframe):
    """Replace the IDs in the dataframe with the actual teamnames

    Uses a csv-file, to exchange the IDs correctly
    'dataframe' must be a pandas dataframe"""
    teamIDs = "Data\\TeamIDs.csv"
    with open(teamIDs) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')            
        for row in csv_reader:
            dataframe['HomeTeam'].replace(int(row[0]), row[1],inplace=True)
            dataframe['AwayTeam'].replace(int(row[0]), row[1],inplace=True)


def computeTeta(filename, firstYear, firstMatchday, lastYear, lastMatchday):
    """Fitting the data to the poisson model

    Computing tetas for each team for home and away and storing them in an array
    'filename' must be a string
    'firstYear', 'firstMatchday', 'lastYear' and 'lastMatchday' must be integers"""
    data = pd.read_csv(filename)
    start = ((firstYear-2009)*306 + (firstMatchday-1)*9)
    end = (3060 - ((2018-lastYear)*306 + (34-lastMatchday)*9))
    if(end!=3060):
        data = data.drop(data.index[end:3060])
    if(start!=0):
        data = data.drop(data.index[0:start])
    replaceIDs(data)
    goal_model_data =  pd.concat([data[['HomeTeam', 'AwayTeam', 'GoalsHome']].assign(Home=1).rename(
        columns={'HomeTeam': 'Team', 'AwayTeam': 'Opponent', 'GoalsHome': 'Goals'}),data[['AwayTeam', 'HomeTeam', 'GoalsAway']].
                                  assign(Home=0).rename(columns={'AwayTeam': 'Team', 'HomeTeam': 'Opponent', 'GoalsAway': 'Goals'})])
    poisson_model = smf.glm(formula='Goals ~ Home + Team + Opponent', data=goal_model_data, family=sm.families.Poisson()).fit()
    return poisson_model

def simulateMatch(homeTeam, awayTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday):
    """Computing the probabilities in a given match

    Computes the probabilities for a certain score between two teams
    'homeTeam', 'awayTeam' and 'filename' must be strings
    'firstYear', 'firstMatchday', 'lastYear' and 'lastMatchday' must be integers"""
    max_goals=10
    poisson_model = computeTeta(filename, firstYear, firstMatchday, lastYear, lastMatchday)
    home_goals_avg = poisson_model.predict(pd.DataFrame(data={'Team': homeTeam, 
                                                            'Opponent': awayTeam,'Home':1},
                                                      index=[1])).values[0]
    away_goals_avg = poisson_model.predict(pd.DataFrame(data={'Team': awayTeam, 
                                                            'Opponent': homeTeam,'Home':0},
                                                      index=[1])).values[0]
    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in [home_goals_avg, away_goals_avg]]
    return(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))

# these methods are the same, just with different returns. Give out the probabilit for a team to win or a draw between the teams
def computeWinProbHome(HomeTeam, AwayTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday):
    """Computes the Probability, that 'HomeTeam' wins

    'HomeTeam', 'AwayTeam' and 'filename' must be strings
    'firstYear', 'firstMatchday', 'lastYear' and 'lastMatchday' must be integers"""
    game = simulateMatch(HomeTeam, AwayTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday)
    winHome = np.sum(np.tril(game, -1))
    return winHome

def computeWinProbAway(HomeTeam, AwayTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday):
    """Computes the Probability, that 'HomeTeam' wins

    'HomeTeam', 'AwayTeam' and 'filename' must be strings
    'firstYear', 'firstMatchday', 'lastYear' and 'lastMatchday' must be integers"""
    game = simulateMatch(HomeTeam, AwayTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday)
    winAway = np.sum(np.triu(game, 1))
    return winAway

def computeDraw(HomeTeam, AwayTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday):
    """Computes the Probability, that the teams draw

    'HomeTeam', 'AwayTeam' and 'filename' must be strings
    'firstYear', 'firstMatchday', 'lastYear' and 'lastMatchday' must be integers"""
    game = simulateMatch(HomeTeam, AwayTeam, filename, firstYear, firstMatchday, lastYear, lastMatchday)
    draw = np.sum(np.diag(game))
    return draw