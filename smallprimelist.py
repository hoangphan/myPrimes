import time
import sys, getopt

def smallPrimelist(n):
	assert (n>=2 and n <= (2**40)), "n must be in a small range for this program"

	b = []

	for i in range (0, n+1):
		b.append(1)

	i = 2
	while (i**2 <= n):
		for j in range (2, n//i+1):
			k = j*i 
			b[k] = 0
		while 1:
			i = i + 1
			if (b[i] == 1):
				break
	P = []
	for k in range (2, n+1):
		if b[k] == 1:
			P.append(k)
	print (P)
	print ('number of found Primes: %d' % len(P))

def proc_opt(argv):
	n = 0
	try:
		opts, args = getopt.getopt(argv, "hn:")
	except getopt.GetoptError:
		print 'smallPrimelist.py -n <end number>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'smallPrimelist.py -n <end number>'
		elif opt == '-n':
			n = int(arg)
	return n

# parsing arguments
n = proc_opt(sys.argv[1:])

if n >= 2:
	print ('we are about to list all prime number up to %d') % n
else:
	sys.exit(2)

start = time.time()

smallPrimelist(n)

print ('time takes to list prime is %s seconds' % (time.time()-start))
