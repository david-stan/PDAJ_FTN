def generator_brojeva(n):
    gen = range(1, n + 1)
    return list(gen)

if __name__ == '__main__':
    l = generator_brojeva(5)
    print(l)
