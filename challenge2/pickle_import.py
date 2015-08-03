import pickle

try:
	with open('output.pkl', 'rb') as f:
		s = pickle.load(f)
		print s
except IOError, e:
	print 'IOError: ', e

