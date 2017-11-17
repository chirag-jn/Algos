def primes_sieve(limit):
    limitn = limit+1
    primes = [a for a in range(2,limit)]
    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

print (primes_sieve(2000))