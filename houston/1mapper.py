#opens input file to read from and output file to write to
input = open("atbats.csv", "r")
output = open("01.txt", "w")

#iterates through input file and separates csv fields
for line in input:
	datalist = line.strip().split(",")
	ab_id,batter_id,event,g_id,inning,o,p_score,p_throws,pitcher_id,stand,top = datalist
	output.write(batter_id + "," + event + "\n") #writes batter_id and event variables to output file
#closes input and output files
input.close()
output.close()
