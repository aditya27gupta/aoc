def find_last_floor(input_file: str) -> int:
    with open(input_file, mode='r') as file:
        string = file.read()

    up_count = string.count('(')
    down_count = string.count(')')
    return up_count - down_count


def find_first_bottom_floor(input_file: str) -> int:
    with open(input_file, mode='r') as file:
        content = file.read()

    total = 0
    for idx, direction in enumerate(content):
        if direction == '(':
            total += 1
        else:
            total -= 1

        if total < 0:
            return idx + 1


def main() -> None:
    result = find_last_floor('input.txt')
    print(result)
    result = find_first_bottom_floor('input.txt')
    print(result)


if __name__ == "__main__":
    main()
