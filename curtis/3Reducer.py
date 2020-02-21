input_file = open("2.txt","r") #Opens sorted data
output_file = open("r.txt", "w") #Writes reducer results to r.txt

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

# apply the aggregation maximum function
  try:
    if(maximum < float(end_speed)):
      maximum = float(end_speed)
  except:
    maximum = end_speed

# Output the final entry when done
output_file.write(str(thisKey) + '\t' + str(maximum)+'\n')

input_file.close()
output_file.close()
print("Reducer Complete")
