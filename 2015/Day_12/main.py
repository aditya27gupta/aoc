import json
from typing import Dict, List


def parse_sum(content: Dict | List) -> int:
    total = 0
    if isinstance(content, dict):
        for val in content.values():
            if isinstance(val, int):
                total += val
            else:
                total += parse_sum(val)

    elif isinstance(content, list):
        for val in content:
            if isinstance(val, int):
                total += val
            else:
                total += parse_sum(val)

    return total


def parse_without_red_sum(content: Dict | List) -> int:
    total = 0
    if isinstance(content, dict):
        for val in content.values():
            if val == "red":
                return 0

            if isinstance(val, int):
                total += val
            else:
                total += parse_without_red_sum(val)

    elif isinstance(content, list):
        for val in content:
            if isinstance(val, int):
                total += val
            else:
                total += parse_without_red_sum(val)

    return total


def main() -> None:
    with open("./input.json", mode="r") as file:
        input_content = json.load(file)
    total_sum = parse_sum(input_content)
    print(total_sum)

    total_sum = parse_without_red_sum(input_content)
    print(total_sum)


if __name__ == "__main__":
    main()
