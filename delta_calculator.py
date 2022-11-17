import string
import sys
import time

d_string = raw_input("Enter date (DD/MM/YYYY): ")
d_fields = string.splitfields(d_string, "/")
n_fields = len(d_fields)

if n_fields != 3:
	print "Invalid date passed -- must be DD/MM/YYYY"
	sys.exit(2)

for i in xrange(fields):
	try:
		d_fields[i] = string.atoi(d_fields[i])
	except ValueError:
		print "Invalid date passed -- must be DD/MM/YYYY"
		sys.exit(2)

d_target = (d_fields[2], d_fields[1], d_fields[0], 0, 0, 0, 0, 0, -1)
delta = time.mktime(d_target) - time.time()

d = int(delta / 86400)
h = int(delta / 3600)
m = int(delta / 60)
s = int(delta - (mins * 60))

print d, "days,", h - (d*24), "hours,", m - (h*60), "mins,", s, "secs"
