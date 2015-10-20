import sqlite3

db = sqlite3.connect('/Users/michaelyouniss/Desktop/Coding/FF_DB_Creator/ff_db.db')

# db.execute(''' 
# 	CREATE TABLE ff_players
# 	(
# 		Player_id int,
# 		Player_Name varchar(255),
# 		Player_Position varchar(5),
# 		Player_Opponent varchar(40),
# 		Player_Price int,
# 		Player_Projection_ESPN float, 
# 		Player_Projection_EDS float,
# 		Player_Projection_FantasySharks float,
# 		Player_Projection_FFToday float,
# 		Player_Projection_Yahoo float, 
# 		Player_Projection_NFL float, 
# 		Player_Projection_numberFire float,
# 		Player_Projection_averageProjection float,
# 		Player_Projection_maxProjection float,
# 		Player_Projection_minProjection float, 
# 		Player_Projection_stdDevInProjections float
# 	)
# 	''')
db.commit()
db.close()
