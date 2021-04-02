
def cached(function):
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        ret = function(*args)
        memo[args] = ret
        return ret
    return wrapper


@cached
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print(fibonacci(25))


if __name__ == '__main__':
    main()
