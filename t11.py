class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


def main():
    class b(metaclass=Singleton):
        a = 1
    a = b()
    c = b()
    print(a)
    print(c)


if __name__ == '__main__':
    main()
