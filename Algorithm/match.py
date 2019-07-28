class Match(object):

    def __init__(self, date, home_team, external_team, home_score, external_score):
        """ this class represents a single match, containing 2 opponents , date and match result


        :param date:
        :param home_team:
        :param external_team:
        :param home_score:
        :param external_score:
        """
        self.date = date
        self.home_team = home_team
        self.external_team = external_team
        self.home_score = home_score
        self.external_score = external_score

    def __str__(self):
        """ get the string representation for the match


        :return:
        """
        return str(self.date) + ", "+self.home_team + " : " + self.external_team + ", "+ str(self.home_score)+":"+str(self.external_score)
