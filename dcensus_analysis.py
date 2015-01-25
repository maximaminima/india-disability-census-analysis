import os
import csv

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

# for rural populace get the magnitude of each disability for male
# for rural populace get the magnitude of each disability for female
# a bar graph plot

# for urban populace get the magitude of each disability for male
# for urban populace get the magitude of each disability for female
# a bar graph plot

# analyse the co-relation between hearing and speech categorisation
