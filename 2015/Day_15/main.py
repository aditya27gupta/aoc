import re
from typing import Dict, List


class Solver:
    def __init__(self):
        self.ingredients: Dict = {}

    def parse_input(self, input_str: List[str]) -> None:
        pattern = r"[-]?\d+"
        for string in input_str:
            matches = re.findall(pattern, string)
            name: str = string.split(":")[0].strip()
            capacity: int = int(matches[0])
            durability: int = int(matches[1])
            flavor: int = int(matches[2])
            texture: int = int(matches[3])
            calories: int = int(matches[4])
            self.ingredients[name] = {
                "capacity": capacity,
                "durability": durability,
                "flavor": flavor,
                "texture": texture,
                "calories": calories,
            }

    def get_score(self, quantities: List[int]) -> int:
        if sum(quantities) != 100:
            return 0

        capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
        for idx, name in enumerate(self.ingredients.keys()):
            capacity += self.ingredients[name]["capacity"] * quantities[idx]
            durability += self.ingredients[name]["durability"] * quantities[idx]
            flavor += self.ingredients[name]["flavor"] * quantities[idx]
            texture += self.ingredients[name]["texture"] * quantities[idx]
            calories += self.ingredients[name]["calories"] * quantities[idx]

        if calories > 500:
            return 0

        return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)

    def best_score(self):
        max_score = 0
        for idx1 in range(1, 100):
            for idx2 in range(1, 100):
                for idx3 in range(1, 100):
                    quantities = [idx1, idx2, idx3, 100 - idx1 - idx2 - idx3]
                    score = self.get_score(quantities)
                    if score > max_score:
                        print(quantities)
                        max_score = score

        return max_score


def main():
    with open("./input.txt", mode="r") as file:
        input_str = file.readlines()

    solver = Solver()
    solver.parse_input(input_str)
    # print(solver.ingredients)
    result = solver.best_score()
    print(result)


if __name__ == "__main__":
    main()
