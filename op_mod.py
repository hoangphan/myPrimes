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

# Implementation of a processing option and arguments passing to the command line
# to improve user experience and easier to integrate into a GUI tool chain
# this is a very simple version.

def proc_opt(argv):
	a, s, n = 0, 0, 0
	try:
		opts, args = getopt.getopt(argv, "ha:s:n:")
	except getopt.GetoptError:
		print 'op_mod.py -a <base> -s <exponent> -n <modulus>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'op_mod.py -a <base> -s <exponent> -n <modulus>'
		elif opt == '-a':
			a = int(arg)
		elif opt == '-s':
			s = int(arg)
		elif opt == '-n':
			n = int(arg)
	if (a < 0 and s < 0 and n <=0): return (0,0,0)
	return a, s, n

# starting the operation
a, s, n = proc_opt(sys.argv[1:])

if (a, s, n) != (0, 0, 0):
	print ("we are about to calculate modulo %d of exponent %d base %d"  %(n, s, a))
else: 
	sys.exit(2)

start = time.time()

x = opt_mod(a, s, n)

print x

print ('time takes to compute is %s seconds' % (time.time()-start))