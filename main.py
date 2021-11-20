from math import sqrt

def number_generator(n):
    gen = range(1, n + 1)
    return list(gen)

def square_generator(num_list):
    return [
        n for n in num_list
        if sqrt(n).is_integer()
    ]

if __name__ == '__main__':
    l = number_generator(10)
    squares_list = square_generator(l)
    print(squares_list)