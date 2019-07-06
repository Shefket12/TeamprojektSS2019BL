# !/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import codecs
import csv
from dateutil import parser as date_parser
from Algorithm.match import Match



#loads the csv data stored by the crawler and extracts the matches
def parse(filename, FirstSeason, LastSeason, FirstGameDay, LastGameDay):
    result = []
    #open the csv file
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file ,delimiter=',')
        #Skipps the first row
        next(csv_reader, None)
        #iterate over each line
        for row in csv_reader:
            
            season_year = int(row[1])
            game_day = int(row[2])
            
            #Check for "Dataselection"
            if(FirstSeason <= season_year and LastSeason >= season_year and FirstGameDay <= game_day and LastGameDay >= game_day):
            
                #extract the information stored in the csv
                date = date_parser.parse(row[0])
                home_team = str(row[3])
                external_team = str(row[4])
                home_score = int(row[5])
                external_score = int(row[6])
                #create a match object, containing the match information
                match = Match(date, home_team, external_team, home_score, external_score)
                result.append(match)
                
    return result
