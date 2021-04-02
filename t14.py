import os
import re


class Container:
    def __init__(self, iter):
        self._container = [str(o) for o in iter]

    def add(self, vals):
        for v in vals:
            self._container.append(v)

    def remove(self, vals):
        for v in vals:
            if v in self._container:
                self._container.remove(v)

    def find(self, vals):
        for v in vals:
            if v not in self._container:
                return False
        return True

    def grep(self, pattern):
        _str = []
        for v in self._container:
            if re.search(pattern, str(v)):
                _str += v
        _str = str(_str)
        return _str[1: -1]

    def save(self, path):
        with open(path, 'w') as fp:
            fp.write(str(self))

    def load(self, path):
        with open(path, 'r') as fp:
            _str = fp.read()
        self._container = _str.replace("'", '').split(', ')

    def __repr__(self):
        _str = str(self._container)
        return _str[1:-1]


commands = ('add', 'remove', 'find', 'grep', 'save', 'load', 'quit')

def main():
    container = Container([1, 5])
    while True:
        os.system('clear')
        print('add remove find grep save load')
        print(container)
        command = input()

        if command not in commands:
            print('wrong command')
            input()
            continue

        if command == 'add':
            vals = input('values: ').split()
            container.add(vals)
        elif command == 'remove':
            vals = input('values: ').split()
            container.remove(vals)
        elif command == 'find':
            vals = input('values: ').split()
            print(container.find(vals))
            input()
        elif command == 'grep':
            regex = input('regex: ')
            try:
                print(container.grep(regex))
            except Exception as e:
                print(e)
            input()
        elif command == 'save':
            path = input('path: ')
            try:
                container.save(path)
            except Exception as e:
                print(e)
                input()
        elif command == 'load':
            path = input('path: ')
            try:
                print(container.load(path))
            except Exception as e:
                print(e)
                input()
        elif command == 'quit':
            break


if __name__ == '__main__':
    main()

