import numpy as np
import re


def toggle_lights(grid: np.array, instruction: str) -> np.array:
    matches = re.findall(r'\d+', instruction, re.IGNORECASE)

    x1, y1, x2, y2 = map(int, matches)
    x2, y2 = x2+1, y2+1

    if 'turn on' in instruction:
        grid[x1:x2, y1:y2] = 1

    elif 'toggle' in instruction:
        check1 = np.where(grid[x1:x2, y1:y2] == 0)
        check2 = np.where(grid[x1:x2, y1:y2] == 1)
        grid[x1:x2, y1:y2][check1] = 1
        grid[x1:x2, y1:y2][check2] = 0

    else:
        grid[x1:x2, y1:y2] = 0

    return grid


def toggle_brightness(grid: np.array, instruction: str) -> np.array:
    matches = re.findall(r'\d+', instruction, re.IGNORECASE)

    x1, y1, x2, y2 = map(int, matches)
    x2, y2 = x2+1, y2+1

    if 'turn on' in instruction:
        grid[x1:x2, y1:y2] += 1

    elif 'toggle' in instruction:
        grid[x1:x2, y1:y2] += 2

    else:
        grid[x1:x2, y1:y2] -= 1

    grid = np.where(grid < 0, 0, grid)

    return grid


def main() -> None:
    grid = np.zeros((1_000, 1_000), dtype=np.int8)

    with open('input.txt', mode='r') as file:
        instructions: list = file.read().split('\n')

    for instruct in instructions:
        if len(instruct) < 1:
            continue
        grid = toggle_lights(grid=grid, instruction=instruct)

    total_lights_on: int = np.sum(grid)
    print(total_lights_on)

    grid = np.zeros((1_000, 1_000), dtype=np.int8)

    for instruct in instructions:
        if len(instruct) < 1:
            continue
        grid = toggle_brightness(grid=grid, instruction=instruct)

    total_brightness: int = np.sum(grid)
    print(total_brightness)


if __name__ == "__main__":
    main()
