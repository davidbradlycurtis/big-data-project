# MLB Pitching - Big Data

## Contributors 
* David Curtis
* Cole Houston
* Dylan Rogney
* Stephen Burke

## Links

## Data

## Introduction

## Data Source
* Local:
* Original: https://www.kaggle.com/pschale/mlb-pitch-data-20152018#games.csv


## Big Data Problems

#### David Curtis
  1. **The question:** For each play type(strike, ball, in-play), I will find the maximum speed of the pitch.
  2. **My Solution:** 
    1. Mapper input:  2	-6.409	-136.065	-3.995	101.14	2.28	158.78	50	5.302	4.16	10.93	55	3	C	S	FF	3	2015000001	0	0	0	1	0	0  
    2. Mapper output / Reducer input:  S 84.1  
    3. Reducer output:  S 104.2  
    4. Your chart. I will be using a bar graph, as it will be easy to see the differences in speed for each play type.  
