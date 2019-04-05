# My second attempt at a factoring program now in Python 3

#seems to work, except some numbers are presented with a decimal...

num = int(input("Enter an integer greater than 1.  "))
factorlist = []
print()
while (num > 1):
	i=2
	while (i <= num**(.5)):		#only need to check up to
		if num%i != 0:		#and including the square root
			i = i+1
		else:
			factorlist = factorlist + [i]
			num = int(num/i)
			i = 2
	factorlist = factorlist + [num]
	num = 1

#print "Factors are %s." %(factorlist)

#how many of which primes?

primelist = []			#some empty lists
explist = []

for factor in factorlist:			#list of distinct primes
	if factor not in primelist:
		primelist.append(factor)
for prime in primelist:				#count how many of each prime there are
	explist.append(factorlist.count(prime))

#print "Primes are %s,\nExponents for those primes are %s" %(primelist, explist)

#now to rebuild the number

productstring = ''
for prime in primelist:
	num = num*(prime**explist[primelist.index(prime)])
	productstring = productstring + '(' + str(prime) + \
	 '^' + str(explist[primelist.index(prime)]) + ')'

print ("%s = %s \n" %(num, productstring))

exit()
