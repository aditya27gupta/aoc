import re
from functools import reduce


def find_coord(row: int, col: int) -> int:
    return ((col + row - 2) * (col + row - 1) // 2) + col


def generate_num(row: int, col: int):
    start_num = 20151125
    count = find_coord(row, col)
    num = reduce(lambda c, i: (c * 252533) % 33554393, range(count - 1), start_num)
    return num


def main():
    with open("./input.txt", mode="r") as file:
        content = file.read()

    result = re.findall(r"\d+", content)
    row, col = map(int, result)
    print(generate_num(row, col))


if __name__ == "__main__":
    main()
