from journee import Journee
from equipe import Equipe
import chpt_config as config


class Championnat():
    def __init__(self):
        self.journees = []
        self.teams = []
        self.classByPoint = []
        self.classAttack  = []
        self.classDefense = []

    def add_journee(self, new_journee):
        self.journees.append(new_journee)
        self.compute(new_journee)

    def add_team(self, newteam):
        self.teams.append(newteam)

    def compute(self, journee):
        pts_array = []
        attaq_temp = []
        def_temp = []
        # Add match for each team
        for match in journee.matches:
            for team in self.teams:
                if match.t1_name == team.nospace_name or match.t2_name == team.nospace_name:
                    team.add_match(match)
        # Update team position
        for team in self.teams:
            pts_array.append(team.pts)
            attaq_temp.append(team.bplus)
            def_temp.append(team.bmoins)
        class_by_pts = sorted(pts_array, key=int, reverse=True)
        attaq_score = sorted(attaq_temp, key=int,reverse=True)
        def_score = sorted(def_temp, key=int)
        for team in self.teams:
            team.pos = class_by_pts.index(team.pts)+1
            team.attaq_class = attaq_score.index(team.bplus) + 1
            team.def_class = def_score.index(team.bmoins)+1
        # Class By Point ranking
        self.classByPoint = []
        for pos in range(1,config.nb_equipe+1,1):
            for team in self.teams:
                if team.pos == pos:
                    self.classByPoint.append(team.name)
        # Attack ranking
        self.classAttack = []
        for bplus in attaq_score:
            for team in self.teams:
                if team.bplus == bplus:
                    self.classAttack.append(team.name)
        # Def ranking
        self.classDefense = []
        for bmoins in def_score:
            for team in self.teams:
                if team.bmoins == bmoins:
                    self.classDefense.append(team.name)

    def print_journee(self):
        for journee in self.journees:
            journee.print_journee()

    def print_team(self):
        for team in self.teams:
            team.print_team()

    def print_rankings(self):
        print("%-35s %02s %02s %02s" % ("Name", "Cl", "At", "Df"))
        for team in self.teams:
            print("%-35s %02d %02d %02d" % (team.name, team.pos, team.attaq_class, team.def_class))

    def dbd_general(self):
        result = []
        # Create temporary championship
        tmp_chpt = Championnat()
        for team in self.teams:
            tmp_chpt.add_team(team)
        for day in self.journees:
            tmp_chpt.add_journee(day)
            result.append(tmp_chpt.classByPoint)
        return result

    def dbd_attack(self):
        result = []
        # Create temporary championship
        tmp_chpt = Championnat()
        for team in self.teams:
            tmp_chpt.add_team(team)
        for day in self.journees:
            tmp_chpt.add_journee(day)
            result.append(tmp_chpt.classAttack)
        return result

    def dbd_defense(self):
        result = []
        # Create temporary championship
        tmp_chpt = Championnat()
        for team in self.teams:
            tmp_chpt.add_team(team)
        for day in self.journees:
            tmp_chpt.add_journee(day)
            result.append(tmp_chpt.classDefense)
        return result

