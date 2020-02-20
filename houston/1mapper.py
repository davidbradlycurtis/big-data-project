input = open("atbats.csv", "r")
output = open("01.txt", "w")

for line in input:
	datalist = line.strip().split(",")
	ab_id,batter_id,event,g_id,inning,o,p_score,p_throws,pitcher_id,stand,top = datalist
	output.write(batter_id + "," + event + "\n")
input.close()
output.close()
