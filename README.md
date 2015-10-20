README.txt

#PROCESS FOR LOADING DATA INTO A WEEK FOLDER

##THE FOLLOWING ARE THE WEBSITES YOU WILL NEED TO GATHER THE DATA FROM:
###DraftKings
-Download all player data at beginning of wednesday

###ESPN
(Need a converter for stats -> DKPTS)
(QBS: 40, RBS: 80, WRS: 120, TES: 40, D/ST: 32)
*- QBS: http://games.espn.go.com/ffl/tools/projections?slotCategoryId=0
*- RBS: http://games.espn.go.com/ffl/tools/projections?slotCategoryId=2&startIndex=0
	http://games.espn.go.com/ffl/tools/projections?slotCategoryId=2&startIndex=40
*- WRS: http://games.espn.go.com/ffl/tools/projections?slotCategoryId=4&startIndex=0
http://games.espn.go.com/ffl/tools/projections?slotCategoryId=4&startIndex=40
http://games.espn.go.com/ffl/tools/projections?slotCategoryId=4&startIndex=80
*- TES: http://games.espn.go.com/ffl/tools/projections?slotCategoryId=6
*- D/ST: http://games.espn.go.com/ffl/tools/projections?slotCategoryId=16

###EDS Football
(Have all positions that map to DKPTS)
*-QBS: http://www.eatdrinkandsleepfootball.com/fantasy/daily-fantasy-sports/draftkings/salary-cap-analysis.html
(Go through each tab for each position)
**NOTE: excel spread sheet is available as well

###Fantasy Sharks
(have all players with DKPTS)
*-All: http://www.fantasysharks.com/apps/bert/forecasts/projections.php?League=-1&Position=92&scoring=16&Segment=537&uid=4
** NOTE: there is apossible excel file to download here

###FF Today
(Need to build some sort of converter from stats -> DKPTS)
*- QBS: http://www.fftoday.com/rankings/playerwkproj.php?Season=2015&GameWeek=6
*- RBS: Keep switching tabs to switch positions

###NFL.com
(Need to build some sort of converter from stats -> DKPTS)
QBS: http://fantasy.nfl.com/research/projections#researchProjections=researchProjections%2C%2Fresearch%2Fprojections%253Fposition%253D1%2526statCategory%253DprojectedStats%2526statSeason%253D2015%2526statType%253DweekProjectedStats%2526statWeek%253D6%2Creplace
Go through tabs for each position and through multiple pages of results. 

###Number Fire
(We have all players with DKPTS values)
All: https://www.numberfire.com/nfl/fantasy/fantasy-football-ppr-projections

###CBS Sports
(Will need to build converter for stats -> DKPTS)
QBS: http://www.cbssports.com/fantasy/football/stats/weeklyprojections/QB/6/avg/ppr
Rest: Switch through tabs

##Convertor Method:
def convert(passingYards, passingTDs, passingInts, 
							rushingYards, rushingTDs,receptions, 
							receptionYards, receptionTDs, fumbles,
							)
	All variable names are very self

	