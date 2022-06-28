# Two ways to create a list:

# 1 - use the list constructor
# 2 - simpler, more common to use brackets

example = list()
example = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

print(primes)
print(primes[1])
print(primes[-1])
print(primes[2:5])

rolls = [4, 7, 2, 7, 12, 4, 7]
print(rolls)

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(numbers + letters)    # concatenation
dir(numbers)

