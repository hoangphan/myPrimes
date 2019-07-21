def fib(n):
	a, b = 0, 1
	while a < n:
		print(a)
		a, b = b, a+b
	print ()

n = input('Tell me the end number?\n')

print ('here is the list of fibonaci number up to %d' % n)
fib(n)
