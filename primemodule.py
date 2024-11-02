def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True
    
def print_primes(x):
    for i in range(x):
        if is_prime(i):
            print(i)

def get_primes(x):
    primes = []
    for i in range(x):
        if is_prime(i):
            primes.append(i)
    return primes
