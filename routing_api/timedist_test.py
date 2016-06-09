import csv
import time
import urllib, urllib2, json
import re

inCSV = 'paratransit_cb2010_pd_pairs_subset.csv'
ouCSV = 'paratransit_cb2010_dp_pairs_osrm_subset_1.csv'

input_file = open(inCSV,'r')
input_reader = csv.reader(input_file)

header = next(input_reader)
header.append('osrm_dura') #route duration, seconds
header.append('osrm_dist') #route dist, meters
header.append('osrm_rval') #route valid

outputFile = open(ouCSV,'w')
output_writer = csv.writer(outputFile)
output_writer.writerow(header)

errorCnt  = 0 #counter for errors
for line in input_reader:
	plat = line[2]
	plng = line[1]
	dlat = line[5]
	dlng = line[4]
	try:
		try:
			#print plat, plng, dlat, dlng
			url = 'https://router.project-osrm.org/route/v1/driving/' + plng +','+ plat + ';' + dlng + ',' + dlat 
			response = urllib.urlopen(url)
			data = json.loads(response.read())
			#print data
			dura = data['routes'][0]['duration']
			dist = data['routes'][0]['distance']
			#print dura, dist
			line.append(dura)
			line.append(dist)
			line.append(1)
		except:
			print '------no route for valid xy',  plat, plng, dlat, dlng
			errorCnt = errorCnt + 1	
			line.append(-99) #add commas and null geocode val
			line.append(-99)
			line.append(-1) #code for error here
	except:
		line.append(-99)
		line.append(-99)
		line.append(-2) #code for error here
	output_writer.writerow(line)

	#time.sleep(0.000001)

input_file.close()
outputFile.close()

