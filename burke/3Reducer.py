s = open("ptss_2.txt","r")
r = open("ptss_3.txt", "w")
#initalizes variables
thisKey = ""
max_start_speed = 0.0

for line in s:
  data = line.strip().split('\t')
  pitch_type, start_speed = data

  if pitch_type != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(str(thisKey) + '\t' + str(max_start_speed)+'\n')

    # start over when changing keys
    thisKey = pitch_type
    max_start_speed = 0.0

# apply the aggregation function
  try:
    if(max_start_speed < float(start_speed)):
      max_start_speed = float(start_speed)
  except:
    max_start_speed = start_speed

# output the final entry when done
r.write(str(thisKey) + '\t' + str(max_start_speed)+'\n')

s.close()
r.close()
