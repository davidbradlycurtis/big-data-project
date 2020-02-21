unsorted = open("1.txt", "r")
sorted = open("2.txt", "w")

dataList = unsorted.readlines()
unsorted.close()
dataList.sort()

for line in dataList:
    sorted.write(line)

sorted.close()
print("SortShuffle Complete")