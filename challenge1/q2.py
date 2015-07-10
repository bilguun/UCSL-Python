import sys

if len(sys.argv) > 1:
	try:
		ar = sorted(set(sys.argv[1:]))
		print ' '.join(ar)
	except ValueError:
		print "Wrong input. Input should be in a form 'x,y' and x,y must be an integer!"
	except BaseException:
		print "Some error occured, check your input!"	
else:
	print "Wrong input. Input should be in a form 'x,y' and x,y must be an integer!"