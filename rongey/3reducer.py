s = open("02.txt", "r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0

for line in s:
	data = line.strip().split(",")
	pitcher_id, event = data

	if event == "Strikeout":
		if pitcher_id != thisKey:
			if thisKey:
				r.write("PLAYER_ID: " + thisKey + "\t" + "Strikeouts: " + str(thisValue) + "\n")
			thisKey = pitcher_id
			thisValue = 0
		thisValue += 1

r.write("PLAYER_ID: " + thisKey + "\t" + "Strikeouts: " + str(thisValue)+"\n")


s.close()
r.close()






