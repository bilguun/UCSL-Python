import sys
import numpy

if len(sys.argv) == 2:
	try:
		[x,y] = [int(i) for i in sys.argv[1].split(',')]
	
		ar = numpy.zeros((x, y))
		for i in range(1,x):
			for j in range(1,y):
				ar[i][j]=i*j

		print ar
	except ValueError:
		print "Wrong input. Input should be in a form 'x,y' and x,y must be an integer!"
	except BaseException:
		print "Some error occured, check your input!"	
else:
	print "Wrong input. Input should be in a form 'x,y' and x,y must be an integer!"