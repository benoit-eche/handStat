import chpt_config as config
from match import Match

class Equipe():
    def __init__(self, name):
        self.name = name
        self.nospace_name = name.replace(" ", "")
        self.pos = 0
        self.pts = 0
        self.play = 0
        self.win = 0
        self.nul = 0
        self.lose = 0
        self.bplus = 0
        self.bmoins = 0
        self.diff = 0
        self.attaq_class = 0
        self.def_class = 0
        self.matches = []


    def add_match(self, match):
        if match.isplayed:
            # Get team & adv score
            if match.t1_name == self.nospace_name:
                adv_name    = match.t2_name
                team_score  = int(match.t1_score)
                adv_score   = int(match.t2_score)
            elif match.t2_name == self.nospace_name:
                adv_name    = match.t1_name
                team_score  = int(match.t2_score)
                adv_score   = int(match.t1_score)
            else:
                print("Error match don't containt current team")
                print("Current Team : %s" % self.name)
                print("Match : %s %s" % (match.t1_name,match.t2_name))
                return -1
            # Affect result
            self.play   += 1
            self.diff    = self.diff + team_score - adv_score
            self.bplus  += team_score
            self.bmoins += adv_score
            # Detect Forfait
            if adv_score == 20 and team_score == 0:
                self.pts += config.forfait_pts
                self.lose += 1
            else:
                if team_score > adv_score:
                    self.win += 1
                    self.pts += config.win_pts
                elif team_score == adv_score:
                    self.nul += 1
                    self.pts += config.nul_pts
                elif team_score < adv_score:
                    self.lose += 1
                    self.pts += config.lose_pts
                else:
                    print("Error : Unable to detect lose or wining with following score %d - %d " % (match.t1_score, match.t2_score))
                    return -2
            self.matches.append(match)
            return

    def compute_equipe(self, res):
        print "--------------------------------------"
        data = res.findAll(text=True)
        team = data[3]
        print team
        print "--------------------------------------"

    def print_team(self):
        # Name Pts  J   G   Nuls    P   But+    Buts- Diff
        print("%-35s\t%02d\t%02d\t%02d\t%02d\t%03d\t%03d\t%03d" % (self.name, self.pts, self.play, self.win, self.lose, self.bplus, self.bmoins,self.diff))


