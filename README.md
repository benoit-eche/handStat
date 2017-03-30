# handStat
Get, save and analyse championship data from ffhb

# Aim
Get Handball championship datas from http://www.ff-handball.org/ by url
Parse and process data to construct :
- Same ranking as ff-hb
- Attack ranking
- Defense ranking

The aim is also to construct following "Day by day" information:
- General ranking
- Attack ranking
- Defense ranking
- Points numbers
- Goal (+ / - )

# Files
- main.py         : general sequencer
- chpt_config.py  : championshit configuration (nb of team, day,...)
- equipe.py       : class "team" which containt informations as point, goals,..
- journee.py      : class "day" which containt informations as match played during days and method to compute all matches
- match.py        : class which containt informations about match and method to compute results
- championnat.py  : class which containt team and day list and compute all results

# Dependency
- Python 2.7
- urllib2
- BeautifulSoup
