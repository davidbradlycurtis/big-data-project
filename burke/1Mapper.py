#Get/Create data files
input_data = open("../data/pitches.csv", "r")
output_data = open("ptss_1.txt", "w")

#Iterates through the data, mapping key pitch speed (end_speed), to the value play result (type)
for line in input_data:
    datalist = line.strip().split(",")
    px,pz,start_speed,end_speed,spin_rate,spin_dir,break_angle,break_length,break_y,ax,ay,az,sz_bot,sz_top,type_confidence,vx0,vy0,vz0,x,x0,y,y0,z0,pfx_x,pfx_z,nasty,zone,code,type,pitch_type,event_num,b_score,ab_id,b_count,s_count,outs,pitch_num,on_1b,on_2b,on_3b = datalist

    #if blank skip
    #assuming data intry error only 9 inputs for FA and AB
    if(pitch_type == '' or start_speed == '' or pitch_type == 'FA' or pitch_type =='AB'): continue
    output_data.write(pitch_type + "\t" + start_speed + "\n")

input_data.close()
output_data.close()