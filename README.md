# MLB Pitching - Big Data

## Contributors 
* David Curtis
* Cole Houston
* Dylan Rogney
* Stephen Burke

## Links
* Public Repo: https://github.com/davidbradlycurtis/big-data-project/blob/master/README.md
* Issues: https://github.com/davidbradlycurtis/big-data-project/issues
## Introduction
Baseball is known as the sport for stats and data nerds, due to the fact that the insane amount of recoreded stats for each game played. Our project hopes to reveal inforpant trends, patterns, and averages that are important to game of baseball. Some of these numbers we will find include the maximum end speed of different types of pitches, and most common outcome of an atbat for each pithcer in the MLB. 
## Data Source
  This data was collected from the MLB 2015-2018 regular seasons. There are five sets of structured data in csv format, and most of which have between ten and 40 columns. The entire dataset is 838mb in size with over 3 million entries. There are some holes in the data, so it will require some cleaning before consumtion. This dataset is highly valueable, as the information that can be learned could provide teams an edge over their opponents.   
  
**Links:**
* Local: https://github.com/davidbradlycurtis/big-data-project/tree/master/data
* Original: https://www.kaggle.com/pschale/mlb-pitch-data-20152018#games.csv


## Big Data Problems

#### David Curtis
  1. **The question:** For type of pitch, I will find the maximum end speed of the pitch.
  2. **My Solution:** 
    1. Mapper input:  2	-6.409	-136.065	-3.995	101.14	2.28	158.78	50	5.302	4.16	10.93	55	3	C	S	FF	3	2015000001	0	0	0	1	0	0  
    2. Mapper output / Reducer input:  PO 84.1  
    3. Reducer output:  CH	92.4  
    4. My chart: I will be using a bar graph, as it will be easy to see the differences in speed for each play type.
#### Cole Houston
  1. **The question:**  
  2. **My Solution:**  
    1. Mapper input:   
    2. Mapper output / Reducer input:  
    3. Reducer output:   
    4. My chart:  
#### Dylan Rogney
  1. **The question:**  For each pitcher, what is the most common outcome of an atbat?
  2. **My Solution:**  
    1. Mapper input:   572761	Groundout	201500001	1	1	0	L	452657	L	TRUE  
    2. Mapper output / Reducer input:  Groundout 452657 (thousdands of times with varying outcomes)  
    3. Reducer output:   Homerun 452657  
    4. My chart:  A pie chart may be interesting, it would display the most common outcomes of an atbat and which category each pitcher falls under  
#### Stephen Burke
  1. **The question:**  For each pitch type what's the max start speed?
  2. **My Solution:**  
    1. Mapper input:   0.416	2.963	92.9	84.1	2305.052	159.235	-25	3.2	23.7	7.665	34.685	-11.96	1.72	3.56	2	-6.409	-136.065	-3.995	101.14	2.28	158.78	50	5.302	4.16	10.93	55	3	C	S	FF	3	0	2015000001	0	0	0	1	0	0	0  
    2. Mapper output / Reducer input:  FF	92.9  
    3. Reducer output: AB	92.4  
    4. My chart:  Using a bar graph because I'm representing differences in catagorical data  
