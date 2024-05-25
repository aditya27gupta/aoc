from typing import List, Dict


class Solver:
    def __init__(self) -> None:
        self.var: Dict = {}

    def parser(self, sue_details: List[str]) -> None:
        for detail in sue_details:
            name, _, extra = detail.strip().partition(": ")
            for ex in extra.split(", "):
                val, count = ex.split(": ")
                self.var.setdefault(name, {})[val] = int(count)

    def check_for_sue(self, ticker: Dict):
        print(ticker)
        for name in self.var.keys():
            score = 0
            check = True
            for key, val in self.var[name].items():
                if key in ["cats", "trees"] and ticker[key] >= val:
                    check = False
                    break
                elif key in ["pomeranians", "goldfish"] and ticker[key] <= val:
                    check = False
                    break
                elif ticker[key] < val:
                    check = False
                    break
                else:
                    score += (ticker[key] - val) ** 2

            score = score**0.5
            if check:
                print(name, self.var[name], score)


def main() -> None:
    with open("./input.txt", mode="r") as file:
        sue_details = file.readlines()

    ticker = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    solver = Solver()
    solver.parser(sue_details)
    solver.check_for_sue(ticker)


if __name__ == "__main__":
    main()
