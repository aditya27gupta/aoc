from typing import List


def count_containers(sizes: List[int], total_size: int, max_num: int) -> int:
    if total_size == 0:
        return 1
    if total_size < 0 or len(sizes) == 0 or max_num == 0:
        return 0

    count = 0
    for idx in range(len(sizes)):
        count += count_containers(
            sizes[idx + 1 :], total_size - sizes[idx], max_num - 1
        )

    return count


def main() -> None:
    with open("./input.txt", mode="r") as file:
        sizes: List = file.readlines()

    sizes = list(map(int, sizes))
    result = count_containers(sizes, total_size=150, max_num=len(sizes))
    print(result)

    for num in range(len(sizes)):
        result = count_containers(sizes, total_size=150, max_num=num)
        if result > 0:
            print(num, result)
            break


if __name__ == "__main__":
    main()
