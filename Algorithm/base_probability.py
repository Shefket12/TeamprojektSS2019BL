
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
        home_team_wins = 0
        external_team_wins = 0
        draw_teams = 0

        #sum up all goals over all matches which are considered, for home team and external team
        for match in relevant_matches:
            if match.external_score < match.home_score:
                home_team_wins = home_team_wins + 1
            elif match.external_score > match.home_score:
                external_team_wins = external_team_wins + 1
            else:
                draw_teams = draw_teams + 1

        return home_team_wins * 1.0 / (home_team_wins + external_team_wins + draw_teams)

#calulates the probability for the external team to win : = 1 - get_probability_hometeam_wins
def get_probability_external_team_wins(matches, home_team, external_team):
    # get only the relevant matches, where home_team and external_team played
    relevant_matches = __find_relevant_matches(matches, home_team, external_team)

    # no match found -> result will be 50% probability since no played match exist to make a better prediction
    if (len(relevant_matches) == 0):
        return 0.5
    else:
        home_team_wins = 0
        external_team_wins = 0
        draw_teams = 0

        # sum up all goals over all matches which are considered, for home team and external team
        for match in relevant_matches:
            if match.external_score < match.home_score:
                home_team_wins = home_team_wins + 1
            elif match.external_score > match.home_score:
                external_team_wins = external_team_wins + 1
            else:
                draw_teams = draw_teams + 1

        return external_team_wins * 1.0 / (home_team_wins + external_team_wins + draw_teams)
    
#calulates the probability for a draw
def get_probability_draw(matches, home_team, external_team):
    # get only the relevant matches, where home_team and external_team played
    relevant_matches = __find_relevant_matches(matches, home_team, external_team)

    # no match found -> result will be 50% probability since no played match exist to make a better prediction
    if (len(relevant_matches) == 0):
        return 0.5
    else:
        home_team_wins = 0
        external_team_wins = 0
        draw_teams = 0

        # sum up all goals over all matches which are considered, for home team and external team
        for match in relevant_matches:
            if match.external_score < match.home_score:
                home_team_wins = home_team_wins + 1
            elif match.external_score > match.home_score:
                external_team_wins = external_team_wins + 1
            else:
                draw_teams = draw_teams + 1

        return draw_teams * 1.0 / (home_team_wins + external_team_wins + draw_teams)
