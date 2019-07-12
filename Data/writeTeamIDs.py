import csv

def writeTeamIDs():
    Teams = {79: '1.FC Nürnberg', 81: '1. FSV Mainz 05', 6: 'Bayer Leverkusen', 7: 'Borussia Dortmund', 87: 'Borussia Mönchengladbach', 
        91: 'Eintracht Frankfurt', 95: 'FC Augsburg', 40: 'FC Bayern', 9: 'FC Schalke 04', 185: 'Fortuna Düsseldorf', 
        55: 'Hannover 96', 54: 'Hertha BSC', 1635: 'RB Leipzig', 112: 'SC Freiburg', 123: 'TSG 1899 Hoffenheim', 
        16: 'Stuttgart', 131: 'VfL Wolfsburg', 134: 'Werder Bremen', 31: 'SC Paderborn 07', 80: '1. FC Union Berlin', 65: '1. FC Köln'}
    download_dir = "C:\\Users\\Shefket\\Documents\\Uni\\SS19\\Teamprojekt\\Data\\TeamIDs.csv"
    csv = open(download_dir, 'w')
    for i in Teams:
        wholeTeam = str(i) + ',' + Teams[i] + '\n'
        csv.write(wholeTeam)