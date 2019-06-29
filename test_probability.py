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

    def test_probabilities(self):
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


if __name__ == '__main__':
    unittest.main()
