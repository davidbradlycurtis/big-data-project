unsorted = open("1.txt", "r") #Opens mapped data
sorted = open("2.txt", "w") #Writes sorted mapped data to 2.txt

dataList = unsorted.readlines()
unsorted.close()
dataList.sort()

for line in dataList:
    sorted.write(line)

sorted.close()
print("SortShuffle Complete")
