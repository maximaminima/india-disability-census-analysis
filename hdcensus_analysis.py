import os
import csv
import operator
from genChart import drawGraph

header = []

f = open("discensus.csv", "r")
reader = csv.reader(f, delimiter=',')
header = next(reader)
header1 = next(reader)
header2 = next(reader)

print header
print header1
print header2
header1[6] = "Total Workers"
header1[7] = "CL"
header1[8] = "AL"
header1[9] = "HHI"
header1[10] = "OW"

disCat = []
with open("total_india_stats.csv", "wb") as ds:
	writer = csv.writer(ds, delimiter=',')
	writer.writerow(header1)

	for row in reader:
		state = row[2]
		disType = row[3]
		if state == "INDIA":
			writer.writerow(row)
		if disType != "Total disabled population":
			if disType not in disCat:
				disCat.append(disType)

	
# get the vector of disability categories 
print disCat

fr = open("discensus.csv", "r")
reader = csv.reader(fr, delimiter=',')
header = next(reader)
header1 = next(reader)
header2 = next(reader)

header1[6] = "Total Workers"
header1[7] = "CL"
header1[8] = "AL"
header1[9] = "HHI"
header1[10] = "OW"

hdataList = {}
hundataList = {}
dataList1 = []
dataList2 = []

for row in reader:
	if row[3] == "In Hearing" and row[4] == "Total" and row[5] == "Persons":
		if row[2] == "INDIA":
			hdataList[row[2]] = int("2062058")
			hundataList[row[2]] = int("2062058")
		else:
			hdataList[row[2]] = int(row[6].strip("\t"))
			hundataList[row[2]] = int(row[6].strip("\t"))

#print dataList
print hundataList
hsortedList = sorted(hdataList.items(), key=operator.itemgetter(1))
print hsortedList

for item in hsortedList:
	dataList1.append(item[0])
	dataList2.append(item[1])

stateList = dataList1
totHPopList = dataList2

del stateList[-1]
del totHPopList[-1]
drawGraph(totHPopList, stateList, "hearing_tot", 373000, 'Total hearing impaired population in India by states')

