import csv

maleRiders = 0
femaleRiders = 0
try:
	f = open('dec-2week-2014.csv', 'r')
	reader = csv.DictReader(f)
	for i in reader:
		if int(i['gender']) == 1:
			maleRiders += 1
		elif int(i['gender']) == 2:
			femaleRiders += 1
		# print i['gender']
	print 'Number of Male Riders: ', maleRiders
	print 'Number of Female Riders:', femaleRiders
	print 'Percentage of Male Riders: ', round((maleRiders*100.0)/(maleRiders+femaleRiders),2),'%'
	print 'Percentage of Female Riders: ', round((femaleRiders*100.0)/(maleRiders+femaleRiders),2),'%'

except IOError, e:
    print 'Error: ',e
finally:
    if f:
        f.close()