from journee import Journee
from equipe import Equipe
from championnat import Championnat
import chpt_config as config
from BeautifulSoup import BeautifulSoup as BS
import urllib2
import time

#Time measurement
start = time.clock()

# Get html content
html = urllib2.urlopen(config.url)
soup = BS(html)
chpt = Championnat()

# Discover all teams and create team_list
teams = soup.findAll('tr', {'class':'t'}) + soup.findAll('tr', {'class':'t even'})
for team in teams:
    data = team.findAll(text=True)
    team_name = data[3]
    newTeam = Equipe(team_name)
    chpt.add_team(newTeam)

# Discover and compute each journee and match
for i in range(1, config.nb_journnee+1,1):
    attr = "j%d touchcarousel-item" %i
    journee = soup.findAll('li',{'class':attr})
    day = Journee(i, journee)
    chpt.add_journee(day)



#Time measurement
end = time.clock()
print "Duration :" + "%0.2f" % (end-start) + "s"