import re
from typing import List
from itertools import permutations


class Solver:
    def __init__(self) -> None:
        self.relations = {}

    def parse_relations(self, input_content: List[str]) -> None:
        for content in input_content:
            content = content.replace(".", "")
            match = re.findall(r"\d+", content)
            happiness = int(match[0]) * -1 if "lose" in content else int(match[0])
            first_person, *_, second_person = content.split()
            self.relations.setdefault(first_person, {})[second_person] = happiness

    def add_yourself(self) -> None:
        keys = list(self.relations.keys())
        for key in keys:
            self.relations.setdefault("You", {})[key] = 0
            self.relations[key]["You"] = 0

    def find_maximum_happiness(self) -> int:
        max_happiness = 0
        check_for = None

        all_combos = permutations(self.relations)
        for combo in all_combos:
            if check_for is None:
                check_for = combo[0]

            happiness = 0
            if check_for == combo[0]:
                for idx in range(len(combo) - 1):
                    happiness += self.relations[combo[idx]][combo[idx + 1]]
                    happiness += self.relations[combo[idx + 1]][combo[idx]]

                happiness += self.relations[check_for][combo[-1]]
                happiness += self.relations[combo[-1]][check_for]

            if happiness > max_happiness:
                max_happiness = happiness

        return max_happiness


def main() -> None:
    with open("./input.txt", mode="r") as file:
        input_text = file.readlines()

    solver = Solver()
    solver.parse_relations(input_text)
    print(solver.relations)
    result = solver.find_maximum_happiness()
    print(result)
    solver.add_yourself()
    print(solver.relations)
    result = solver.find_maximum_happiness()
    print(result)


if __name__ == "__main__":
    main()
