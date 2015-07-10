import sys
print "UPPER CASE ", sum(1 for c in ''.join(sys.argv[1:]) if c.isupper())
print "LOWER CASE  ", sum(1 for c in ''.join(sys.argv[1:]) if c.islower())