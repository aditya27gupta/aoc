def look_and_say(input_string: str, repetitions: int) -> str:

    for repeat in range(repetitions):
        count = 0
        prev_word = None
        end_string = ""
        for word in input_string:
            if prev_word is None:
                prev_word = word

            if prev_word == word:
                count += 1
            else:
                end_string += f"{count}{prev_word}"
                count = 1
                prev_word = word

        end_string += f"{count}{word}"
        input_string = end_string

    return end_string


def main():
    with open("./input.txt", mode="r") as file:
        input_string = file.read().strip()
    num_of_times = 50
    print('"' + input_string + '"')

    result = look_and_say(input_string, num_of_times)
    print(len(result))


if __name__ == "__main__":
    main()
