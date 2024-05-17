import re


def naught_or_not(input_string: str) -> int:
    no_words = ['ab', 'cd', 'pq', 'xy']
    no_words_check = any(
        [True if word in input_string else False for word in no_words])
    if no_words_check:
        return 0

    vowel_matches = re.findall(r'[a|e|i|o|u]', input_string, re.IGNORECASE)
    vowel_check = len(vowel_matches) >= 3

    double_match = re.findall(r'([a-z])\1', input_string, re.IGNORECASE)
    double_check = len(double_match) >= 1

    if vowel_check and double_check:
        return 1

    return 0


def new_naught_or_not(input_string: str) -> int:
    pair_matches = re.findall(r'([a-z]{2}).*\1', input_string, re.IGNORECASE)
    pair_check = len(pair_matches) >= 1

    one_between_match = re.findall(r'([a-z])\w\1', input_string, re.IGNORECASE)
    one_between_check = len(one_between_match) >= 1

    if pair_check & one_between_check:
        return 1

    return 0


def main() -> None:
    nice_strings = 0
    with open('input.txt', mode='r') as file:
        input_string = file.readlines()

    for string in input_string:
        result = naught_or_not(string)
        nice_strings += result
    print(nice_strings)

    new_nice_strings = 0
    for string in input_string:
        result = new_naught_or_not(string)
        new_nice_strings += result
    print(new_nice_strings)


if __name__ == "__main__":
    main()
