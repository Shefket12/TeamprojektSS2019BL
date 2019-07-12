#!/usr/bin/env python
# coding: utf-8

def get_TeamID(TeamName):
    if TeamName == "1. FC Nürnberg":
        return 79
    elif TeamName == "1. FSV Mainz 05":
        return 81
    elif TeamName == "Bayer Leverkusen":
        return 6
    elif TeamName == "Borussia Dortmund":
        return 7
    elif TeamName == "Borussia Mönchengladbach":
        return 87
    elif TeamName == "Eintracht Frankfurt":
        return 91
    elif TeamName == "FC Augsburg":
        return 95
    elif TeamName == "FC Bayern":
        return 40
    elif TeamName == "FC Schalke 04":
        return 9
    elif TeamName == "Fortuna Düsseldorf":
        return 185
    elif TeamName == "Hannover 96":
        return 55
    elif TeamName == "Hertha BSC":
        return 54
    elif TeamName == "RB Leipzig":
        return 1635
    elif TeamName == "SC Freiburg":
        return 112
    elif TeamName == "TSG 1899 Hoffenheim":
        return 123
    elif TeamName == "VfB Stuttgart":
        return 16
    elif TeamName == "VfL Wolfsburg":
        return 131
    elif TeamName == "Werder Bremen":
        return 134
    elif TeamName == "1. FC Union Berlin":
        return 80
    elif TeamName == "SC Paderborn 07":
        return 31
    elif TeamName == "1. FC Köln":
        return 65
    else: 
        return 0
    
    
def get_TeamName(TeamID):
    if TeamID == 79:
        return "1. FC Nürnberg"
    elif TeamID == 81:
        return "1. FSV Mainz 05"
    elif TeamID == 6:
        return "Bayer Leverkusen"
    elif TeamID == 7:
        return "Borussia Dortmund"
    elif TeamID == 87:
        return "Borussia Mönchengladbach"
    elif TeamID == 91:
        return "Eintracht Frankfurt"
    elif TeamID == 95:
        return "FC Augsburg"
    elif TeamID == 40:
        return "FC Bayern"
    elif TeamID == 9:
        return "FC Schalke 04"
    elif TeamID == 185:
        return "Fortuna Düsseldorf"
    elif TeamID == 55:
        return "Hannover 96"
    elif TeamID == 54:
        return "Hertha BSC"
    elif TeamID == 1635:
        return "RB Leipzig"
    elif TeamID == 112:
        return "SC Freiburg"
    elif TeamID == 123:
        return "TSG 1899 Hoffenheim"
    elif TeamID == 16:
        return "VfB Stuttgart"
    elif TeamID == 131:
        return "VfL Wolfsburg"
    elif TeamID == 134:
        return "Werder Bremen"
    elif TeamID == 80:
        return "1. FC Union Berlin"
    elif TeamID == 31:
        return "SC Paderborn 07"
    elif TeamID == 65:
        return "1. FC Köln"
    else: 
        return "UnknownTeam"
