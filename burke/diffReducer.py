s = open("speed_se_2.txt","r")
r = open("speed_se_3.txt", "w")

thisKey = ""
thisValue = 0.0
thatValue = 100

for line in s:
  data = line.strip().split('\t')
  pitch_type, start_speed, end_speed = data

  if pitch_type != thisKey:
    if thisKey:
      # output the last key value pair result
      #dif = int(int(thisValue) - int(thatValue))
      try:
        dif = round(float(float(thisValue) - float(thatValue)),1)
      except:
        dif = 'difference'
      r.write(str(thisKey) + '\t' + str(thisValue) + '\t' + str(thatValue) + '\t' + str(dif) + '\n')

    # start over when changing keys
    thisKey = pitch_type
    thisValue = 0.0
    thatValue = 100

# apply the aggregation function
  try:
    if(thisValue < float(start_speed)):
      thisValue = float(start_speed)
  except:
    thisValue = 'max_start_speed'

  try:
    if(thatValue > float(end_speed)):
      thatValue = float(end_speed)
  except:
    thatValue = 'min_end_speed'

# output the final entry when done
#dif = int(int(thisValue) - int(thatValue))

try:
  dif = round(float(float(thisValue) - float(thatValue)),1)
except:
  dif = 'difference'



r.write(str(thisKey) + '\t' + str(thisValue) + '\t' + str(thatValue) + '\t' + str(dif) + '\n')
r.write('CH - Changeup \nCU - Curveball \nEP - Eephus* \nFC - Cutter \nFF - Four-seam Fastball \nFO - Pitchout (also PO)* \nFS - Splitter \nFT - Two-seam Fastball \nIN - Intentional ball \nKC - Knuckle curve \nKN - Knuckeball \nPO - Pitchout (also FO)* \nSC - Screwball* \nSI - Sinker \nSL - Slider \nUN - Unknown*')
s.close()
r.close()
