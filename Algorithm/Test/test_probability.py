import unittest
from parse_csv_data import parse
from base_probability import get_probability_hometeam_wins
from base_probability import get_probability_external_team_wins
from base_probability import get_probability_draw


data = "../example_data/BuliDaten.csv"


class TestProbabilities(unittest.TestCase):

    def setUp(self):
        # get the matches from the dataset
        self.matches = parse(data)

        # create a set of all clubs contained in the dataset
        self.clubs = set()
        for match in self.matches:
            self.clubs.add(match.home_team)
            self.clubs.add(match.external_team)

    def test_probabilities_sum1(self):
        # iterate over all clubs
        for club in self.clubs:

            # copy all clubs as opponents and remove the actual investigated club
            opponent_clubs = self.clubs.copy()
            opponent_clubs.remove(club)

            # iterate over all possible opponents
            for opponent in opponent_clubs:
                p_home_team = get_probability_hometeam_wins(self.matches, club, opponent)
                p_external_team = get_probability_external_team_wins(self.matches, club, opponent)
                p_draw = get_probability_draw(self.matches, club, opponent)
                p = p_home_team + p_external_team + p_draw

                # make sure, that the probability of win,loose,draw = 1
                self.assertEqual(1.0,  p, 'incorrect probability')

    def test_probabilities_empty_playlist(self):
        emptyMatches = set()
        # iterate over all clubs
        for club in self.clubs:
            # copy all clubs as opponents and remove the actual investigated club
            opponent_clubs = self.clubs.copy()
            opponent_clubs.remove(club)

            # iterate over all possible opponents
            for opponent in opponent_clubs:
                p_home_team = get_probability_hometeam_wins(emptyMatches, club, opponent)
                p_external_team = get_probability_external_team_wins(emptyMatches, club, opponent)
                p_draw = get_probability_draw(emptyMatches, club, opponent)
                # make sure, that the probability is 1/3 for all cases since no matches exists
                self.assertEqual(1.0 / 3,  p_home_team, 'incorrect probability')
                self.assertEqual(1.0 / 3, p_draw, 'incorrect probability')
                self.assertEqual(1.0 / 3, p_external_team, 'incorrect probability')

    def test_probabilities_unknown_club(self):
        # iterate over all clubs
        for club in self.clubs:
            unknown_club = "unknown"
            p_home_team = get_probability_hometeam_wins(self.matches, club, unknown_club)
            p_external_team = get_probability_external_team_wins(self.matches, club, unknown_club)
            p_draw = get_probability_draw(self.matches, club, unknown_club)
            # make sure, that the probability is 1/3 for all cases since the unknown club was not
            #contained in the history
            self.assertEqual(1.0 / 3, p_home_team, 'incorrect probability')
            self.assertEqual(1.0 / 3, p_draw, 'incorrect probability')
            self.assertEqual(1.0 / 3, p_external_team, 'incorrect probability')

if __name__ == '__main__':
    unittest.main()
