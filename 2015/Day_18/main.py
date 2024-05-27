import numpy as np


def get_state(input_array: np.array) -> np.array:
    num_rows, num_cols = input_array.shape
    new_array = np.zeros((num_rows, num_cols)).astype(np.int8)
    for row in range(num_rows):
        for col in range(num_cols):
            r1, c1, r2, c2 = max(0, row - 1), max(0, col - 1), row + 2, col + 2
            neighbor_sum = input_array[r1:r2, c1:c2].sum() - input_array[row, col]
            if input_array[row, col] == 1 and int(neighbor_sum) not in (2, 3):
                new_array[row, col] = 0
            elif input_array[row, col] == 0 and int(neighbor_sum) == 3:
                new_array[row, col] = 1
            else:
                new_array[row, col] = input_array[row, col]
    return new_array


def main() -> None:
    with open("./input.txt", mode="r") as file:
        initial_input = file.readlines()

    initial_input = [
        list(string.strip().replace(".", "0").replace("#", "1"))
        for string in initial_input
    ]
    initial_input = np.array(initial_input).astype(np.int8)
    new_array = initial_input.copy()
    for i in range(100):
        new_array = get_state(new_array)
        new_array = new_array
    result = new_array.sum()
    print(result)

    new_array = initial_input.copy()
    for i in range(100):
        new_array[0, 0], new_array[0, -1], new_array[-1, 0], new_array[-1, -1] = (
            1,
            1,
            1,
            1,
        )
        new_array = get_state(new_array)

    new_array[0, 0], new_array[0, -1], new_array[-1, 0], new_array[-1, -1] = 1, 1, 1, 1
    result = new_array.sum()
    print(result)


if __name__ == "__main__":
    main()
