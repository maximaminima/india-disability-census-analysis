import os
import csv
import sys
import operator
from genChart import drawGraph

state = sys.argv[1]

header = []

f = open("discensus.csv", "r")
read = csv.reader(f, delimiter=',')

header = next(read)
header1 = next(read)
header2 = next(read)

ldis = []

for row in read:
	if row[3] not in ldis:
		ldis.append(row[3])

print ldis 

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

maxdic = {}

for row in reader:
	if int(row[1]) > 27:
		if row[5] == 'Persons' and row[4] == 'Total':
			if row[3] in ldis and state.upper() in row[2] and row[3] != 'Total disabled population':
				maxdic[row[3]] = int(row[11]) 

sorted_maxdic = sorted(maxdic.items(), key=operator.itemgetter(1))
print sorted_maxdic
