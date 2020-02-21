s = open("ptss_2.txt","r")
r = open("ptss_3.txt", "w")
#initalizes variables
thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  pitch_type, start_speed = data

  if pitch_type != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(str(thisKey) + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = pitch_type
    thisValue = 0.0

# apply the aggregation function
  try:
    if(thisValue < float(start_speed)):
      thisValue = float(start_speed)
  except:
    thisValue = start_speed

# output the final entry when done
r.write(str(thisKey) + '\t' + str(thisValue)+'\n')

s.close()
r.close()
