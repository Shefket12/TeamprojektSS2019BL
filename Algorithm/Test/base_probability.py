
#return only the matches, where home_team and external_team played in the same constellation
def __find_relevant_matches(matches, home_team, external_team):
    result = []
    for match in matches:
        if((match.external_team == external_team) and (match.home_team == home_team)):
            result.append(match)
    return result


# calulates the probabilitys for the possible match outputs, based on:
# taking only games into account, where the external team and home team was playing in the same constellation
# so home team is identical to the home team to evaluate aswell as the external team
def get_probabilitys(matches, home_team, external_team):
    # get only the relevant matches, where home_team and external_team played
    relevant_matches = __find_relevant_matches(matches, home_team, external_team)

    # base probabilities are evenly distributed
    result = {"home_team": 1.0/3, "external_team": 1.0/3, "draw": 1.0/3}

    # no match found -> result will be p=1/3 for all possible outcomes since no played match exist to make a better prediction
    if(len(relevant_matches) == 0):
        return result
    else:
        home_team_wins = 0
        external_team_wins = 0
        draw = 0

        #count occurences for win, draw, loose
        for match in relevant_matches:
            if match.external_score < match.home_score:
                home_team_wins = home_team_wins + 1
            elif match.external_score > match.home_score:
                external_team_wins = external_team_wins + 1
            else:
                draw = draw + 1

        #compute probabilities
        common_part = 1.0 / (home_team_wins + external_team_wins + draw)
        result["home_team"] = home_team_wins * common_part
        result["draw"] = draw * common_part
        result["external_team"] = external_team_wins * common_part
        return result


# calculates the probability for the home team to win
def get_probability_hometeam_wins(matches, home_team, external_team):
    probabilities = get_probabilitys(matches, home_team, external_team)
    return probabilities["home_team"]


# calculates the probability for the external team to win
def get_probability_external_team_wins(matches, home_team, external_team):
    probabilities = get_probabilitys(matches, home_team, external_team)
    return probabilities["external_team"]


# calulates the probability for a draw match
def get_probability_draw(matches, home_team, external_team):
    probabilities = get_probabilitys(matches, home_team, external_team)
    return probabilities["draw"]
