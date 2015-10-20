import sqlite3
from statsToDKFP import convert
import csv
#CONNECT TO DB
db = sqlite3.connect('/Users/michaelyouniss/Desktop/Coding/FF_DB_Creator/ff_db.db')
current_week = "week_6"

#DRAFTKINGS PLAYER DATA

#db.execute()
#ESPN PROJECTIONS
csvFile = open('data/'+current_week+'/espn_projections.csv')
quarterBackProjectionData = csv.DictReader(csvFile, delimiter=',')
for quarterBack in quarterBackProjectionData:
	name = quarterBack['Name']
	print(name)
	points = quarterBack['Points']
	db.execute("INSERT INTO ff_players (Player_Name, Player_Projection_ESPN) VALUES (\"" + name +  "\", " + points + " )")
	# db.execute(''' 
	# 	UPDATE ff_players SET Player_Projection_ESPN WHERE name={name}
	# 	''')
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
