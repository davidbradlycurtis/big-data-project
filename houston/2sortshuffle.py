#opens input file to read from and output file to write to
unsorted = open("01.txt", "r")
sorted = open("02.txt", "w")

#sorts list of data
dataList = unsorted.readlines()
dataList.sort()

#writes sorted data to output file
for line in dataList:
	sorted.write(line)

#closes input and output files
unsorted.close()
sorted.close()
