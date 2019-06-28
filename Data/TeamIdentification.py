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
    else: 
        return 0
