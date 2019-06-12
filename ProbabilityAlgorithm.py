#!/usr/bin/env python
# coding: utf-8

# In[5]:


# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import sys
from parse_csv_data import parse
from base_probability import*

class Algorithm:
    def __init__(self):
        self.matches = []
    
    
    def printData(self):
        for i in self.matches:
            print(i)
       
    def processData(self, filename):
        self.matches = parse(filename)

    def deleteData(self):
        self.matches = []
    
    def getBaseAlgorithm(self,HomeTeam, GuestTeam):
        if(self.matches == []):
            sys.stderr.write("No matches given to caluculate")
        else:
            probabilitys = [get_probability_hometeam_wins(self.matches, HomeTeam, GuestTeam), get_probability_external_team_wins(self.matches, HomeTeam, GuestTeam)]
            return probabilitys
    







