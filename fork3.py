from forklib import fork_map
import logging


logging.basicConfig(level=logging.INFO)


def map_func(item):
    return item + 1


def main():
    for item in fork_map(map_func, range(200), workers=10):
        print(item)


if __name__ == '__main__':
    main()