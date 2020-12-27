# Define a function that recieves a list of all primes < n, and a
# number n for which you are checking for primality
def is_prime(primes, n):

    # Iterate over all prime values in the prime list
    for prime in primes:

        # If n is evenly divisble by a prime value
        # then it is not itself a prime value and return false */
        if n % prime == 0:
            return False

     # If n is not evenly divisble by any of the lower prime
     # values then, it is itself a prime number and return true */
    return True

if __name__ == "__main__":

    # Initialize our array of primes with the first 5 prime numbers
    primes = [2, 3, 5, 7, 11]

    # Start counting up to 1,000,000 from 12, i.e. the next largest number
    # in our prime list.
    for n in range(12, 1000000):

        # If our current number n is prime, append it to the prime list
        if(is_prime(primes, n)):
            primes.append(n)

        # Check if we have reached the 10,001 prime
        if (len(primes) == 10001):
            break

    # Print the 10,001 prime (indexed from 0)
    print(primes[10000])
