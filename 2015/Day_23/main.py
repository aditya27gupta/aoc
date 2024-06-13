class Computer:
    def __init__(self, a: int = 0):
        self.a = a
        self.b = 0

    def follow_instructions(self, instructions: list[str]):
        idx = 0
        while idx < len(instructions):
            instruction = instructions[idx].strip()
            if instruction.startswith("inc"):
                if "a" in instruction:
                    self.a += 1
                else:
                    self.b += 1
            elif instruction.startswith("tpl"):
                self.a *= 3
            elif instruction.startswith("hlf"):
                self.a = self.a // 2
            elif instruction.startswith("j"):
                if instruction.startswith("jio") and self.a != 1:
                    idx += 1
                    continue
                elif instruction.startswith("jie") and self.a % 2 != 0:
                    idx += 1
                    continue
                jump_idx = instruction.split()[-1]
                idx += int(jump_idx)
                continue

            idx += 1


def main() -> None:
    with open("./input.txt", mode="r") as file:
        input_txt = file.readlines()
    # input_txt = ["inc a", "jio a, +2", "tpl a", "inc a"]
    comp = Computer()
    comp.follow_instructions(input_txt)
    print(comp.__dict__)
    comp = Computer(1)
    comp.follow_instructions(input_txt)
    print(comp.__dict__)


if __name__ == "__main__":
    main()
