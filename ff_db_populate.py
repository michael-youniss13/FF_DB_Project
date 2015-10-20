import sqlite3
from statsToDKFP import convert
import csv
#CONNECT TO DB
db = sqlite3.connect('/Users/michaelyouniss/Desktop/Coding/FF_DB_Creator/ff_db.db')
current_week = "week_6"

#DRAFTKINGS PLAYER DATA

#db.execute()
#ESPN PROJECTIONS
csvFile = open('data/'+current_week+'/espn_projections_top40QBs.csv')
quarterBackProjectionData = csv.DictReader(csvFile, delimiter=',')
for quarterBack in quarterBackProjectionData:
	name = quarterBack['Name']
	points = quarterBack['Points']
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +  "\", " + points + " )")
	
csvFile_top40rbs = open('data/'+current_week+'/espn_projections_top40RBs.csv')
top40RunningBackProjections = csv.DictReader(csvFile_top40rbs, delimiter=',')
for rb in top40RunningBackProjections:
	name = rb["0"]
	points = rb["1"]
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +" \", " + points + ")")

csvFile_top80rbs = open('data/'+current_week+'/espn_projections_top80RBs.csv')
top80RunningBackProjections = csv.DictReader(csvFile_top80rbs, delimiter=',')
for rb in top80RunningBackProjections:
	name = rb["0"]
	points = rb["1"]
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +" \", " + points + ")")

csvFile_top40wrs = open('data/'+current_week+'/espn_projections_top40WRs.csv')
top40WideReceiversProjections = csv.DictReader(csvFile_top40wrs, delimiter=',')
for wr in top40WideReceiversProjections:
	name = wr["0"]
	points = wr["1"]
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +" \", " + points + ")")

csvFile_top80wrs = open('data/'+current_week+'/espn_projections_top80WRs.csv')
top80WideReceiversProjections = csv.DictReader(csvFile_top80wrs, delimiter=',')
for wr in top80WideReceiversProjections:
	name = wr["0"]
	points = wr["1"]
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +" \", " + points + ")")

csvFile_top120wrs = open('data/'+current_week+'/espn_projections_top120WRs.csv')
top120WideReceiversProjections = csv.DictReader(csvFile_top120wrs, delimiter=',')
for wr in top120WideReceiversProjections:
	name = wr["0"]
	points = wr["1"]
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +" \", " + points + ")")

csvFile_top40tes = open('data/'+current_week+'/espn_projections_top40TEs.csv')
top40TightEndsProjections = csv.DictReader(csvFile_top40tes, delimiter=',')
for te in top40TightEndsProjections:
	name = te["0"]
	points = te["1"]
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +" \", " + points + ")")


csvFile_DST = open('data/'+current_week+'/espn_projections_dst.csv')
topDSTProjections = csv.DictReader(csvFile_DST, delimiter=',')
for dst in topDSTProjections:
	name = dst["0"]
	print name
	points = dst["1"]
	if points == "":
		points = "-10.0"
	print points
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +" \", " + points + ")")


db.commit()
db.close()


db.execute()
#EDS PROJECTIONS

db.execute()
#FANTASYPROS PROJECTIONS

db.execute()
#FANTASYSHARKS PROJECTIONS

db.execute()
#FFTODAY PROJECTIONS

db.execute()
#YAHOO PROJECTIONS

db.execute()
#NFL PROJECTIONS

db.execute()
#NUMBERFIRE PROJECTIONS

db.execute()
#CALCULATE MAX, MIN, AVG, STDEV
##Use a helper function here that will go through each row, 
##add up all the projections, average them, find the max and min and std. dev.
