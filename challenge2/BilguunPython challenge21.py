import random
import pickle
import sys

##################################
#### READING INPUT.TXT FILE ######
##################################
lines = []
if len(sys.argv) == 2:
	try:
		with open(sys.argv[1], 'r') as f:
			lines = [line.rstrip('\n') for line in f]
	except IOError, e:
		print 'IOError: ', e


	########################################
	#### WRITING SHUFFLED PICKLE FILE ######
	########################################
	try: 
		with open('output.pkl', 'wb') as f:
			random.shuffle(lines)
			pickle.dump(lines, f)
	except IOError, e:
		print 'IOError: ', e


	########################################
	#### READING SHUFFLED PICKLE FILE BACK ######
	########################################
	try:
		with open('output.pkl', 'rb') as f:
			s = pickle.load(f)
			print s
	except IOError, e:
		print 'IOError: ', e