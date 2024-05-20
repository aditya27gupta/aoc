class Solver:
    def __init__(self):
        self.variables = {}
        self.instructions = {}

    def parse_instructions(self, instructions) -> None:
        for instruct in instructions:
            splitted = instruct.split()
            self.instructions[splitted[-1]] = splitted[:-1]

    def solve(self, target: str) -> int:
        if target in self.variables:
            return self.variables[target]

        temp_result = self.instructions[target]
        if temp_result[1] == "->":
            result = (
                int(temp_result[0])
                if temp_result[0].isdigit()
                else self.solve(temp_result[0])
            )
            self.variables[target] = result
            return result

        elif temp_result[0] == "NOT":
            value = self.solve(temp_result[1])
            result = ~value

        elif temp_result[1] == "AND":
            value1 = (
                int(temp_result[0])
                if temp_result[0].isdigit()
                else self.solve(temp_result[0])
            )
            value2 = self.solve(temp_result[2])
            result = value1 & value2

        elif temp_result[1] == "OR":
            value1 = self.solve(temp_result[0])
            value2 = self.solve(temp_result[2])
            result = value1 | value2

        elif temp_result[1] == "LSHIFT":
            value1 = self.solve(temp_result[0])
            value2 = (
                int(temp_result[2])
                if temp_result[2].isdigit()
                else self.solve(temp_result[2])
            )
            result = value1 << value2

        elif temp_result[1] == "RSHIFT":
            value1 = self.solve(temp_result[0])
            value2 = (
                int(temp_result[2])
                if temp_result[2].isdigit()
                else self.solve(temp_result[2])
            )
            result = value1 >> value2

        self.variables[target] = result
        return result


def main():
    with open("input.txt", mode="r") as file:
        instructions = file.readlines()

    solver = Solver()
    solver.parse_instructions(instructions)
    variable_to_check = "a"
    print(solver.solve(target=variable_to_check))

    solver.variables = {}
    solver.variables["b"] = 16076
    print(solver.solve(target=variable_to_check))


if __name__ == "__main__":
    main()
