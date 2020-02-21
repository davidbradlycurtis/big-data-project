#opens input file to read from and output file to write to
s = open("02.txt", "r")
r = open("output.txt", "w")

#initializes thisKey and thisValue variables
thisKey = ""
thisValue = 0

#iterates through input file
for line in s:
	#creates variables from csv file
	data = line.strip().split(",")
	batter_id, event = data

	#checks if the event was a groundout before continuing, since only they are being counted
	if event == "Groundout":
		#checks for change in batter_id
		if batter_id != thisKey:
			#writes groundout for a player to output file
			if thisKey:
				r.write("PLAYER_ID: " + thisKey + "\t" + "GROUNDOUTS: " + str(thisValue) + "\n")
			thisKey = batter_id
			thisValue = 0
		#increments total number of groundouts
		thisValue += 1

#writes out final value to output file
r.write("PLAYER_ID: " + thisKey + "\t" + "GROUNDOUTS: " + str(thisValue)+"\n")

#closes input and output files
s.close()
r.close()
