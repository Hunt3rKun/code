from Crypto.Util.number import getPrime,long_to_bytes,bytes_to_long,isPrime
import gmpy2
import libnum
c= 2782

e=1

while True:

	try:
		if(gmpy2.iroot(c,e)[1]==True):
			print(libnum.n2s(gmpy2.iroot(c,e)[0]))
			break
		e=e+1
		print(e)
	except:
		e=e+1
		print(e)
		continue