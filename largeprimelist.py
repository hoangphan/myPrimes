import time
import math 
import random
import sys, getopt

# Optimal function for Modulo of a big number exponent
# based on the Fermat little theorem 
# see more detail here
# https://primes.utm.edu/notes/proofs/FermatsLittleTheorem.html

def opt_mod(a, s, n):
	assert (s >=0), "improper input to the optimize modulus function"
	if s == 0:
		return 1
	elif s==1:
		return a%n
	elif (s&0x1==0):
		y = opt_mod(a, s>>1, n)
		return (y*y) % n
	else:#s is odd
		y = opt_mod(a, (s-1)/2, n)
		return (a*y*y) % n



# Rabin Miller algorithm implementation
# to check if a big number is a Prime or not
# with the pricision of 2^(-128)
# with heavy support from Fermat little theorem (see above opt_mod function)

def rabin_miller(n):
	assert (n >=3 and n&0x1 == 1), "improper input to Rabin Miller"
	# first we compute (s, t) such that s is odd and s*2^t = n-1
	(s, t) = (n-1, 0)
	while ((s & 0x1) == 0):
		(s, t) = (s>>1, t+1)
	# we keep track of the probability of a false result in k.
	# the probability is at most 2^(-k)
	# we loop until the probability of a false result is small enough
	
	k = 0
	while k < 128:
		a = random.randrange(2, n)
		# print ('enter danger zone with a = %d') %a
		# DANGER OF EXPENSIVE COMPUTING
		v = opt_mod(a, s, n)
		if v != 1:
			i = 0
			while (v!= n-1):
				# in case we exhaust the list but doens't get what we want
				# then n is a composite number
				if i == t-1:
					return False
				else:
					#continue the sequence of v power 2
					(v, i) = (opt_mod(v, 2, n), i+1)
		k = k +2
	return True

# Generic isPrime implementation
# cover small divisors (odd number up to 1000)
# with big prime divisors, rely on the Rabin Miller algorithm (see above)

def isPrime(n):
	assert (n >=3), "input n must be greater than 3"
	p =[2]
	for i in range (1, 500):
		p.append(i*2+1)
	
	for i in range (0, 499):
		if n % p[i] == 0:
			return (p[i]==n)

	return rabin_miller(n)

# Implemenation of generating large Prime number
# base on simple idea: create a random number within a lower bound and upper bound
# then check if it is a Prime or not
# this is a very light way implementation

def genlargePrime(l, u):
	assert (l>2 and u >=l), "improper input range, check for a sensible range" 
	r = 100*(math.log(u, 2) +1)
	while 1:
		r = r-1
		assert (r > 0)
		n = random.randrange(l, u)
		# print ('now random is %d') % n
		if (isPrime(n) == True):
			break
	#print ('%d') % n
	return n


# Implementation of a processing option and arguments passing to the command line
# to improve user experience and easier to integrate into a GUI tool chain
# this is a very simple version.

def proc_opt(argv):
	n, l, u = 0, 2, 2
	try:
		opts, args = getopt.getopt(argv, "hn:l:u:", ["lowbin=", "upbin="])
	except getopt.GetoptError:
		print 'largeprimelist.py -n <num to gen> -l <lower bound> -u <upper bound>'
		print 'OR the 2nd usage'
		print 'largeprimelist.py -n <num to gen> --lowbin <lower bound of binary length> --upbin <upper bound of binary length>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'largeprimelist.py -n <num to gen> -l <lower bound> -u <upper bound>'
			print 'OR the 2nd usage'
			print 'largeprimelist.py -n <num to gen> --lowbin <lower bound of binary length> --upbin <upper bound of binary length>'
		elif opt == '-n':
			n = int(arg)
		elif opt == '-l':
			l = int(arg)
		elif opt == '-u':
			u = int(arg)
		elif opt == '--lowbin':
			l = 2**int(arg)
		elif opt == '--upbin':
			u = 2**int(arg)
	if (n <= 0 or l <=2 or u <=3): return (0,0,0)
	return n, l, u


# starting the operation
n, l, u = proc_opt(sys.argv[1:])



if (n, l, u) != (0, 0, 0):
	print ("we are about to generate %d number of primes from %d to %d"  %(n, l, u))
else: 
	sys.exit(2)

start = time.time()

P = []

for i in range (0, n):
	x = genlargePrime(l, u)
	P.append(x)

P.sort()
print P

print ('time takes to compute is %s seconds' % (time.time()-start))
