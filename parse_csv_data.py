import csv
from dateutil import parser as date_parser
from match import Match


#loads the csv data stored by the crawler and extracts the matches
def parse(filename):
    result = []
    #open the csv file
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #iterate over each line
        for row in csv_reader:
            #extract the information stored in the csv
            date = date_parser.parse(row[0])
            home_team = row[1]
            external_team = row[2]
            home_score = int(row[3])
            external_score = int(row[4])
            #create a match object, containing the match information
            match = Match(date, home_team, external_team, home_score, external_score)
            result.append(match)
    return result




