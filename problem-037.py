# Define a function that recieves a list of all primes < n, and a
# number n for which you are checking for primality
def is_prime(primes, n):

    # Iterate over all prime values in the prime list
    for prime in primes:

        # If n is evenly divisble by a prime value
        # then it is not itself a prime value and return false
        if n % prime == 0:
            return False

     # If n is not evenly divisble by any of the lower prime
     # values then, it is itself a prime number and return true
    return True

# Define a function that receives a list of all primes < n, and a
# number n for which you are checking for truncatablilty
def is_truncatable(primes, n):

    # Check if trunctable by dropping left digits
    for i in range(0, len(str(n))):
        subvalue = str(n)[i:len(str(n))]

        # If subvalue is not a prime then it is not truncatable
        if int(subvalue) not in primes:
            return False

    # Check if truncatable by dropping right digits
    for i in range(1, len(str(n))):
        subvalue = str(n)[0:i]
        
        # If subvalue is not a prime then it is not truncatable
        if (int(subvalue) not in primes):
            return False

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

        # Check if we have reached the 100,001 prime
        if (len(primes) == 100001):
            break

    # Count the number of truncatable primes
    count = 0
    truncatable = []

    # Iterate over all primes
    for n in primes:
        
        # Check if prime is truncatable and not 2, 3, 5, 7
        if(is_truncatable(primes, n) and n > 7):
            count += 1
            truncatable.append(n)

        # Check if we have found all 11 truncatable primes
        if(count == 11):
            break

    # Print the sum of all truncatable primes
    print(sum(truncatable))