unsorted = open("ptss_1.txt", "r")
sorted = open("ptss_2.txt", "w")
#takes unsorted data and sorts it
dataList = unsorted.readlines()
unsorted.close()
dataList.sort()

for line in dataList:
    sorted.write(line)

sorted.close()