s = open("speed_se_2.txt","r")
r = open("speed_se_3.txt", "w")

thisKey = ""
max_start_speed = 0.0
min_end_speed = 100

for line in s:
  data = line.strip().split('\t')
  pitch_type, start_speed, end_speed = data

  if pitch_type != thisKey:
    if thisKey:
      # output the last results
      try:
        dif = round(float(float(max_start_speed) - float(min_end_speed)),1)
      except:
        dif = 'difference'
      r.write(str(thisKey) + '\t' + str(max_start_speed) + '\t' + str(min_end_speed) + '\t' + str(dif) + '\n')

    # start over when changing keys
    thisKey = pitch_type
    max_start_speed = 0.0
    min_end_speed = 100

  # apply the aggregation function to find max_start_speed
  try:
    if(max_start_speed < float(start_speed)):
      max_start_speed = float(start_speed)
  except:
    max_start_speed = 'max_start_speed'

  # apply the aggregation function to find min_end_speed
  try:
    if(min_end_speed > float(end_speed)):
      min_end_speed = float(end_speed)
  except:
    min_end_speed = 'min_end_speed'

# output the final entry when done
try:
  dif = round(float(float(max_start_speed) - float(min_end_speed)),1)
except:
  dif = 'difference'

r.write(str(thisKey) + '\t' + str(max_start_speed) + '\t' + str(min_end_speed) + '\t' + str(dif) + '\n')
r.write('CH - Changeup \nCU - Curveball \nEP - Eephus* \nFC - Cutter \nFF - Four-seam Fastball \nFO - Pitchout (also PO)* \nFS - Splitter \nFT - Two-seam Fastball \nIN - Intentional ball \nKC - Knuckle curve \nKN - Knuckeball \nPO - Pitchout (also FO)* \nSC - Screwball* \nSI - Sinker \nSL - Slider \nUN - Unknown*')
s.close()
r.close()
