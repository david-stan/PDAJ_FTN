from math import sqrt

def generator_brojeva(n):
    gen = range(1, n + 1)
    return list(gen)

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i==0:
            return False
    return True

def filter_prime(l):
    return [n for n in l if is_prime(n)]


if __name__ == '__main__':
    l = generator_brojeva(20)
    l_prime = filter_prime(l)
    print(l_prime)
