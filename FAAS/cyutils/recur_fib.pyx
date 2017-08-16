

async def rec_fib(long n):
	cdef long a 
	cdef long b
	cdef long i
	a, b = 1, 1
	for i in range(n-1):
		a, b = b, a + b
	return a