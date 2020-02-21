unsorted = open("01.txt", "r")
sorted = open("02.txt", "w")

dataList = unsorted.readlines()
unsorted.close()
dataList.sort()

for line in dataList:
    #print(line)
    sorted.write(line)

sorted.close()