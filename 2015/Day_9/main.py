from typing import List, Dict
from itertools import permutations


class Solver:
    def __init__(self) -> None:
        self.path: Dict = {}

    def parse_path(self, paths: List[str]) -> None:
        for path in paths:
            path = path.split()
            dist = int(path[-1])
            city1 = path[0]
            city2 = path[2]
            self.path.setdefault(city1, {})[city2] = dist
            self.path.setdefault(city2, {})[city1] = dist

    def find_shortest_path(self) -> int:
        all_possible_paths = permutations(self.path)
        min_dist = None
        for paths in all_possible_paths:
            total_dist = 0
            for idx in range(len(paths) - 1):
                total_dist += self.path[paths[idx]][paths[idx + 1]]
            if min_dist is None or min_dist > total_dist:
                min_dist = total_dist

        return min_dist

    def find_longest_path(self) -> int:
        all_possible_paths = permutations(self.path)
        max_dist = None
        for paths in all_possible_paths:
            dist = 0
            for idx in range(len(paths) - 1):
                dist += self.path[paths[idx]][paths[idx + 1]]
            if max_dist is None or max_dist < dist:
                max_dist = dist

        return max_dist


def main():
    with open("input.txt") as file:
        paths: List[str] = file.readlines()

    solver = Solver()
    solver.parse_path(paths)
    result = solver.find_shortest_path()
    print(result)
    result = solver.find_longest_path()
    print(result)


if __name__ == "__main__":
    main()
