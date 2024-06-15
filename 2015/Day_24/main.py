from operator import mul
from functools import reduce
from itertools import combinations


def find_min_qe(weights: list[int], groups: int):
    target = sum(weights) // groups

    for length in range(1, len(weights)):
        for combo in combinations(weights, length):
            if sum(combo) == target:
                return reduce(mul, combo)


def main() -> None:
    with open("./input.txt", mode="r") as file:
        weights = file.readlines()
    weights = list(map(int, weights))

    result = find_min_qe(weights, groups=3)
    print(result)
    result = find_min_qe(weights, groups=4)
    print(result)


if __name__ == "__main__":
    main()
