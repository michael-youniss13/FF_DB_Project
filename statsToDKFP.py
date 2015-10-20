def convert(passingYards, passingTDs, passingInts, 
						rushingYards, rushingTDs, receptions, 
						receptionYards, receptionTDs, fumbles):
	score = 0.0
	score += float(passingYards/25.0)
	print(score)
	score += float(passingTDs*4.0)
	print(score)
	score += float(passingInts*(-1.0))
	print(score)
	score += float(rushingYards/10.0)
	print(score)
	score += float(rushingTDs*6.0)
	print(score)
	score += float(receptions)
	print(score)
	score += float(receptionYards/10.0)
	print(score)
	score += float(receptionTDs*6.0)
	print(score)
	score += float(fumbles*(-1.0))
	print(score)
	if rushingYards >= 100:
		score += 3.0
	if receptionYards >= 100:
		score += 3.0
	if passingYards >= 300:
		score += 3.0
	return score
	