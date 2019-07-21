import sys, getopt

def proc_opt(argv):
	n = 0
	try:
		opts, args = getopt.getopt(argv, "hn:")
	except getopt.GetoptError:
		print 'fibonaci.py -n <end number>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'fibonaci.py -n <end number>'
		elif opt == '-n':
			n = int(arg)
	return n


def fib(n):
	a, b = 0, 1
	while a < n:
		print(a)
		a, b = b, a+b

# parsing arguments
n = proc_opt(sys.argv[1:])

print ('we are about to list all fibonaci number up to %d' % n)
fib(n)
