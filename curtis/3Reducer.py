input_file = open("2.txt","r")
output_file = open("r.txt", "w")

thisKey = ""
maximum = 0.0

for line in input_file:
  data = line.strip().split('\t')
  pitch_type, end_speed = data

  if pitch_type != thisKey:
    if thisKey:
      # output the last key value pair result
      output_file.write(str(thisKey) + '\t' + str(maximum)+'\n')

    # start over when changing keys
    thisKey = pitch_type
    maximum = 0.0

# apply the aggregation function
  try:
    if(maximum < float(end_speed)):
      maximum = float(end_speed)
  except:
    maximum = end_speed

# output the final entry when done
output_file.write(str(thisKey) + '\t' + str(maximum)+'\n')

input_file.close()
output_file.close()
print("Reducer Complete")
