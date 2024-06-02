from collections import defaultdict


def get_factors(num: int) -> set:
    factors = set()

    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)

    return factors


def get_house_gifts(elf_limit: int, multiplier: int, threshold: int) -> int:
    elf_visits: dict = defaultdict(int)
    for idx in range(1, 1_000_000):
        gifts = 0
        factors = get_factors(idx)
        if not elf_limit:
            gifts = sum(factors) * multiplier
        else:
            for factor in factors:
                if elf_visits[factor] >= elf_limit:
                    pass
                else:
                    gifts += factor * multiplier
                    elf_visits[factor] += 1

        if gifts >= threshold:
            return idx


def main() -> None:
    threshold = 3_31_00_000
    result = get_house_gifts(elf_limit=0, multiplier=10, threshold=threshold)
    print(result)
    result = get_house_gifts(elf_limit=50, multiplier=11, threshold=threshold)
    print(result)


if __name__ == "__main__":
    main()
