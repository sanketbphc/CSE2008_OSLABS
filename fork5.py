import logging

from forklib import fork_map


logging.basicConfig(level=logging.INFO)


def map_func(item):
    return item + 1


def main():
    for item in fork_map(map_func, range(20000), workers=10):
        print(item)


if __name__ == "__main__":
    main()