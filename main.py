
def is_prime(primes_array, number):
    """
    Checks if number is prime.
    :param primes_array: list of prime numbers
    :param number: number to check
    :return: True if number is prime, False if not
    """
    if number == 2 or number == 5:
        return True
    sn = str(number)
    if sn[len(sn) - 1] == '5':
        return False
    for j in range(0, len(primes_array)):
        if primes_array[j][1] == 1:
            if number % primes_array[j][0] == 0:
                return False
    return True


def find_primes(start, end, prime_array):
    """
    Finds all prime numbers between start and end.
    :param prime_array: list of prime numbers
    :param start: start of range
    :param end: end of range
    :return: list of prime numbers
    """
    if prime_array is None:
        prime_array = []
    if start < 2:
        start = 2
    for i in range(start, end):
        if is_prime(prime_array, i):
            prime_array.append([i, 1])
        else:
            prime_array.append([i, 0])
    return prime_array

if __name__ == '__main__':
    primes = []
    for i in range(10):
        primes = find_primes(i * 100000, 100000 * (i + 1), primes)
        print(len(primes))
        print(primes)
    with open('primes.txt', 'w') as f:
        f.write(str(primes))
    print('Done')
