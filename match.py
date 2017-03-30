
class Match():
    def __init__(self):
        self.t1_name = ""
        self.t1_score = ""
        self.t2_name = ""
        self.t2_score = ""
        self.date = ""
        self.arbitre = ""
        self.isplayed = False

    def print_result(self):
        #print(self.t1_name + " " + self.t1_score + "-" + self.t2_score + " " + self.t2_name)
        print("%35s %02d - %02d %-35s" %(self.t1_name, self.t1_score, self.t2_score, self.t2_name))

    def print_all(self):
        print(self.date + ": " + self.t1_name + " " + self.t1_score + "-" + self.t2_score + " " + self.t2_name + " Arbitres : " + self.arbitre)

    def compute_match(self, res):
        date = res.findChild('td', {'class':'date'}).text
        teams = res.findChild('td', {'class':'eq'})
        teamss = teams.findChildren()
        # Match not played
        if len(teamss) == 4:
            temp1 = teamss[0].text.split("-")
            temp2 = teamss[2].text.split("-")
            score_1 = score_2 = None
            self.isplayed = False
        # Match played
        elif len(teamss) == 6:
            self.isplayed = True
            temp1 = teamss[0].text.split("-")
            temp2 = teamss[3].text.split("-")
            score_1 = int(teamss[2].text)
            score_2 = int(teamss[5].text)
        self.t1_name = temp1[-1].replace(" ", "")
        self.t2_name = temp2[-1].replace(" ", "")
        self.t1_score = score_1
        self.t2_score = score_2
        self.date = date
