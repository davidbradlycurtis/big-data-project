unsorted = open("ptss_1.txt", "r")
sorted = open("ptss_2.txt", "w")

dataList = unsorted.readlines()
unsorted.close()
dataList.sort()

for line in dataList:
    #print(line)
    sorted.write(line)

sorted.close()