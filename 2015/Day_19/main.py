import random
from typing import Dict, List, Set


class Solver:
    def __init__(self):
        self.word: str = None
        self.replacements: Dict = {}

    def parse_text(self, input_text: List[str]) -> None:
        for text in input_text:
            if "=>" in text:
                splitted_text = text.strip().split(" => ")
                self.replacements.setdefault(splitted_text[0], []).append(
                    splitted_text[1]
                )
            elif len(text) < 2:
                continue
            else:
                self.word = text.strip()

    def generate_molecules(self) -> Set:
        molecules: Set = set()

        for idx, char in enumerate(self.word):
            if char in self.replacements:
                for val in self.replacements[char]:
                    new_word = self.word[:idx] + val + self.word[idx + 1 :]
                    molecules.add(new_word)
            elif self.word[idx : idx + 2] in self.replacements:
                for val in self.replacements[self.word[idx : idx + 2]]:
                    new_word = self.word[:idx] + val + self.word[idx + 2 :]
                    molecules.add(new_word)

        return molecules

    def create_medicine(self):
        reverse = [(v, k) for k in self.replacements for v in self.replacements[k]]
        steps = 0
        target = self.word
        while target != "e":
            changed = False
            for repl, source in reverse:
                if repl in target:
                    target = target.replace(repl, source, 1)
                    steps += 1
                    changed = True
            if not changed:
                target = self.word
                random.shuffle(reverse)
                steps = 0
        return steps


def main() -> None:
    with open("./input.txt", mode="r") as file:
        input_text = file.readlines()

    solver = Solver()
    solver.parse_text(input_text)
    result = solver.generate_molecules()
    print(len(result))

    result = solver.create_medicine()
    print(result)


if __name__ == "__main__":
    main()
