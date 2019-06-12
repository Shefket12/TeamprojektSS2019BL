
#return only the matches, where home_team and external_team played in the same constellation
def __find_relevant_matches(matches, home_team, external_team):
    result = []
    for match in matches:
        if((match.external_team == external_team) and (match.home_team == home_team)):
            result.append(match)
    return result


#calulates the probability for the hometeam  to win, based on:
# taking only games into account, where the external team and home team was playing in the same constellation
# so home team is identical to the home team to evaluate aswell as the external team
# the formula used: sum of all goals shot by same home_team divided by the sum of all goals shot by home + external team
def get_probability_hometeam_wins(matches, home_team, external_team):
    #get only the relevant matches, where home_team and external_team played
    relevant_matches = __find_relevant_matches(matches, home_team, external_team)

    #no match found -> result will be 50% probability since no played match exist to make a better prediction
    if(len(relevant_matches) == 0):
        return 0.5
    else:
        sum_goals_hometeam = 0
        sum_goals_external_team = 0

        #sum up all goals over all matches which are considered, for home team and external team
        for match in relevant_matches:
            sum_goals_external_team = sum_goals_external_team + match.external_score
            sum_goals_hometeam = sum_goals_hometeam + match.home_score

        #goal balance identical -> 50% chance to win
        if(sum_goals_external_team == sum_goals_hometeam):
            return 0.5

        else:
            return sum_goals_hometeam * 1.0 / (sum_goals_hometeam + sum_goals_external_team)

#calulates the probability for the external team to win : = 1 - get_probability_hometeam_wins
def get_probability_external_team_wins(matches, home_team, external_team):
    return 1.0 - get_probability_hometeam_wins(matches, home_team, external_team)


