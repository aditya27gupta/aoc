def main(input_file: str) -> int:
    with open(input_file, mode='r') as file:
        string = file.read()

    up_count = string.count('(')
    down_count = string.count(')')
    return up_count - down_count


if __name__ == "__main__":
    print(main('input.txt'))
