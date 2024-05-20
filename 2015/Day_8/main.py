def get_string_length(string: str) -> int:
    string = eval(string)
    length = len(string)
    return length


def get_raw_string_length(string: str) -> int:
    length = len(string)
    return length - 1


def new_encoding(string: str) -> int:
    string = string.replace("\\", "\\\\")
    string = string.replace('"', '\\"')
    length = len(string)
    return length + 1


def main() -> None:
    total_length, total_raw_length, total_new_encoding_length = 0, 0, 0
    with open("input.txt") as file:
        strings = file.readlines()

    for string in strings:
        length = get_string_length(string)
        raw_length = get_raw_string_length(string)
        new_encoding_length = new_encoding(string)

        total_length += length
        total_raw_length += raw_length
        total_new_encoding_length += new_encoding_length

    print(total_raw_length - total_length)
    print(total_new_encoding_length - total_raw_length)


if __name__ == "__main__":
    main()
