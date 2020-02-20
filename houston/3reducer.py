s = open("02.txt", "r")
r = open("output.txt", "w")

thisKey = ""
thisValue = 0

for line in s:
	data = line.strip().split(",")
	batter_id, event = data

	if event == "Groundout":
		if batter_id != thisKey:
			if thisKey:
				r.write("PLAYER_ID: " + thisKey + "\t" + "GROUNDOUTS: " + str(thisValue) + "\n")
			thisKey = batter_id
			thisValue = 0
		thisValue += 1

r.write("PLAYER_ID: " + thisKey + "\t" + "GROUNDOUTS: " + str(thisValue)+"\n")

s.close()
r.close()
