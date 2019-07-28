# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import sys
from Algorithm.parse_csv_data import parse
from Algorithm.base_probability import *
from Algorithm.poisson_algo import *
from Data.TeamIdentification import *
import pandas as pd
import numpy as np
from scipy.stats import poisson
import statsmodels.api as sm
import statsmodels.formula.api as smf
import csv
from Data.writeTeamIDs import *


class AlgorithmInterface:

    # every Algorithm has an index
    # base algorithm = 0
    # poisson regression = 1
    def __init__(self):
        self.matches = []
        self.algorithmIndex = -1
        self.FirstSeason = 2009
        self.LastSeason = 2018
        self.FirstGameDay = 1
        self.LastGameDay = 34

    def setAlgorithm(self, index):
        """
        
        :param index: 
        :return: 
        """
        self.algorithmIndex = index

    def setSeasons(self, FirstSeason, LastSeason, FirstGameDay, LastGameDay):
        """
        
        :param FirstSeason: 
        :param LastSeason: 
        :param FirstGameDay: 
        :param LastGameDay: 
        :return: 
        """
        self.FirstSeason = FirstSeason
        self.LastSeason = LastSeason
        self.FirstGameDay = FirstGameDay
        self.LastGameDay = LastGameDay

    def printData(self):
        """
        
        :return: 
        """
        for i in self.matches:
            print(i)

    def processData(self, filename):
        """
        
        :param filename: 
        :return: 
        """
        self.matches = parse(filename, self.FirstSeason, self.LastSeason, self.FirstGameDay, self.LastGameDay)

    def deleteData(self):
        """
        
        :return: 
        """
        self.matches = []

    def hasMatches(self):
        """
        
        :return: 
        """
        if (self.matches != []):
            return True
        else:
            return False

    def getResult(self, HomeTeam, GuestTeam, filename):
        """
        
        :param HomeTeam: 
        :param GuestTeam: 
        :param filename: 
        :return: 
        """

        if (self.matches == []):
            sys.stderr.write("No matches given to caluculate")
        else:
            # Basis algorithm:
            if (self.algorithmIndex == 0):
                probabilities = [
                    get_probability_hometeam_wins(self.matches, get_TeamID(HomeTeam), get_TeamID(GuestTeam)),
                    get_probability_external_team_wins(self.matches, get_TeamID(HomeTeam), get_TeamID(GuestTeam)),
                    get_probability_draw(self.matches, get_TeamID(HomeTeam), get_TeamID(GuestTeam))]

            # Poisson regression, filename
            elif (self.algorithmIndex == 1):
                try:
                    probabilities = [
                        computeWinProbHome(HomeTeam, GuestTeam, filename, self.FirstSeason, self.FirstGameDay,
                                           self.LastSeason, self.LastGameDay),
                        computeWinProbAway(HomeTeam, GuestTeam, filename, self.FirstSeason, self.FirstGameDay,
                                           self.LastSeason, self.LastGameDay),
                        computeDraw(HomeTeam, GuestTeam, filename, self.FirstSeason, self.FirstGameDay, self.LastSeason,
                                    self.LastGameDay)]
                except:
                    probabilities = [1.0 / 3, 1.0 / 3, 1.0 / 3]

            else:
                sys.stderr.write("No algorithm given for the calculation")

            return probabilities

