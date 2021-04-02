def fib(n):
    a = 1
    b = 1
    for _ in range(n-2):
        a, b = a + b, a
        print(a)


def main():
    fib(66666)


if __name__ == '__main__':
    main()

