import chpt_config as config
from match import Match
from BeautifulSoup import BeautifulSoup as BS

class Journee :
    def __init__(self, number, journee):
        self.num = number
        self.matches = []
        self.compute_journee(journee)

    def add_match(self, match):
        if type(match) == type(Match()):
            self.matches.append(match)
        else:
            print("Error not match type pass as argument")
            return -1

    def print_result(self):
        for match in self.matches:
            match.print_result()

    def compute_journee(self, journee):
        # Get All Match into journee
        matches  = journee[0].findAll('table', {'class':'res  even'})
        for event in matches:
            match = Match()
            match.compute_match(event)
            self.matches.append(match)
        matchesImpair = journee[0].findAll('table', {'class':'res '})
        for event2 in matchesImpair:
            match = Match()
            match.compute_match(event2)
            self.matches.append(match)

    def print_journee(self):
        print("- Journee %02d" % self.num)
        self.print_result()

    def is_played(self):
        for match in self.matches:
            if match.isplayed:
                return True
        return False


#resevent  = soup.findAll('table', {'class':'res  even'})
#for event in resevent:
#res2match(event)